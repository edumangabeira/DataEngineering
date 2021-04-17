from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 tables=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.tables= tables
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        self.log.info('Stablishing hooks and connections...')
        redshift = PostgresHook(self.redshift_conn_id)
        errors = 0
        failures = []
        
        for target_table in tables:
            query = check.get('check_sql')
            result = check.get('expected_result')
            self.log.info(f"Checking for records in {query} ...")
            records = redshift.get_records(query)[0]
            if result != records[0]:
                errors += 1
                failures.append(query)
        if errors > 0:
            self.log.info('Expected number of rows not found at:')
            self.log.info(failures)
            raise ValueError('Data quality check failed')
        else:
            self.log.info("All data quality checks passed")