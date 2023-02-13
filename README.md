# Challenge

[![python](https://img.shields.io/badge/python-3.10.6-brightgreen)](https://www.python.org/downloads/release/python-3106)
[![django-restframework](https://img.shields.io/pypi/djversions/djangorestframework)](https://www.django-rest-framework.org/)

API-based application 

See real examples: <url>/cms

## Getting Started

***`NOTE`***: There is already a pre existing VM file that is completely setup and ready to go. If you want to use it then go directly to `Running our Web server > VM File` section below. But if you want to install from scratch then just disregard this note.

Make sure that you update your Ubuntu packages : ```sudo add-apt-repository ppa:ubuntugis/ppa``` and run ```sudo apt-get update```

### Prerequisite
 - Python3
 - PIP3
 - Virtual Envinronment
 - RDS Configured

Check version using ```python3 -V```

## Installation

```bash
sudo apt install python3-pip
sudo apt install python3-venv
sudo apt-get install git
```
Check version Django ```django-admin --version```

Let's create the directory!
```bash
mkdir /challenge
cd /challenge
git clone https://github.com/joydaven/pizza.git
sudo chown -R ubuntu:ubuntu pizza
cd pizza
cp .env_sample .env
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages from this point.
Check python3 version then use it when installing venv below ```python3 --version```
```bash
cd pizza
python3.10.6 -m venv venv
source venv/bin/activate
```
Now for the packages
```bash
pip install -r requirements.txt
```

## Starting a Project for the first time
Your folder project will look like this:
```bash
pizza
+-- apps
¦   +-- api
¦   ¦	+-- migrations
¦   ¦   +-- __init__.py 
¦   ¦   +-- admin.py
¦   ¦   +-- apps.py
¦   ¦   +-- models
¦   ¦   ¦   +-- xxxxxxx.py
¦   ¦   +-- tests.py
¦   ¦   +-- templates
¦   ¦   +-- views
¦   ¦   ¦   +-- xxxxxxx.py
¦   +-- cms
¦   ¦	+-- migrations
¦   ¦   +-- __init__.py 
¦   ¦   +-- admin.py
¦   ¦   +-- apps.py
¦   ¦   +-- models.py
¦   ¦   +-- tests.py
¦   ¦   +-- views.py
+-- pizza
¦   +-- __init__.py
¦   +-- asgi.py
¦   +-- settings_dev.py
¦   +-- settings_prod.py
¦   +-- urls.py
¦   +-- wsgi.py
+-- manage.py
+-- venv
```

# Running our Web server

## Nginx Configuration
Open or download the setup-nginx.sh to get the conf file
```bash
chmod u+x bin/setup-nginx.sh
./bin/setup-nginx.sh
```
check if running: ```sudo nginx -t```

## Run Application Configuration
We have to stop the current cause its pointing to default conf (/etc/supervisor/conf.d)
```bash
sudo chmod u+x /challenge/pizza/bin/run-app.sh
```

## Usage
Using run-app.sh
```bash
/challenge/pizza/bin/run-app.sh
```
Using Gunicorn (make sure venv is activated and you're on it!)
```bash
 . /challenge/pizza/venv/bin/activate && gunicorn --workers 1 --bind 127.0.0.1:8000 pizza.wsgi
```
## References:
 - Python-Django : https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

