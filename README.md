# email_celery_redis
This code is to send email async via celery.

The code is tested properly for windows, not for linux.
The broker is using Redis, so you need to install redis in advance on your computer.

The basic steps to the code is as follows:

**must use python3.8**

2. create a virtual python environment:
`pip venv -m celery-redis
`
3. activate the environment
`celery-redis/Scripts/activate.bat
`   Next cd to the project directory
4. install the necessary requirements.
`pip install -r requirements.txt
`
5. change the password of your qq email in the settings.py. 
When you activate the smtp in qq, it will give a new password for email

6. input the command to run celery; For windows, we need to use eventlet.
`celery -A celery_redis.celery worker -l info -P eventlet -c 10
` Latter, you will see the info about receiving the task and processing the task in the console.

7. run django web server
`python manage runserver`

8. test email via browser or postman
http://127.0.0.1:8000/email/send-email/
