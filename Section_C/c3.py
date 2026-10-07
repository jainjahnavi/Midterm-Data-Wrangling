from airflow.sdk import dag, task


@dag(dag_id="stock_check")
def stock_check():

    @task
    def check_stock():
        return {"item": "rice", "qty": 12}

    @task.branch
    def decide(data):
        if data["qty"] < 20:
            return "place_order"
        return "skip_order"

    @task
    def place_order():
        print("Stock low! Order placed successfully.")

    @task
    def skip_order():
        print("Stock sufficient. No order needed.")

    @task(trigger_rule="one_success")
    def notify():
        print("Stock Check done")

    # Workflow dependencies
    stock_data = check_stock()
    branch = decide(stock_data)

    p_order = place_order()
    s_order = skip_order()

    branch >> [p_order, s_order]
    [p_order, s_order] >> notify()


stock_check()

