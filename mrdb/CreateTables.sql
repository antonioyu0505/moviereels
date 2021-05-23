-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-05-22 22:18:52.949

-- tables
-- Table: Movie
CREATE TABLE Movie (
    id int NOT NULL AUTO_INCREMENT,
    type varchar(10) NOT NULL,
    tag varchar(15) NOT NULL,
    typeId int NOT NULL,
    UNIQUE INDEX unique_typeId (typeId),
    CONSTRAINT Movie_pk PRIMARY KEY (id)
);

-- Table: User
CREATE TABLE User (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    password tinytext NOT NULL,
    countryCode varchar(6) NOT NULL,
    lastLogin timestamp NOT NULL,
    UNIQUE INDEX unique_username (username),
    CONSTRAINT User_pk PRIMARY KEY (id)
);

-- Table: UserList
CREATE TABLE UserList (
    id int NOT NULL AUTO_INCREMENT,
    userId int NOT NULL,
    movieId int NOT NULL,
    CONSTRAINT UserList_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: UserList_Movie (table: UserList)
ALTER TABLE UserList ADD CONSTRAINT UserList_Movie FOREIGN KEY UserList_Movie (movieId)
    REFERENCES Movie (id);

-- Reference: UserList_User (table: UserList)
ALTER TABLE UserList ADD CONSTRAINT UserList_User FOREIGN KEY UserList_User (userId)
    REFERENCES User (id);

-- End of file.
