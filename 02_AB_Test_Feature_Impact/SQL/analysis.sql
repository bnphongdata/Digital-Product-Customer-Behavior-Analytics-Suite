-- name: variant_summary
-- 1. Tổng hợp các chỉ số theo biến thể thử nghiệm (phiên, chuyển đổi, tỷ lệ thoát, điểm tương tác, doanh thu)
SELECT variant,COUNT(*) AS sessions,SUM(converted) AS conversions,
 AVG(1.0*converted) AS conversion_rate,AVG(1.0*bounce) AS bounce_rate,
 AVG(engagement_score) AS mean_engagement,SUM(revenue) AS revenue,
 AVG(revenue) AS revenue_per_session
FROM ab_sessions_clean GROUP BY variant ORDER BY variant;

-- name: segment_conversion
-- 2. Đánh giá tỷ lệ chuyển đổi chi tiết theo từng phân khúc thiết bị và nguồn truy cập
SELECT device, source, variant, COUNT(*) AS sessions,SUM(converted) AS conversions,
 AVG(1.0*converted) AS conversion_rate
FROM ab_sessions_clean GROUP BY device,source,variant ORDER BY device,source,variant;

-- name: daily_assignment
-- 3. Theo dõi số lượng phiên và lượt chuyển đổi được phân bổ theo từng ngày thử nghiệm
SELECT session_date, variant,COUNT(*) AS sessions,SUM(converted) AS conversions
FROM ab_sessions_clean GROUP BY session_date,variant ORDER BY session_date,variant;
