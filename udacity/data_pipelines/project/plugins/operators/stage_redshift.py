from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    template_fields = ('s3_key',)
    sql_copy = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        {} REGION '{}'
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 target_table="",
                 s3_bucket="",
                 s3_key="",
                 region="",
                 data_format="",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.target_table = target_table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.data_format = data_format

    def execute(self, context):
        self.log.info('Stablishing hooks and connections...')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        aws_hook = AwsHook(self.aws_credentials_id)
        self.log.info('Validating credentials...')
        credentials = aws_hook.get_credentials()
        
        s3_key_render = self.s3_key.format(**context)
        s3_path = f's3://{self.s3_bucket}/{s3_key_render}'
        query = StageToRedshiftOperator.sql_copy.format(
            self.target_table, 
            s3_path, 
            credentials.access_key,
            credentials.secret_key,
            self.data_format, 
            self.region
        )

        self.log.info('Copying data from {s3_path} to Redshift {self.target_table}')
        redshift.run(query)