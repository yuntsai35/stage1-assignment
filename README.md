Task2
-----
1.CREATE DATABASE website;
<img width="939" height="61" alt="image" src="https://github.com/user-attachments/assets/2ec7a58a-42a8-4dff-a1c3-c190c1e1db23" />
2.CREATE TABLE member(id int UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, follower_count int UNSIGNED NOT NULL DEFAULT(0), time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ,PRIMARY KEY(id));
