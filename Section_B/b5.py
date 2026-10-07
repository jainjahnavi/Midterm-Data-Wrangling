"""
In the airflow code, 2 main things are missing and wrong
1. We need to call the functions inside the dag.
-->extract_sol= extract()
-->total_sol= total(extract_sol)  #we have to call it before

2. then, the next line will be: 
-->extract_sol >> total_sol

3. We need to call the dag.
-->report_dag()
"""
#Actual Code
from airflow.sdk import dag,task

@dag(dag_id="daily_report",schedule=None)
def report_task():

    @task.python
    def extract():
        return [1,2,3]

    @task.python
    def total(numbers):
        print(sum(numbers))


    extract_sol=extract()
    total_sol=total(extract_sol)

    extract >> total

report_dag()

    



