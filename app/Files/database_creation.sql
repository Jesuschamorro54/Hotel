-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `hotel` ;

-- -----------------------------------------------------
-- Table `hotel`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL DEFAULT NULL,
  `email` VARCHAR(70) NULL DEFAULT NULL,
  `password` VARCHAR(50) NULL DEFAULT NULL,
  `image` TEXT NULL DEFAULT NULL,
  `fuente` ENUM('facebook', 'google') NULL DEFAULT NULL,
  `rol` ENUM('free', 'moderador', 'admin') NULL DEFAULT NULL,
  `city` VARCHAR(100) NULL DEFAULT NULL,
  `state` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`rooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`rooms` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numero` VARCHAR(10) NULL DEFAULT NULL,
  `descriptions` TEXT NULL DEFAULT NULL,
  `calification` FLOAT NULL DEFAULT NULL,
  `image` TEXT NULL DEFAULT NULL,
  `state` INT NULL DEFAULT NULL,
  `enabled` INT NULL DEFAULT NULL,
  `price` DOUBLE NULL DEFAULT NULL,
  `date_create` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `room_id` INT NULL DEFAULT NULL,
  `descriptions` TEXT NULL DEFAULT NULL,
  `likes` INT NULL DEFAULT NULL,
  `state` INT NULL DEFAULT NULL,
  `fecha` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id` (`user_id` ASC) VISIBLE,
  INDEX `room_id` (`room_id` ASC) VISIBLE,
  CONSTRAINT `comments_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `hotel`.`users` (`id`),
  CONSTRAINT `comments_ibfk_2`
    FOREIGN KEY (`room_id`)
    REFERENCES `hotel`.`rooms` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `reservation` INT NULL DEFAULT NULL,
  `referencia` VARCHAR(100) NULL DEFAULT NULL,
  `valor` DOUBLE NULL DEFAULT NULL,
  `request` DATETIME NULL DEFAULT NULL,
  `expiration` DATETIME NULL DEFAULT NULL,
  `state` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id` (`user_id` ASC) VISIBLE,
  INDEX `reservation` (`reservation` ASC) VISIBLE,
  CONSTRAINT `payments_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `hotel`.`users` (`id`),
  CONSTRAINT `payments_ibfk_2`
    FOREIGN KEY (`reservation`)
    REFERENCES `hotel`.`rooms` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `hotel`.`reservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`reservas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `room_id` INT NULL DEFAULT NULL,
  `descriptions` TEXT NULL DEFAULT NULL,
  `solicitado` DATETIME NULL DEFAULT NULL,
  `date_inicio` DATETIME NULL DEFAULT NULL,
  `date_final` DATETIME NULL DEFAULT NULL,
  `state` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id` (`user_id` ASC) VISIBLE,
  INDEX `room_id` (`room_id` ASC) VISIBLE,
  CONSTRAINT `reservas_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `hotel`.`users` (`id`),
  CONSTRAINT `reservas_ibfk_2`
    FOREIGN KEY (`room_id`)
    REFERENCES `hotel`.`rooms` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;