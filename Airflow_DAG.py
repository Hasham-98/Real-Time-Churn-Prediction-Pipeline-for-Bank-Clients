from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.utils.email import send_email_smtp


default_args = {
    'owner': 'Hossam',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 24),
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

def starter():
    apache_airflow_job = """
    AAAAA   PPPPP    AAAAA    CCCCC   H    H  EEEEE           AAAAA  III  RRRRR   FFFFF  L       OOOOO  W     W
    A     A  P    P  A     A  C        H    H  E               A     A  I   R    R  F      L      O     O  W     W
    AAAAAAA  PPPPP   AAAAAAA  C        HHHHHH  EEEEE           AAAAAAA  I   RRRRR   FFFFF  L      O     O  W  W  W
    A     A  P       A     A  C        H    H  E               A     A  I   R    R  F      L      O     O   W W W
    A     A  P       A     A   CCCCC   H    H  EEEEE           A     A  III  R    R  F      LLLLL   OOOOO     W W
    """

    hossam_fid_signature = """
    Written by Hossam Fid
    """

    print(apache_airflow_job)
    print(hossam_fid_signature)
    print("Apache Airflow job started working! .........")

def check_connection(**kwargs):
    s3_hook = S3Hook(aws_conn_id='s3_connection')
    connection_status = s3_hook.check_for_bucket('graduationprojectbucket')
    
    if connection_status:
        print("connection successfully ^_^ 100%")
    else:
        print("S3 connection failed S3 connection failed S3 connection failed")
    

def download_csv_from_s3(**kwargs):
    s3_hook = S3Hook(aws_conn_id='s3_connection')  
    bucket_name = 'graduationprojectbucket'
    s3_key = 'Churn_Modelling.csv'  

    
    file_content = s3_hook.read_key(key=s3_key, bucket_name=bucket_name) #download the csvfile

    #save the file locally
    #local_file_path = 'C:/Users/hossa/OneDrive/Desktop/churndata.csv'  
    local_file_path = 'churndata.csv'  
    with open(local_file_path, 'w') as file:
        file.write(file_content)

    print(f"File downloaded to ==>>> {local_file_path}")

'''
def send_email():
    send_email_smtp(
        to='mrhossamfid@gmail.com',
        subject='Airflow CHurn DAG Run',
        html_content=' Airflow DAG has completed successfully!'
    )
'''

with DAG('s3_data_load_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    job_start = PythonOperator(
        task_id='job_start',
        python_callable=starter
    )


    check_connection = PythonOperator(
        task_id='check_s3_connection',
        python_callable=check_connection,
        provide_context=True
    )


    download_csv_task = PythonOperator(
        task_id='download_csv_from_s3',
        python_callable=download_csv_from_s3,
        provide_context=True
    )
'''
    email_task = PythonOperator(
    task_id='send_success_email',
    python_callable=send_email,
    provide_context=True
    
    
    
   )
'''
job_start   >>check_connection >>  download_csv_task 
    
    
    
    
    
