# Task manager
[![Build Status](https://travis-ci.org/Lelikov/python-project-lvl4.svg?branch=master)](https://travis-ci.org/Lelikov/python-project-lvl4)
[![Maintainability](https://api.codeclimate.com/v1/badges/4bd002caabd84f2327dd/maintainability)](https://codeclimate.com/github/Lelikov/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4bd002caabd84f2327dd/test_coverage)](https://codeclimate.com/github/Lelikov/python-project-lvl4/test_coverage)

This app is simple task manager.

You can watch it at work here:
https://task-manager-hexlet-lvl4.herokuapp.com/

For use localy:
``` 
https://github.com/Lelikov/python-project-lvl4.git
```
Use should rename file .env.example to .env and added value of variable environments
```
DATABASE_URL = !Path to your database!
DEBUG = !'True' if you want to use debug mode!
SECRET_KEY = !Key for Django settings!
POST_SERVER_ITEM_ACCESS_TOKEN = !Token for your rollbar account!
```
After this:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py creatsuperuser
``` 

You can initially set statuses and tags using files `statuses.json` and `tags.json` in a folder `/tasks/fixtures/`

And then:
```
python3 manage.py loaddata statuses.json
python3 manage.py loaddata tags.json
```
For start application:
```
python3 manage.py runserver
```
The application is locally available at [http://127.0.0.1:8000]