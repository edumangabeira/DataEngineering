import logging

from airflow import DAG
from airflow.operators import LoadDimensionOperator

def load_dim_table(
        parent_dag,
        task_id,
        default_args,
        postgres_conn_id,
        sql_queries,
        tables,
        *args,
        **kwargs):

    dag = DAG(
        dag_id=f'{parent_dag}.{task_id}',
        default_args=default_args,
        **kwargs,
    )

    tasks = []
    for target_table, query in zip(tables, sql_queries):
        task = LoadDimensionOperator(
            task_id=f'Load_{target_table}_dim_table',
            dag=dag,
            postgres_conn_id=postgres_conn_id,
            sql=query,
            table=table
        )
        tasks.append(task)

    return dag