-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema proyectosharks
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyectosharks
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyectosharks` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`table1`
-- -----------------------------------------------------

USE `proyectosharks` ;

-- -----------------------------------------------------
-- Table `proyectosharks`.`shark_clean`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyectosharks`.`shark_clean` (
  `case number` TEXT NULL DEFAULT NULL,
  `date` DATETIME NULL DEFAULT NULL,
  `year` INT NULL DEFAULT NULL,
  `type` TEXT NULL DEFAULT NULL,
  `country` TEXT NULL DEFAULT NULL,
  `area` TEXT NULL DEFAULT NULL,
  `location` TEXT NULL DEFAULT NULL,
  `activity` TEXT NULL DEFAULT NULL,
  `name` TEXT NULL DEFAULT NULL,
  `sex` TEXT NULL DEFAULT NULL,
  `age` INT NULL DEFAULT NULL,
  `injury` TEXT NULL DEFAULT NULL,
  `fatal (y/n)` TEXT NULL DEFAULT NULL,
  `time` TEXT NULL DEFAULT NULL,
  `species` TEXT NULL DEFAULT NULL,
  `investigator or source` TEXT NULL DEFAULT NULL,
  `pdf` TEXT NULL DEFAULT NULL,
  `href formula` TEXT NULL DEFAULT NULL,
  `href` TEXT NULL DEFAULT NULL,
  `case number.1` TEXT NULL DEFAULT NULL,
  `case number.2` TEXT NULL DEFAULT NULL,
  `original order` INT NULL DEFAULT NULL,
  `unnamed: 22` TEXT NULL DEFAULT NULL,
  `unnamed: 23` TEXT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
