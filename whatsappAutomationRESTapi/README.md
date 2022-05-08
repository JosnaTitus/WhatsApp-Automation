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

Thank You !!!

1.	MYSQL with “whatsapp_automation” database created.
 ![image](https://user-images.githubusercontent.com/56665824/167295252-140ca4eb-eb0c-4499-a5fb-eff4e74b1bd4.png)

2.	List of tables in “whatsapp_automation” database
 
3.	Running the server and opening on browser with “accounts” list.
 
4.	Implementation of REST APIs – POST method
 
5.	Implementation of REST APIs – GET method
 
6.	Implementation of REST APIs – PUT method
 
7.	Data is inserted into MYSQL.
 
