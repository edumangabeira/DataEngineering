from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries
from dags.load_dim_table_subdag import load_dim_table

REDSHIFT_CONN_ID = 'redshift'
AWS_CREDENTIALS = 'aws_credentials'
S3_BUCKET = 'udacity-dend'
S3_SONG_KEY = 'song_data'
S3_LOG_KEY = 'log_data/{execution_date.year}/{execution_date.month}'
LOG_JSON_PATH = f's3://{S3_BUCKET}/log_json_path.json'
REGION = 'us-east-2'

default_args = {
    'owner': 'udacity',
    'start_date': datetime(2019, 1, 12),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False
}

dag = DAG('redshift_load_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='@hourly'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    redshift_conn_id=REDSHIFT_CONN_ID,
    aws_credentials_id=AWS_CREDENTIALS,
    table='staging_events',
    s3_bucket=S3_BUCKET,
    s3_key=S3_LOG_KEY,
    region=REGION,
    data_format=f"JSON '{LOG_JSON_PATH}'",
)

stage_songs_to_redshift = StageToRedshiftOperator(
   task_id='Stage_songs',
    dag=dag,
    redshift_conn_id=REDSHIFT_CONN_ID,
    aws_credentials_id=AWS_CREDENTIALS,
    table='staging_songs',
    s3_bucket=S3_BUCKET,
    s3_key=S3_LOG_KEY,
    region=REGION,
    data_format=f"JSON 'auto'",
)


load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,
    postgres_conn_id=REDSHIFT_CONN_ID,
    query=SqlQueries.songplay_table_insert,
    table='songplays',
)

load_dim_tables = SubDagOperator(
    subdag=load_dim_table(
        parent_dag_name='redshift_load_dag',
        task_id="Load_dimension_tables",
        default_args=default_args,
        postgres_conn_id=REDSHIFT_CONN_ID,
        sql_queries=[
            SqlQueries.user_table_insert,
            SqlQueries.song_table_insert,
            SqlQueries.artist_table_insert,
            SqlQueries.time_table_insert,
        ],
        tables=['users', 'songs', 'artists', 'time']
    ),
    dag=dag,
    task_id=load_dimension_table_task_id,
)

dq_checks=[
        {'check_sql': "SELECT COUNT(*) FROM songplays WHERE playid is null", 'expected_result': 0},
        {'check_sql': "SELECT COUNT(*) FROM users WHERE userid is null", 'expected_result': 0},
        {'check_sql': "SELECT COUNT(*) FROM songs WHERE songid is null", 'expected_result': 0},
        {'check_sql': "SELECT COUNT(*) FROM artists WHERE artistid is null", 'expected_result': 0},
        {'check_sql': "SELECT COUNT(*) FROM time WHERE start_time is null", 'expected_result': 0}
    ]
run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    postgres_conn_id=REDSHIFT_CONN_ID,
    tables=dq_checks
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


start_operator >> stage_events_to_redshift
start_operator >> stage_songs_to_redshift
stage_events_to_redshift >> load_songplays_table
stage_songs_to_redshift >>  load_songplays_table
load_songplays_table >> load_dim_tables
load_dim_tables >> run_quality_checks
run_quality_checks >> end_operator