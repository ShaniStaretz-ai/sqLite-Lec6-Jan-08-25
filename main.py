
import sqlite3

def input_order():
    product_name=input("enter a new product name:")
    product_price = float(input("enter a price for the product:"))
    db_name: str = "Jan-8-25.db"
    connector = sqlite3.connect(db_name)
    connector.row_factory = sqlite3.Row
    cursor = connector.cursor()
    query='INSERT INTO products (name, price) VALUES (?, ?);'
    cursor.execute(query, (product_name,product_price))
    connector.commit()
    select_query='SELECT products.* from products'
    rows=cursor.execute(select_query)
    rows_list = [tuple(row) for row in rows]
    for row in rows_list:
        print(row)

if __name__ == '__main__':
    input_order()
