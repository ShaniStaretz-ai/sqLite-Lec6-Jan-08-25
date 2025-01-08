# sqLite-Lec6-Jan-08-25
SQL 1-N, N-N
* N-N:
  * theory:
    *   usually will be in a separate table that contain the PK of 1st table and PK of 2nd table:
      * there are 2 ways to do it: 
        * a table A with **1 PK made from** the 2 PK from the 2 tables 
          * these PKs are FKs references to the 1st and 2nd tables
        * a table B with separated PK AI and 2 other **Unique** FKs of the PK from the other tables
  * in SQLite:
    * in table A:
     ```
       CREATE TABLE product_order (
       order_id INTEGER NOT NULL,
       product_id INTEGER NOT NULL,
       quantity INTEGER NOT NULL,
	                 PRIMARY KEY(order_id, product_id)
	      FOREIGN KEY (order_id) REFERENCES orders(order_id)
	      FOREIGN KEY (product_id) REFERENCES products(product_id)
	);
     ```
    * in table B:
    ```
    CREATE TABLE product_order (
	               product_order_id INTEGER PRIMARY KEY AUTOINCREMENT
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
	               UNIQUE(order_id, product_id)
	
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
        FOREIGN KEY (product_id) REFERENCES products(product_id)
	);
    ```
  * add alias to long tables names (op) and use it in the query
  ```
  select * from product_order op
  join product p on po.product_id=p.product_id
  ```
  * as "total price" instead as total_price
  
  ```
