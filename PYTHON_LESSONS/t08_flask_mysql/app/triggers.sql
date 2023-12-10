DELIMITER //
CREATE TRIGGER check_comments_curse_words
BEFORE INSERT ON comments
FOR EACH ROW
BEGIN
    IF NEW.text LIKE '%kurwa%' THEN
        SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Don`t use bad words silly';
    END IF;
END 
// DELIMITER;


DELIMITER //
CREATE TRIGGER check_user_info_nickname
BEFORE INSERT ON user_info
FOR EACH ROW
BEGIN 
	IF CHAR_LENGTH(NEW.name) > 15 THEN 
		SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Nickname is too long, write shorter one';
	END IF;
END 
// DELIMETER;
    

DELIMITER //
CREATE TRIGGER insert_comments_trigger
BEFORE INSERT ON comments
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT * FROM user_account WHERE userID = NEW.userID) THEN
        SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Error!!!!!!!!!! userID does not exist';
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER update_comments_trigger
BEFORE UPDATE ON comments
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT * FROM user_account WHERE userID = NEW.userID) THEN
        SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Error!!!!!!!!!! userID does not exist';
    END IF;
END 
// DELIMITER ;