from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    sql_insert = """
        INSERT INTO {}
        {}
        ;
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 query="",
                 delete_load=False,
                 table="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.query = query
        self.delete_load = delete_load
        self.table = table

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.delete_load:
            self.log.info("Deleting Redshift table before loading data")
            redshift.run("DELETE FROM {}".format(self.query))

        insert = LoadDimensionOperator.insert_sql.format(
            self.query,
            self.table
        )
        self.log.info(f"Executing {insert} ...")
        redshift.run(insert)
        self.log.info(f"Data loaded into redshift")