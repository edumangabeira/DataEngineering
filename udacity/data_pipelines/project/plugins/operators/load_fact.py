from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'
    sql_insert = """
        INSERT INTO {}
        {}
        ;
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 query="",
                 table="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.query = query
        self.table = table

    def execute(self, context):
        self.log.info('Stablishing hooks and connections...')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        insert = LoadFactOperator.sql_insert.format(
            self.query,
            self.table
        )
        self.log.info(f"Executing {insert } ...")
        redshift.run(insert)
        self.log.info(f"Data loaded into redshift")