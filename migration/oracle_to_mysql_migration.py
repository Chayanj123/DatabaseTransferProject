# migrations/oracle_to_mysql_migration.py
import mysql.connector
import cx_Oracle
from config.database_config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from config.database_config import ORACLE_HOST, ORACLE_PORT, ORACLE_SID, ORACLE_USER, ORACLE_PASSWORD

def migrate_oracle_to_mysql():
    # Connect to Oracle
    dsn_tns = cx_Oracle.makedsn(ORACLE_HOST, ORACLE_PORT, service_name=ORACLE_SID)
    oracle_conn = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASSWORD, dsn=dsn_tns)
    oracle_cursor = oracle_conn.cursor()

    # Connect to MySQL
    mysql_conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    mysql_cursor = mysql_conn.cursor()

    # Example query to fetch data from Oracle and insert into MySQL
    oracle_cursor.execute("SELECT * FROM source_table")
    rows = oracle_cursor.fetchall()
    for row in rows:
        mysql_cursor.execute("INSERT INTO destination_table (column1, column2) VALUES (%s, %s)", row)
    
    mysql_conn.commit()
    oracle_cursor.close()
    oracle_conn.close()
    mysql_cursor.close()
    mysql_conn.close()
