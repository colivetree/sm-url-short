README:

Deployment Instructions
- If unavailable, download & install “pip”: https://pypi.python.org/pypi/pip
- with “pip” in place, install “virtualenv” by going to the terminal / console and doing:
— pip install virtualenv
- create a new virtual environment for the application. In this case, we’re gonna call it “smart_venv”:
— virtualenv smart_venv
- start the virtual environment
— source smart_venv/bin/activate
- you should now be inside the virtual environment. here, install the application’s preretirements:
— pip install -r {{APP_FOLDER}}/conf/requirements.txt
— NOTE: APP_FOLDER should not have blank spaces in the path
- go to {{APP_FOLDER}} and run: 
— python manage.py syncdb
- to run the server, now run:
— python manage.py runserver 0.0.0.0:8080


Front-End at:
http://localhost:8080/smart_fe
API at:
http://localhost:8080/api/v1/

Worth Mentioning:
- Missing security checks, data validations & performance considerations
- Missing comments and tests
- using sqlite db for easier setup
- apps are all in the same project for readability and testability (NOT RECOMMENDED FOR PRODUCTION CODE - SPLIT APPS FOR HIGHER DECOUPLING):
— url_short_api contains API code
— smart_url_api has setup code
— smart_shortener_fe contains frontend code

- API and Front-End consider that server is launched on 8080 & local_machine
— see settings.py “CURRENT_BASE_URL”

- no beautification on front-end