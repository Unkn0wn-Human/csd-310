DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('3425 52nd street, Miami Florida, 12345');



INSERT INTO book(book_name, author, details)
    VALUES('Pride and Prejudice', 'Pride and Prejudice', 'the courtship of two opposed characters in a world where manners and courtesy are of the utmost importance.');

INSERT INTO book(book_name, author, details)
    VALUES('The Book Thief', 'Markus Zusak', 'Liesel rescues books from the tyranny of Nazi rule.');

INSERT INTO book(book_name, author, details)
    VALUES('The Hobbit', 'The Hobbit', 'Bilbo Baggins traverses the harsh landscapes of Middle Earth to challenge a dragon');

INSERT INTO book(book_name, author, details)
    VALUES('Fahrenheit 451', 'Fahrenheit 451', 'Books are forbidden and burned');

INSERT INTO book(book_name, author, details)
    VALUES('The Catcher in the Rye', 'J.D. Salinger', 'the challenges and isolation of adolescence.');

INSERT INTO book(book_name, author, details)
    VALUES("Lord of the Flies", 'Lord of the Flies', ' follows the lives of boys marooned on an island');

INSERT INTO book(book_name, author, details)
    VALUES('A Tale of Two Cities', 'Charles Dickens', 'eighteen years as a political prisoner, Dr Manette is released and returns to England');

INSERT INTO book(book_name, author, details)
    VALUES('Wuthering Heights', 'Emily Bronte', 'Catherine Earnshaw and her father’s adopted foundling Heathcliff as they grow into very different adults.');

INSERT INTO book(book_name, author, details)
    VALUES('The Color Purple', 'Alice Walker', 'a devastating tale that tackles the lives of colored women in 1930s USA');




INSERT INTO user(first_name, last_name) 
    VALUES('Isaac', 'Krass');

INSERT INTO user(first_name, last_name)
    VALUES('Joe', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('Ivan', 'King');




INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Isaac'), 
        (SELECT book_id FROM book WHERE book_name = 'The Book Thief')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Joe'),
        (SELECT book_id FROM book WHERE book_name = 'The Hobbit')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ivan'),
        (SELECT book_id FROM book WHERE book_name = 'Wuthering Heights')
    );