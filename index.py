import sqlite3
import os
from jenkinsapi.jenkins import Jenkins

# create connection to sqlite database


def create_connection():
    try:
        dir = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'sqlite.db')
        conn = sqlite3.connect(dir)
        return conn
    except Exception as e:
        print('error', e)
    finally:
        conn.close()


# get a jenkins server instance

def get_server_instance():
    jenkins_url = 'http://jenkins_host:8080'
    server = Jenkins(jenkins_url, username='foouser',
                     password='foopassword')
    return server

# get the details of the instance server jobs and insert into jobs table in sqlite database


def get_job_details():
    server = get_server_instance()
    conn = create_connection()
    createTableSql = """ CREATE TABLE IF NOT EXISTS JOBS (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        jobname text NOT NULL,
                                        status text,
                                        datechecked date default CURRENT_TIMESTAMP

                                    ); """
    createTable(conn, createTableSql)
    insertsql = ''' INSERT INTO JOBS(jobname,status)
              VALUES(?,?) '''
    for job_instance in server.get_jobs():
        cur = conn.cursor()
        cur.execute(insertsql, [job_instance.name, job_instance.is_running()])
    pass
# create a table JOB to store the jobs status


def createTable(conn, createTableSql):
    try:
        cur = conn.cursor()
        cur.execute(createTableSql)
    except Exception as error:
        print(error)
    pass
# run the script


get_job_details()
