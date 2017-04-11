-- Database name 'EmmeDomotica'
-- Created 11/04/2017

-- Database creation
CREATE DATABASE IF NOT EXISTS EmmeDomotica;
USE EmmeDomotica;

-- Table to store devices
CREATE TABLE IF NOT EXISTS device (
    mac_address VARCHAR(18) NOT NULL,
    descrizione ENUM('led', 'door', 'bulb') NOT NULL,
    status BOOLEAN,
    number_value INT,
    char_value VARCHAR(16),
    PRIMARY KEY (mac_address)
);
