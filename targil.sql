--detect the total price of order id == 2
select sum(products.price*product_order.quantity) as total_price
from product_order
join products on product_order.product_id ==products.product_id
where order_id=2;

--detect the total price per order (don't forget price x quantity)
select product_order.order_id,sum(products.price*product_order.quantity) as total_price
from product_order
join products on product_order.product_id ==products.product_id
GROUP by product_order.order_id