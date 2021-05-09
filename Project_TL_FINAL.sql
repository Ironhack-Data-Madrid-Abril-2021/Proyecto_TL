-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema sharks
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sharks
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sharks` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `sharks` ;

-- -----------------------------------------------------
-- Table `sharks`.`attacks_clean`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharks`.`attacks_clean` (
  `Case Number` BIGINT NOT NULL,
  `Date` BIGINT NOT NULL,
  `Year` BIGINT NOT NULL,
  `Type` TEXT NOT NULL,
  `Country` TEXT NOT NULL,
  `Area` TEXT NOT NULL,
  `Location` TEXT NOT NULL,
  `Activity` TEXT NOT NULL,
  `Name` TEXT NOT NULL,
  `Sex` TEXT NOT NULL,
  `Age` INT NOT NULL,
  `Injury` TEXT NOT NULL,
  `Fatal (Y/N)` TEXT NOT NULL,
  `Time` BIGINT NOT NULL,
  `Species` TEXT NOT NULL,
  `Investigator or Source` TEXT NOT NULL,
  `pdf` TEXT NOT NULL,
  `href formula` TEXT NOT NULL,
  `href` TEXT NOT NULL,
  `Case Number.1` TEXT NOT NULL,
  `Case Number.2` TEXT NOT NULL,
  `original order` DOUBLE NOT NULL,
  `Unnamed: 22` TEXT NOT NULL,
  `Unnamed: 23` TEXT NOT NULL,
  `month` TEXT NOT NULL,
  `Clean_Hours` DOUBLE NOT NULL,
  `sessions` TEXT NOT NULL,
  PRIMARY KEY (`Case Number`, `Date`, `Year`, `Type`, `Country`, `Area`, `Location`, `Activity`, `Name`, `Sex`, `Age`, `Injury`, `Fatal (Y/N)`, `Time`, `Species`, `Investigator or Source`, `pdf`, `href formula`, `href`, `Case Number.1`, `Case Number.2`, `original order`, `Unnamed: 22`, `Unnamed: 23`, `month`, `Clean_Hours`, `sessions`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharks`.`Attacks per hour/session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharks`.`Attacks per hour/session` (
  `Fatal (Y/N)` TEXT NOT NULL,
  `Clean_Hours` DOUBLE NOT NULL,
  `sessions` TEXT NOT NULL,
  PRIMARY KEY (`Fatal (Y/N)`, `Clean_Hours`, `sessions`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharks`.`attacks related to sex of victim`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharks`.`attacks related to sex of victim` (
  `Sex` TEXT NOT NULL,
  `Fatal (Y/N)` TEXT NOT NULL,
  PRIMARY KEY (`Sex`, `Fatal (Y/N)`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharks`.`Attacks by species of sharks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharks`.`Attacks by species of sharks` (
  `Fatal (Y/N)` TEXT NOT NULL,
  `Species` TEXT NOT NULL,
  PRIMARY KEY (`Fatal (Y/N)`, `Species`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharks`.`Attacks by country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharks`.`Attacks by country` (
  `Country` TEXT NOT NULL,
  `Fatal (Y/N)` TEXT NOT NULL,
  PRIMARY KEY (`Country`, `Fatal (Y/N)`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `sharks`.`Attack per year`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sharks`.`Attack per year` (
  `Year` BIGINT NOT NULL,
  `Fatal (Y/N)` TEXT NOT NULL,
  PRIMARY KEY (`Year`, `Fatal (Y/N)`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
