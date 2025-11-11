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
2. SELECT *FROM member;
<img width="1609" height="412" alt="image" src="https://github.com/user-attachments/assets/5c968caf-5942-452e-89a6-05c9acbd5372" /> 
3. SELECT *FROM member ORDER BY time DESC;
<img width="1613" height="419" alt="image" src="https://github.com/user-attachments/assets/75c673d3-d001-4f6b-a154-9c73e17fbe6a" />
4. SELECT * FROM member ORDER BY time DESC limit 3;
<img width="1779" height="331" alt="image" src="https://github.com/user-attachments/assets/5fac43dd-7392-4a5b-b5b5-9a019819f9b2" />
5. SELECT * FROM member WHERE email='test@test.com';
<img width="1776" height="260" alt="image" src="https://github.com/user-attachments/assets/ffd671d4-7509-4b76-8259-179c5a39ba20" />
6. SELECT * FROM member WHERE name LIKE '%es%';
<img width="1668" height="270" alt="image" src="https://github.com/user-attachments/assets/f5dcefe6-cf7c-456e-a809-eabfe738d38c" />
8. SELECT * FROM member WHERE email='test@test.com' and password='test';
<img width="2153" height="261" alt="image" src="https://github.com/user-attachments/assets/d7902617-3d50-4f40-8490-2f8b80ce665a" />
10. UPDATE * FROM member WHERE 
UPDATE member SET name = 'test2' WHERE email='test@test.com';
<img width="2009" height="561" alt="image" src="https://github.com/user-attachments/assets/c7381c75-4237-4d90-bb4b-c2e1edfb7c94" />

task4
----
After renewing the follower_count data, the picture below shows the updated chart.

