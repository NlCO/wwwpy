# Essai de site web en python avec Django

## Steps / reminders

- warm-up

```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install Django
sudo apt-get install python-virtualenv
```

- implementation & using virtualenv
`virtualenv -p python3 env`

  - activation
  `source env/bin/activate`
  - desactivation 
  `deactivate`

- install project
`django-admin.py startproject project1`

- rajout de django via pip dans l'environnement (!?)

- adding application
`python manage.py startapp app1`
> add it in setting.py file in the variable INSTALLED_APPS 
