DELIMITER //
CREATE PROCEDURE InsertFollower(
    IN p_userID1 INT,
    IN p_userID2 INT
)
BEGIN
    INSERT INTO follower (user_account_userID, user_account_userID1)
    VALUES (p_userID1, p_userID2);
    
    UPDATE user_account
    SET follower_amount = follower_amount + 1
    WHERE userID IN (p_userID1, p_userID2);
END;
//
DELIMITER ;
CALL InsertFollower(2, 5);


DELIMITER //
CREATE PROCEDURE InsertUserAccount(
    IN p_nickname VARCHAR(45),
    IN p_follower_amount INT,
    IN p_photo_amount INT,
    IN p_storie_amount INT
)
BEGIN
    INSERT INTO user_account (nickname, follower_amount, photo_amount, storie_amount)
    VALUES (p_nickname, p_follower_amount, p_photo_amount, p_storie_amount);
END //
DELIMITER ;
CALL InsertUserAccount("Noname19", 100, 20, 30);

DELIMITER //
CREATE PROCEDURE InsertRowsIntoUserInfo()
BEGIN
    SET @counter = 1;

    WHILE @counter <= 10 DO
        SET @row_value = CONCAT('Noname', @counter);

        INSERT INTO user_info (name, age, gender, user_account_userID)
        VALUES (@row_value, FLOOR(RAND() * 30) + 20, IF(@counter % 2 = 0, 'F', 'M'), @counter);

        SET @counter = @counter + 1;
    END WHILE;
END //
DELIMITER ;
CALL InsertRowsIntoUserInfo();

