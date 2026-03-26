import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})


merge_df=pd.merge(customers, orders,how='left', left_on="id",right_on="customerId")


no_orders = merge_df[merge_df['customerId'].isna()]

no_orders=no_orders.rename(columns={"name":"Customers"})[["Customers"]]

print(no_orders)
