import cx_Oracle
import logging

logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
class DBConnection:

    def __init__(self,user:str,passw:str,port:int,hostname:str,servicename:str):
        cx_Oracle.init_oracle_client(lib_dir="D:\Programe\oracle\instantclient_21_3")
        self.dsn_tns = cx_Oracle.makedsn(hostname, port, service_name=servicename)

        self.user=user
        self.passw=passw

        self.connection=None
        self.cursor=None

        self.is_connected=False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        if exc_type:
            logging.exception(f"{exc_type}: {exc_val} -> {exc_tb}")

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(user=self.user, password=self.passw, dsn=self.dsn_tns)
            self.is_connected=True
            logging.info("Connected to database")
        except cx_Oracle.Error as err:
            self.log_error(err)

    def disconnect(self):
        if self.is_connected and self.connection:
            try:
                self.connection.close()
                self.is_connected = False
                logging.info("Disconnected from database")
            except cx_Oracle.Error as err:
                self.log_error(err)


    # functie utila pt interogari
    def fetch_data(self,sql_query:str):
        response = None
        try:
            self.cursor=self.connection.cursor()
            self.cursor.execute(sql_query)
            response=self.cursor

        except cx_Oracle.Error as err:
            self.log_error(err)

        return response

    # functie utilizata pt modificari efectuate in baza de date (insert/update/delete)
    def exec_cmd(self,sql_cmd:str):
        response=False
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_cmd)
                self.connection.commit()
                response=True
        except cx_Oracle.Error as err:
            self.log_error(err)
        return response


    @staticmethod
    def log_error(err):
        logging.error(f"Database error: {err}")