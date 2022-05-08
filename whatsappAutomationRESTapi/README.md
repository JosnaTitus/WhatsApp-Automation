# WhatsApp-Automation-REST-API

To Run this project, 

> Make Sure django, djangorestframework, mysql & PyMySQL is installed.


> Other wise you can download it using these links - [Django](https://pypi.org/project/Django/), [Django REST FrameWork](https://pypi.org/project/djangorestframework/), [MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04), [PyMySQL](https://pypi.org/project/PyMySQL/).



      1. Create Database naming "whatsapp_automation" in mysql.

      2. Go to [whatsappAutomationRESTapi -> settings.py](whatsappAutomationRESTapi/settings.py)   and Enter your user and password in DATABASES part.

      3. then run following commands:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   python3 manage.py runserver
   ```
      4. After Server is up and running [Click here](http://127.0.0.1:8000/admin).

      5. Login page will appear. Login with Username and Password set while creating super user.

      6. After Login, we can see the tables.

      7. Change URL to [http://127.0.0.1:8000/accounts/](http://127.0.0.1:8000/accounts/) to Create, Update, delete or view the accounts.

For your reference you can use the images given below:

1.	MYSQL with “whatsapp_automation” database created.
 ![image](https://user-images.githubusercontent.com/56665824/167295252-140ca4eb-eb0c-4499-a5fb-eff4e74b1bd4.png)

2.	List of tables in “whatsapp_automation” database
![image](https://user-images.githubusercontent.com/56665824/167295288-47652d7e-0158-4cee-bd44-ddab4a6acc05.png)
 
3.	Running the server and opening on browser with “accounts” list.
 ![image](https://user-images.githubusercontent.com/56665824/167295297-e01d9b00-8b59-4ef5-ae51-62768df83529.png)

4.	Implementation of REST APIs – POST method
 ![image](https://user-images.githubusercontent.com/56665824/167295314-b294fcb0-ca84-488b-85e9-14b9ce8da6c4.png)

5.	Implementation of REST APIs – GET method
 ![image](https://user-images.githubusercontent.com/56665824/167295323-f58e5a4c-b19d-4b2c-83c1-2cd5896d2b27.png)

6.	Implementation of REST APIs – PUT method
 ![image](https://user-images.githubusercontent.com/56665824/167295329-73af4900-ad73-476a-a4f2-6d8c5002e087.png)

7.	Data is inserted into MYSQL.
 ![image](https://user-images.githubusercontent.com/56665824/167295341-65711825-168f-4964-8e01-f233aa0fb343.png)

Thank you!
