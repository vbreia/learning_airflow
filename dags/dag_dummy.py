from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator

# Definindo argumentos padrão	
default_args = {
    'owner': 'Victor', #dono da DAG
    'depends_on_past': False, #não depende de DAGs anteriores
    'start_date': datetime.now(), #data de início
    'email_on_failure': False, #não envia email em caso de falha
    'email_on_retry': False, #não envia email em caso de retry
    'retries': 1, #número de tentativas
    'retry_delay': timedelta(minutes=5), #intervalo entre as tentativas
    }

# Definindo a DAG
dag = DAG(
    'dag_dummy',
    default_args=default_args,
    description='A simple dummy DAG',
    schedule_interval=timedelta(days=1), #intervalo de execução
)

# Definindo os operadores
start = DummyOperator(
    task_id='start',  #nome da task
    dag=dag #DAG ao qual a task pertence
    )

sleep = BashOperator(
    task_id='sleep', #nome da task
    bash_command='sleep 10', #comando a ser executado
    dag=dag #DAG ao qual a task pertence
    )

end = DummyOperator(task_id='end', #nome da task
                    dag=dag #DAG ao qual a task pertence
                    )

start >> [sleep] >> end #definindo a ordem de execução das tasks