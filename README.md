Task2
-----
1.CREATE DATABASE website;
<img width="939" height="61" alt="image" src="https://github.com/user-attachments/assets/2ec7a58a-42a8-4dff-a1c3-c190c1e1db23" />

2.CREATE TABLE member(id int UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, follower_count int UNSIGNED NOT NULL DEFAULT(0), time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ,PRIMARY KEY(id));
<img width="1937" height="135" alt="image" src="https://github.com/user-attachments/assets/c2362124-ed8c-481a-bd97-5d92003b2c7c" />
<img width="1675" height="415" alt="image" src="https://github.com/user-attachments/assets/36a2177d-8db8-409f-a79b-c857eb11f452" />

Task3
-----
1. INSERT INTO member(name,email, password) VALUES ('test','test@test.com','test');
   
<img width="1403" height="488" alt="image" src="https://github.com/user-attachments/assets/1d5a3dca-2a5c-42f2-a319-17da0fb2f39e" />
3. SELECT *FROM member;
<img width="1609" height="412" alt="image" src="https://github.com/user-attachments/assets/5c968caf-5942-452e-89a6-05c9acbd5372" /> 
4. SELECT *FROM member ORDER BY time DESC;
<img width="1613" height="419" alt="image" src="https://github.com/user-attachments/assets/75c673d3-d001-4f6b-a154-9c73e17fbe6a" />
5. SELECT * FROM member ORDER BY time DESC limit 3;
<img width="1779" height="331" alt="image" src="https://github.com/user-attachments/assets/5fac43dd-7392-4a5b-b5b5-9a019819f9b2" />
6. SELECT * FROM member WHERE email='test@test.com';
<img width="1776" height="260" alt="image" src="https://github.com/user-attachments/assets/ffd671d4-7509-4b76-8259-179c5a39ba20" />
7. SELECT * FROM member WHERE name LIKE '%es%';
<img width="1668" height="270" alt="image" src="https://github.com/user-attachments/assets/f5dcefe6-cf7c-456e-a809-eabfe738d38c" />
8. SELECT * FROM member WHERE email='test@test.com' and password='test';
<img width="2153" height="261" alt="image" src="https://github.com/user-attachments/assets/d7902617-3d50-4f40-8490-2f8b80ce665a" />
9. UPDATE * FROM member WHERE 
UPDATE member SET name = 'test2' WHERE email='test@test.com';
<img width="2009" height="561" alt="image" src="https://github.com/user-attachments/assets/c7381c75-4237-4d90-bb4b-c2e1edfb7c94" />

task4
----
After renewing the follower_count data, the picture below shows the updated chart.
<img width="1612" height="417" alt="image" src="https://github.com/user-attachments/assets/ba775869-3611-461b-bdeb-8227c91ba58d" />
1. SELECT COUNT(*) FROM member;
<img width="1367" height="261" alt="image" src="https://github.com/user-attachments/assets/f3534946-14f9-481c-847f-a92c37a056cd" />
2. SELECT SUM(follower_count) FROM member;
<img width="1577" height="264" alt="image" src="https://github.com/user-attachments/assets/fe2e1120-fad9-453d-b285-2e10bf90581c" />
3. SELECT AVG(follower_count) FROM member;
<img width="1597" height="274" alt="image" src="https://github.com/user-attachments/assets/64ea5eeb-6e25-437e-bf4f-161c682c3116" />
4. SELECT AVG(follower_count) FROM( SELECT follower_count FROM member ORDER BY follower_count DESC limit 2) AS top2_avg;
<img width="2287" height="299" alt="image" src="https://github.com/user-attachments/assets/8df44d95-36a3-4de3-a6ec-59042284fb9a" />

task5
-----
1. CREATE TABLE message (id INT UNSIGNED NOT NULL AUTO_INCREMENT, member_id INT UNSIGNED NOT NULL, content VARCHAR(65535) NOT NULL, like_count INT UNSIGNED NOT NULL DEFAULT 0, time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id), FOREIGN KEY (member_id) REFERENCES member(id));
<img width="2319" height="566" alt="image" src="https://github.com/user-attachments/assets/046fede8-79dc-4c46-a00c-7469b4028f6e" />
2.SELECT message.id, member.name, message.member_id, message.content, message.like_count, message.time From member Inner Join message on message.member_id = member.id;
<img width="2831" height="482" alt="image" src="https://github.com/user-attachments/assets/00de2ba1-9a03-46e4-81ea-935624a1c1d6" />
3. SELECT message.id, member.name, message.member_id, message.content, message.like_count, message.time From member Inner Join message on message.member_id = member.id WHERE member.email = 'test@test.com';
<img width="2836" height="301" alt="image" src="https://github.com/user-attachments/assets/802cb1c5-dde7-4b5f-a628-c6e28a479751" />
4. SELECT AVG(message.like_count) FROM member INNER JOIN message ON member.id = message.member_id WHERE member.email = 'test@test.com';
<img width="2836" height="303" alt="image" src="https://github.com/user-attachments/assets/f11cc6ec-64cd-4597-9a25-8d16480eec8d" />
5. SELECT member.email, AVG(message.like_count) FROM member INNER JOIN message ON member.id = message.member_id GROUP BY member.email;
<img width="2841" height="453" alt="image" src="https://github.com/user-attachments/assets/418f516c-f6ad-47b6-9e64-e75f9d087a27" />

