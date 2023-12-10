DELIMITER //
CREATE PROCEDURE InsertStorie (
	IN storie_id INT,
    IN follower_id INT,
    IN views_amount INT,
    IN user_account_userID INT
) 
BEGIN 
	INSERT INTO storie (storieID, follower_id, views_amount, user_account_userID)
    VALUES (storie_id, follower_id, views_amount, user_account_userID);
END;
//
DELIMITER ;
CALL InsertStorie(5, 1, 243, 1);


DELIMITER //
CREATE PROCEDURE InsertsUserAccount(
    IN nickname VARCHAR(45),
    IN follower_amount INT,
    IN photo_amount INT,
    IN storie_amount INT
)
BEGIN
    INSERT INTO user_account (nickname, follower_amount, photo_amount, storie_amount)
    VALUES (nickname, follower_amount, photo_amount, storie_amount);
END //
DELIMITER ;
CALL InsertsUserAccount("drtfgyhuji", 100, 20, 30);

DELIMITER //
CREATE PROCEDURE InsertNamesIntoUserInfo()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        INSERT INTO user_info (name, age, gender, user_account_userID)
		VALUES (CONCAT('Noname', counter), FLOOR(RAND() * 100), CASE WHEN (RAND()*100) > 50 THEN 'M' ELSE 'F' END, counter);
        
        SET counter = counter + 1;
    END WHILE;
END //
DELIMITER ;
CALL InsertNamesIntoUserInfo();

