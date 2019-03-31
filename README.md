# fossee4
Project for IITB summer Internship Entrance in Open source<br>
Please see the demo video on maximum possible volume with Earphones.<br>

-About the application

It's an application simulating an API for images, where user can use the image by Id.<br>
And the Id will be returned by the API itself.

<b> Setting up the project:</b>

- Clone the repo
``` 
git clone https://github.com/mananpoddar/fossee4
cd fossee4/mysite
```
- Create a virtualenv
```
virtualenv -p python3 venv
source venv/bin/activate
```

- Install the requirements
```
pip install -r requirements.txt
```
- Setup your mysql database and sync it with my project
```
go to fossee4/mysite/mysite/settings.py and in DATABASE array, change the password and 
username to yours.
do python manage.py makemigrations
then, python manage.py migrate
```

- close any libreoffice application running on your system for better experience

- Run the dev server
```
python manage.py runserver
```
- request localhost:8000/fossee4

<br><br>

<b>Important directories and files to make your look up to the code easier:</b>
```
core backend logic - > fossee4/mysite/fossee4/views.py
core frontend logic - > fossee4/mysite/fossee4/static/fossee4/ajax.js
templates(html files) - > fossee4/mysite/fossee4/templates/fossee4/
routing files - > fossee4/mysite/fossee4/urls.py

```
