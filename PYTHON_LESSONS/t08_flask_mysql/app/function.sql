DELIMITER //
CREATE FUNCTION getMaxAgeUserInfo()
RETURNS DECIMAL
READS SQL DATA
BEGIN
    DECLARE max_age DECIMAL;
    SELECT MAX(age) INTO max_age
    FROM user_info;
    RETURN max_age;
END //
DELIMITER ;
SELECT getMaxAgeUserInfo() AS get_max_age_user_info;