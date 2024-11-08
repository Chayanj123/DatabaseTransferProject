import mysql.connector
import cx_Oracle
import logging
from config.database_config import MYSQL_CONFIG, ORACLE_CONFIG

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_mysql_connection():
    """Create a connection to MySQL database."""
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        return conn
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to MySQL: {err}")
        raise

def create_oracle_connection():
    """Create a connection to Oracle database."""
    try:
        conn = cx_Oracle.connect(**ORACLE_CONFIG)
        return conn
    except cx_Oracle.DatabaseError as err:
        logging.error(f"Error connecting to Oracle: {err}")
        raise

def perform_transfer(source_db='MySQL', destination_db='Oracle', table_name='your_table'):
    """Perform data transfer from source_db to destination_db."""
    logging.info(f"Starting data transfer from {source_db} to {destination_db} for table {table_name}")

    source_conn = None
    dest_conn = None

    try:
        if source_db == 'MySQL':
            source_conn = create_mysql_connection()
            source_cursor = source_conn.cursor()
            source_cursor.execute(f"SELECT * FROM {table_name}")
            data = source_cursor.fetchall()
        elif source_db == 'Oracle':
            source_conn = create_oracle_connection()
            source_cursor = source_conn.cursor()
            source_cursor.execute(f"SELECT * FROM {table_name}")
            data = source_cursor.fetchall()
        else:
            logging.error("Invalid source database")
            raise ValueError("Invalid source database")

        if destination_db == 'MySQL':
            dest_conn = create_mysql_connection()
            dest_cursor = dest_conn.cursor()
            dest_cursor.execute(f"DELETE FROM {table_name}")  # Clear the destination table
            dest_cursor.executemany(f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(data[0]))})", data)
            dest_conn.commit()
        elif destination_db == 'Oracle':
            dest_conn = create_oracle_connection()
            dest_cursor = dest_conn.cursor()
            dest_cursor.execute(f"DELETE FROM {table_name}")  # Clear the destination table
            dest_cursor.executemany(f"INSERT INTO {table_name} VALUES ({', '.join([':1'] * len(data[0]))})", data)
            dest_conn.commit()
        else:
            logging.error("Invalid destination database")
            raise ValueError("Invalid destination database")

        logging.info(f"Data transfer completed successfully from {source_db} to {destination_db}")

    except Exception as e:
        logging.error(f"Error during data transfer: {e}")

    finally:
        if source_conn:
            source_conn.close()
        if dest_conn:
            dest_conn.close()

if __name__ == "__main__":
    perform_transfer(source_db='MySQL', destination_db='Oracle', table_name='your_table')
