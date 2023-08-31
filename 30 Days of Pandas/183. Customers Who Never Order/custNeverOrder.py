import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_id_uniq_order = orders['customerId'].unique()
    cust_id_order = customers[~customers['id'].isin(cust_id_uniq_order)]
    result = cust_id_order['name'].rename(columns={'name': 'Customers'})

    return result