PRODUCT UNDER DEVELOPMENT

DEV ENV:
PY 3.6.6
DJANGO 2.2.2

# py -m pip install django 
py -m pip install ven
py -m venv myenv 
myvenv\Scripts\activate
(in wirtual env) py -m pip install django
django-admin.exe startproject MadkaApka .
py manage.py migrate
python manage.py startapp apka
python manage.py makemigrations
python manage.py migrate
