import pandas as pd

# Sales table
sales_data = {
    "sale_id": [1, 2, 7],
    "product_id": [100, 100, 200],
    "year": [2008, 2009, 2011],
    "quantity": [10, 12, 15],
    "price": [5000, 5000, 9000]
}
sales = pd.DataFrame(sales_data)

# Product table
product_data = {
    "product_id": [100, 200, 300],
    "product_name": ["Nokia", "Apple", "Samsung"]
}
product = pd.DataFrame(product_data)


result=pd.merge(sales, product,on="product_id", how="inner")[["product_name","year","price"]]

print(result)