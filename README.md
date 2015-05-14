## Setup

This based off of the tutorial from the website [miguelgrinberg.com](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)


After you clone the repository change into the directory and create a virtual env
```
$ virtualenv flask
```
If you choose a name other than flask make sure that you update run.py, After you create the virtualenv 
you can start downloading python packages with pip
```
$ flask/bin/pip install flask
$ flask/bin/pip install flask-login
$ flask/bin/pip install flask-openid
$ flask/bin/pip install flask-mail
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-wtf
$ flask/bin/pip install flask-babel
$ flask/bin/pip install guess_language
$ flask/bin/pip install flipflop
$ flask/bin/pip install coverage
```
After that you should be able to get the development server running by runnning run.py
```
$ ./run.py
```
