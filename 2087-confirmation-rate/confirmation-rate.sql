SELECT 
    si.user_id, 
    Round(COALESCE(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.user_id), 0),2) AS confirmation_rate
FROM 
    confirmations c
Right JOIN 
    signups si ON si.user_id = c.user_id 
GROUP BY 
    si.user_id
ORDER BY
    si.user_id;
