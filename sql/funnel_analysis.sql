show databases;

use ecommerce;

CREATE TABLE ecommerce_funnel (
    user_id INT,
    session_id INT,
    date DATE,
    month VARCHAR(10),
    channel VARCHAR(50),
    campaign_type VARCHAR(50),
    device VARCHAR(30),
    user_type VARCHAR(30),
    region VARCHAR(30),
    visited_website VARCHAR(5),
    viewed_product VARCHAR(5),
    added_to_cart VARCHAR(5),
    checkout_started VARCHAR(5),
    purchase_completed VARCHAR(5),
    discount_applied VARCHAR(5),
    order_value DECIMAL(10,2),
    revenue DECIMAL(12,2)
);


SELECT count(SESSION_id) as total_session , count( DISTINCT user_id) 
as total_customers
from ecommerce_funnel;


SELECT count(case when purchase_completed='yes' then 1 end)
/count(session_id)*100 as conversion_rate from ecommerce_funnel;


SELECT COUNT(CASE WHEN purchase_completed = 'yes' THEN 1 END) 
AS total_purchases,
COUNT(session_id) AS total_sessions,
COUNT(CASE WHEN purchase_completed = 'yes' THEN 1 END)
/ COUNT(session_id) * 100 AS conversion_rate
FROM ecommerce_funnel;

SELECT count(case when visited_website='yes' then 1 end)
as website_visitors,
count(CASE when visited_website='yes' and viewed_product
='yes' then 1 end) as product_visitors,
count(CASE when visited_website='yes' and viewed_product
='yes' then 1 end)/count(case when visited_website='yes' then 1 end)*100
as conversion_rate
from ecommerce_funnel;


SELECT count(case when viewed_product='yes' then 1 end)
as product_viewed,count(CASE WHEN viewed_product='yes'
and added_to_cart='no' then 1 end) as drop_off_users_after_product_view,
count(CASE WHEN added_to_cart='yes' then 1 end)/
count(CASE WHEN viewed_product='yes' then 1 END)*100 as 
conversion_rate from ecommerce_funnel;


SELECT count(case when added_to_cart='yes' then 1 end) 
as cart_users,count(case when checkout_started='yes'
 then 1 end) as checkout_users,count(case when added_to_cart
='yes' and checkout_started='no' then 1 end ) as
drop_off_users_after_addedtocart,count(case when
checkout_started='yes' then 1 end)/count(case WHEN
added_to_cart='yes' then 1 end)*100 as conversion_rate
from ecommerce_funnel;


SELECT count(case when checkout_started='yes'
then 1 end) as checkout_users,count(case WHEN
purchase_completed='yes' then 1 end) as purchased_complete,
count(case when checkout_started='yes' AND
purchase_completed='no' then 1 end) as 
drop_off_after_checkout,
count(case when purchase_completed='yes' then 1 end)/
count(case when checkout_started='yes' then 1 end)*100 as conversion_rate
from ecommerce_funnel;


SELECT channel, 
count(session_id) as total_session,count(case when viewed_product='yes'
then 1 end) as viewed_product,count(case WHEN
added_to_cart='yes' then 1 end) as cart_users,
count(case when checkout_started='yes' then 1 end)
as checkout_users,count(case when purchase_completed=
'yes' then 1 end) as purchases,count(case WHEN
purchase_completed='yes' then 1 end)/count(session_id)*100
as conversion_rate,sum(revenue) as total_revenue
from ecommerce_funnel GROUP BY channel ;


SELECT device,count(SESSION_id) as total_sessions,
count(case when purchase_completed='yes' then 1 end)
as purchases,sum(revenue) as total_revenue,
sum(revenue)/count(case when purchase_completed='yes' 
then 1 end) as AOV, count(case when purchase_completed=
'yes' then 1 end)/count(session_id)*100 as conversion_rate
from ecommerce_funnel GROUP BY device;


SELECT user_type,count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end)
as purchases,sum(revenue)/count(case WHEN
purchase_completed='yes' then 1 end) as AOV,
sum(revenue) as total_revenue,count(case when purchase_completed=
'yes' then 1 end)/count(session_id)*100 as conversion_rate
from ecommerce_funnel GROUP BY user_type;


SELECT campaign_type,count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end)
as purchases,sum(revenue)/count(case WHEN
purchase_completed='yes' then 1 end) as AOV,
sum(revenue) as total_revenue,count(case when purchase_completed=
'yes' then 1 end)/count(session_id)*100 as conversion_rate
from ecommerce_funnel GROUP BY campaign_type;


SELECT channel,campaign_type,count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end)
as purchases,sum(revenue)/count(case WHEN
purchase_completed='yes' then 1 end) as AOV,
sum(revenue) as total_revenue,count(case when purchase_completed=
'yes' then 1 end)/count(session_id)*100 as conversion_rate
from ecommerce_funnel GROUP BY channel,campaign_type;


SELECT discount_applied,count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end)
as purchases,sum(revenue)/count(case WHEN
purchase_completed='yes' then 1 end) as AOV,
sum(revenue) as total_revenue,count(case when purchase_completed=
'yes' then 1 end)/count(session_id)*100 as conversion_rate
from ecommerce_funnel GROUP BY discount_applied;


SELECT count(case when discount_applied='yes'
and purchase_completed='no' then 1 end) FROM
ecommerce_funnel;


SELECT 
    discount_applied,
    purchase_completed,
    COUNT(*) AS sessions
FROM ecommerce_funnel
GROUP BY discount_applied, purchase_completed;


SELECT discount_applied,AVG(order_value)
as AOV from ecommerce_funnel GROUP BY
discount_applied;


SELECT user_type,discount_applied,
count(*) as total_session from ecommerce_funnel
GROUP BY user_type,discount_applied;


SELECT channel,count(case when viewed_product='yes' THEN
1 end)/count(case when visited_website='yes' then 1 END)
*100 as website_to_view_prodcut_CR,count(case WHEN
added_to_cart='yes' then 1 end)/count(case WHEN viewed_product=
'yes' then 1 end)*100 as viewed_product_to_added_cart_CR,
count(case when checkout_started='yes' then 1 end)/
count(case when added_to_cart='yes' then 1 end)*100 AS
added_to_cart_to_checkout_CR,count(case when purchase_completed=
'yes' then 1 end)/count(case when checkout_started='yes'
then 1 end)*100 as checkout_to_purchase_CR from ecommerce_funnel
GROUP BY channel;


SELECT user_type,device,discount_applied,
count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end) AS
purchases,count(case when purchase_completed='yes' then 1 end)/
count(session_id)*100 as conversion_rate,sum(revenue) AS
total_revenue,AVG(order_value) as AOV from ecommerce_funnel
GROUP BY user_type,device,discount_applied;


SELECT count(case when purchase_completed='yes' THEN
1 end) as purchases, sum(case when purchase_completed='yes'
then order_value else 0 end) as total_OV,
sum(case when purchase_completed='yes' then
revenue else 0 end) as total_revenue,
sum(case when purchase_completed='yes' then order_value
else 0 end)-sum(case when purchase_completed='yes' THEN
revenue else 0 end)
as revenue_leakage,(sum(case when purchase_completed='yes' then order_value
else 0 end)-sum(case when purchase_completed='yes' THEN
revenue else 0 end))/sum(case when purchase_completed='yes'
then order_value else 0 end)*100 as leakage_percent
from ecommerce_funnel;


SELECT discount_applied,sum(case WHEN
purchase_completed='yes' then order_value else 0 end)
as total_OV,sum(case when purchase_completed='yes' THEN
revenue else 0 end) as total_revenue,
sum(case when purchase_completed='yes' then order_value
else 0 end)-sum(case when purchase_completed='yes'
then revenue ELSE 0 end) as revenue_leakage,
(sum(case when purchase_completed='yes' THEN
order_value else 0 end)-sum(case when purchase_completed=
'yes' then revenue else 0 end))/sum(case when purchase_completed=
'yes' then order_value else 0 end)*100 as leakage_percent
from ecommerce_funnel GROUP BY discount_applied;


SELECT month,count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end)
as purchases,count(case when purchase_completed='yes'
then 1 end)/count(session_id)*100 as conversion_rate
from ecommerce_funnel GROUP BY month
ORDER BY month;


with monthly as (SELECT month,count(session_id)
as total_session,count(case when purchase_completed='yes' then 1 
end) as purchases,count(case when purchase_completed='yes' then
1 end )/count(session_id)*100 as conversion_rate 
from ecommerce_funnel GROUP BY month)
SELECT month,total_session,purchases,conversion_rate,
LAG(conversion_rate) over (order by month) as
previous_cr,conversion_rate-LAG(conversion_rate)
over (order by month) as CR_change
from monthly ORDER BY month;


SELECT CHANNEL,count(session_id) as total_session,
count(case when purchase_completed='yes' then 1 end)
as purchases,sum(revenue) as total_revenue,count(
case when purchase_completed='yes' then 1 end)/
count(session_id)*100 as CR,sum(revenue)/count(session_id)
*1000 as revenue_per_1000_session FROM ecommerce_funnel
GROUP BY channel;


SELECT * FROM ecommerce_funnel LIMIT 100;