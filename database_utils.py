# database_utils.py
import yaml
from sqlalchemy import create_engine

class DatabaseConnector:
    def __init__(self):
        self.engine = self.init_db_engine()

    def read_db_creds(self, file_path="db_creds.yaml"):
        pass

    def init_db_engine(self):
        pass

    def list_db_tables(self):
        pass

    def upload_to_db(self, data, table_name):
        pass

