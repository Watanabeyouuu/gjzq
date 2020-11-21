SELECT DISTINCT hist_date, NULL AS active_device, sales AS new_device, NULL AS year_date, date_month AS month_date,
IF ( sales * screen_area_m2 = 0, NULL, sales * screen_area_m2 ) AS screen_area_m2_total, brand,
back_cam_1_group AS `back_cam1主摄像素分布（组）`, back_cam_num, battery_vol_group AS `battery_vol（组）`, CPU_brand, 
fingerprint_type, front_cam_1, front_cam_num,
IF ( full_screen = "", 0, full_screen ) AS full_screen,
IF ( OLED = "", 0, OLED ) AS OLED, ppi_group AS `ppi（组）`,
IF ( quick_charge = "", 0, quick_charge ) AS quick_charge, screen_area_m2, screen_per AS `screen_perc（组）`,
IF ( wireless_charge = "", 0, wireless_charge ) AS wireless_charge, ROUND( screen_size ) AS screen_size, IP,
front_cam_1_group AS `front_cam1主摄像素分布（组）`, 5G AS G5 
FROM tab_mobile_sales AS s LEFT JOIN tab_mobile_file_info AS f 
ON f.id = s.m_index 
ORDER BY hist_date
-- 数据跟踪