-- name: summary
-- 1. Tổng quan giao dịch bán hàng trên sàn (số dòng, số lượng bán, doanh thu, chênh lệch giá x số lượng, số người bán)
SELECT COUNT(*) AS sales_rows,SUM(units_sold) AS units,SUM(revenue) AS recorded_revenue,
 SUM(price*units_sold) AS price_times_units,
 SUM(ABS(revenue-price*units_sold)>0.011) AS revenue_discrepancy_rows,
 COUNT(DISTINCT seller_id) AS sellers FROM sales_clean;

-- name: seller_concentration
-- 2. Phân tích mức độ tập trung doanh thu theo từng nhà bán hàng (seller)
WITH seller AS (SELECT seller_id,SUM(revenue) AS revenue FROM sales_clean GROUP BY seller_id),
 ranked AS (SELECT *,ROW_NUMBER() OVER(ORDER BY revenue DESC,seller_id) AS rank,
 SUM(revenue) OVER() AS total_revenue FROM seller)
SELECT *,revenue/NULLIF(total_revenue,0) AS revenue_share FROM ranked ORDER BY rank;

-- name: category_performance
-- 3. Hiệu quả kinh doanh và đóng góp doanh thu theo từng ngành hàng sản phẩm
SELECT category,SUM(revenue) AS recorded_revenue,SUM(units_sold) AS units,COUNT(*) AS sales_rows
FROM sales_clean GROUP BY category ORDER BY recorded_revenue DESC;

-- name: stock_status_association
-- 4. Tương quan giữa trạng thái tồn kho (in_stock), khoảng giá và doanh thu trung bình của tin đăng
WITH r AS (SELECT listing_id,SUM(revenue) AS revenue FROM sales_clean GROUP BY listing_id)
SELECT l.category,CASE WHEN l.price<50 THEN 'Under 50' WHEN l.price<100 THEN '50 to 99.99' ELSE '100+' END AS price_band,
 l.in_stock,COUNT(*) AS listings,AVG(COALESCE(r.revenue,0)) AS mean_recorded_revenue
FROM listings_clean l LEFT JOIN r USING(listing_id)
GROUP BY l.category,price_band,l.in_stock ORDER BY l.category,price_band,l.in_stock;
