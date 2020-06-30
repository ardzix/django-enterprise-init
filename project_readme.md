# Requirements
- Python 3.6 or above
- PostgreSQL
- NginX

# Installation

- Go to specified directory which the app will be installed
- Create virtual environment for your python

`python3 -m venv venv` or `virtualenv venv`

- Clone the project from repository

`git clone https://bitbucket.org/bridce/mat-padi.git`

- Go to project directory

`cd padi.bri.co.id`

- Create file *local_settings.py* based on *default_local_settings.py* inside dashboard directory

`cp project/default_local_settings.py project/local_settings.py`

- Activate yout virtual environment

`source ../venv/bin/activate`

- Install the dependencies

`pip install -r requirements.txt`




# Environment variable (on local_settings.py)

```python
# Environment
DEBUG = False
PRODUCTION = True
NEWS_ENABLED = False
SECRET_KEY = 'on&m%*l23jfofv0djvdkwifada9hiacu*(4'

ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'padi_db',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'padi_db_test'
        }
    }
}

USE_RACKSPACE = False

AUTH_USER_MODEL = 'authentication.User'

SITE_ID = 1

BASE_URL = "http://127.0.0.1:8000/"

IS_CELERY = False

PADI_URL = 'https://api.thebigbox.id/padi-umkm/1.0.0/padis'
PADI_KEY = 'yJBUTJ31ER6z2dDW6CFGSzr4MhNCNKHu'

```

# Preparation

- Check your project

`./manage.py check`


- Make migrations

`./manage.py makemigrations`

- Migrate

`./manage.py migrate`

- Create superuser

`./manage.py createsuperuser`

- Check the server again

`./manage.py check`

# Configure uWSGI

- Create a directory with uWSGI configuration files:
`sudo mkdir -p /etc/uwsgi/sites`

- Create configuration file `sample.ini` with the following contents:
```
[uwsgi]
project = sample
base = /home/django

chdir = %(base)/%(project)
home = %(base)/Env/%(project)
module = %(project).wsgi:application

master = true
processes = 2

socket = %(base)/%(project)/%(project).sock
chmod-socket = 664
vacuum = true
```

- Create an Upstart job for uWSGI:
```
description "uWSGI"
start on runlevel [2345]
stop on runlevel [06]
respawn

env UWSGI=/usr/local/bin/uwsgi
env LOGTO=/var/log/uwsgi.log

exec $UWSGI --master --emperor /etc/uwsgi/sites --die-on-term --uid django --gid www-data --logto $LOGTO
```
This job will start uWSGI in Emperor mode, meaning that it will monitor /etc/uwsgi/sites directory and will spawn instances (vassals) for each configuration file it finds. Whenever a config file is changed, the emperor will automatically restart its vassals.

- Start the uwsgi service:
`sudo service uwsgi start`

# Configure nginx
- Remove the default nginx site configuration:
`sudo rm /etc/nginx/sites-enabled/default`

- Create an nginx site configuration file for your Django application:
```
server {
    listen 80;
    server_name padi.bri.co.id;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/django/sample;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/home/django/sample/sample.sock;
    }
}
```

- Create a symlink to nginx’s sites-enabled directory to enable your site configuration file
`sudo ln -s /etc/nginx/sites-available/sample /etc/nginx/sites-enabled`

- Check nginx’s configuration and restart it:
`sudo service nginx configtest && sudo service nginx restart`

- You should now be able to reach your Django application by visiting your Linode’s hostname or IP address on port 80 in your browser.



__*Regards, Arif Dzikrullah - [ardzix@hotmail.com](mailto:ardzix@hotmail.com)*__