DELIMITER //
CREATE TRIGGER check_comments_curse_words
BEFORE INSERT ON comments
FOR EACH ROW
BEGIN
    IF NEW.text LIKE '%kurwa%' THEN
        SIGNAL SQLSTATE '23000'
        SET MESSAGE_TEXT = 'Don`t use bad words silly';
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER update_statistics
AFTER INSERT ON reactions
FOR EACH ROW
BEGIN
    UPDATE statistic
    SET reactions_amount = reactions_amount + 1,
        comments_amount = comments_amount + (CASE WHEN NEW.reactions_type = 'Comment' THEN 1 ELSE 0 END),
        views_amount = views_amount + 1
    WHERE user_account_userID = NEW.userID;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER update_followers_amount
AFTER INSERT ON follower
FOR EACH ROW
BEGIN
    UPDATE user_account
    SET follower_amount = follower_amount + 1
    WHERE userID = NEW.user_account_userID1;
END;
//
DELIMITER ;

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
END //
DELIMITER ;