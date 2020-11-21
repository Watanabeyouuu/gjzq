SELECT DISTINCT hist_date, NULL as active_device, sales as new_device, NULL as year_date, 
date_month as month_date, if(s.mobile_name='其余安卓机型', '其他', brand) as brand, 
s.mobile_name as modern_clean, if(s.mobile_name='其余安卓机型', 
'其他', top5_brand) as top5_brand, 5G as G5
FROM tab_mobile_sales s LEFT JOIN tab_mobile_file_info f
ON f.id = s.m_index
ORDER BY hist_date, s.mobile_name
-- 销量数据