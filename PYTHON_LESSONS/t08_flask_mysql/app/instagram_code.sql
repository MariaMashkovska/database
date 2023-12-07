-- MySQL Workbench Forward Engineering

SET @OLD_UNcommentscommentscommentsIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

CREATE DATABASE IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8;
USE mydb;

-- -----------------------------------------------------
-- Table `mydb`.`user_account`
-- -----------------------------------------------------

DROP TABLE IF EXISTS comments;
CREATE TABLE IF NOT EXISTS comments (
  commentID INT NOT NULL AUTO_INCREMENT,
  text VARCHAR(2200) NULL,
  userID VARCHAR(45) NOT NULL,
  PRIMARY KEY (commentID)
)
ENGINE = InnoDB;

-- Table user_account
DROP TABLE IF EXISTS user_account;
CREATE TABLE user_account (
  userID INT NOT NULL AUTO_INCREMENT,
  nickname VARCHAR(45) NOT NULL,
  follower_amount INT NOT NULL,
  photo_amount INT NULL,
  storie_amount INT NULL,
  INDEX idx_nickname (nickname),
  INDEX idx_follower_amount (follower_amount),
  PRIMARY KEY (userID)
) ENGINE = InnoDB;

-- Table storie
DROP TABLE IF EXISTS storie;
CREATE TABLE storie (
  storieID INT NOT NULL AUTO_INCREMENT,
  follower_id INT NOT NULL,
  views_amount INT NULL,
  user_account_userID INT NOT NULL,
  PRIMARY KEY (storieID, user_account_userID),
  INDEX idx_follower_id (follower_id),
  INDEX idx_storieID (storieId),
  FOREIGN KEY (user_account_userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Table report
DROP TABLE IF EXISTS report;
CREATE TABLE report (
  reportID INT NOT NULL AUTO_INCREMENT,
  text VARCHAR(300) NULL,
  INDEX idx_reportID_text (reportID, text),
  INDEX idx_text (text),
  PRIMARY KEY (reportID)
) ENGINE = InnoDB;


-- Table views
DROP TABLE IF EXISTS views;
CREATE TABLE views (
  viewsID INT NOT NULL AUTO_INCREMENT,
  storie_storieID INT NOT NULL,
  user_account_userID INT NOT NULL,
  report_reportID INT NOT NULL,
  PRIMARY KEY (viewsID, storie_storieID),
  FOREIGN KEY (storie_storieID) REFERENCES storie (storieID) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (user_account_userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (report_reportID) REFERENCES report (reportID) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Table reactions
DROP TABLE IF EXISTS reactions;
CREATE TABLE reactions (
  reactionsID INT NOT NULL AUTO_INCREMENT,
  reactions_type VARCHAR(3663) NULL,
  userID INT NOT NULL,
  views_viewsID INT NOT NULL,
  views_storie_storieID INT NOT NULL,
  PRIMARY KEY (reactionsID),
  FOREIGN KEY (views_viewsID, views_storie_storieID) REFERENCES views (viewsID, storie_storieID) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Table media
DROP TABLE IF EXISTS media;
CREATE TABLE media (
  mediaID INT NOT NULL AUTO_INCREMENT,
  media_url VARCHAR(250) NOT NULL,
  storie_storieID INT NOT NULL,
  storie_user_account_userID INT NOT NULL,
  media_type VARCHAR(10) NULL,
  PRIMARY KEY (mediaID),
  INDEX idx_media_url (media_url),
  FOREIGN KEY (storie_storieID) REFERENCES storie (storieID) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (storie_user_account_userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Table statistic
DROP TABLE IF EXISTS statistic;
CREATE TABLE statistic (
  statisticID INT NOT NULL AUTO_INCREMENT,
  comments_amount INT NULL,
  views_amount INT NULL,
  reactions_amount INT NULL,
  user_account_userID INT NOT NULL,
  PRIMARY KEY (statisticID),
  INDEX idx_reactions_amount (reactions_amount),
  FOREIGN KEY (user_account_userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION
  ) ENGINE = InnoDB;


-- Table user_info
DROP TABLE IF EXISTS user_info;
CREATE TABLE user_info (
  user_infoID INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  age INT NOT NULL,
  gender VARCHAR(3) NOT NULL,
  user_account_userID INT NOT NULL,
  INDEX idx_name (name),
  INDEX idx_age (age),
  PRIMARY KEY (user_infoID),
  FOREIGN KEY (user_account_userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Table follower
DROP TABLE IF EXISTS follower;
CREATE TABLE follower (
  user_account_userID INT NOT NULL,
  user_account_userID1 INT NOT NULL,
  PRIMARY KEY (user_account_userID, user_account_userID1),
  INDEX idx_user_account_userID (user_account_userID),
  FOREIGN KEY (user_account_userID) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (user_account_userID1) REFERENCES user_account (userID) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- Table user_account
INSERT INTO user_account (nickname, follower_amount, photo_amount, storie_amount) VALUES
('User1', 100, 20, 30),
('User2', 200, 10, 40),
('User3', 150, 15, 35),
('User4', 180, 18, 42),
('User5', 90, 9, 27),
('User6', 120, 12, 36),
('User7', 250, 25, 45),
('User8', 80, 8, 24),
('User9', 60, 6, 18),
('User10', 110, 11, 33);

-- Table storie
INSERT INTO storie (follower_id, views_amount, user_account_userID) VALUES
(1, 50, 1),
(2, 60, 2),
(3, 70, 3),
(4, 80, 4),
(5, 45, 5),
(6, 55, 6),
(7, 65, 7),
(8, 75, 8),
(9, 85, 9),
(10, 95, 10);

-- Table report
INSERT INTO report (text) VALUES
('Report 1'),
('Report 2'),
('Report 3'),
('Report 4'),
('Report 5'),
('Report 6'),
('Report 7'),
('Report 8'),
('Report 9'),
('Report 10');

-- Table views
INSERT INTO views (storie_storieID, user_account_userID, report_reportID) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- Table reactions
INSERT INTO reactions (reactions_type, userID, views_viewsID, views_storie_storieID) VALUES
('Like', 1, 1, 1),
('Comment', 2, 2, 2),
('Like', 3, 3, 3),
('Comment', 4, 4, 4),
('Like', 5, 5, 5),
('Comment', 6, 6, 6),
('Like', 7, 7, 7),
('Comment', 8, 8, 8),
('Like', 9, 9, 9),
('Comment', 10, 10, 10);

-- Table media
INSERT INTO media (media_url, storie_storieID, storie_user_account_userID, media_type) VALUES
('media_url_1', 1, 1, 'Image'),
('media_url_2', 2, 2, 'Video'),
('media_url_3', 3, 3, 'Image'),
('media_url_4', 4, 4, 'Video'),
('media_url_5', 5, 5, 'Image'),
('media_url_6', 6, 6, 'Video'),
('media_url_7', 7, 7, 'Image'),
('media_url_8', 8, 8, 'Video'),
('media_url_9', 9, 9, 'Image'),
('media_url_10', 10, 10, 'Video');

-- Table comments
INSERT INTO comments (length, followerID, views_viewsID) VALUES
('Comment 1', 'User1', 1),
('Comment 2', 'User2', 2),
('Comment 3', 'User3', 3),
('Comment 4', 'User4', 4),
('Comment 5', 'User5', 5),
('Comment 6', 'User6', 6),
('Comment 7', 'User7', 7),
('Comment 8', 'User8', 8),
('Comment 9', 'User9', 9),
('Comment 10', 'User10', 10);

-- Table statistic
INSERT INTO statistic (comments_amount, views_amount, reactions_amount, user_account_userID) VALUES
(5, 50, 10, 1),
(10, 60, 20, 2),
(7, 55, 15, 3),
(8, 60, 12, 4),
(4, 45, 8, 5),
(6, 70, 14, 6),
(9, 80, 18, 7),
(3, 30, 6, 8),
(2, 20, 4, 9),
(12, 100, 24, 10);

-- Table user_info
INSERT INTO user_info (name, age, gender, user_account_userID) VALUES
('User1', 25, 'M', 1),
('User2', 30, 'F', 2),
('User3', 28, 'M', 3),
('User4', 32, 'F', 4),
('User5', 22, 'M', 5),
('User6', 27, 'F', 6),
('User7', 34, 'M', 7),
('User8', 29, 'F', 8),
('User9', 26, 'M', 9),
('User10', 31, 'F', 10);

-- Table follower
INSERT INTO follower (user_account_userID, user_account_userID1) VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 1);


