# By using OMDB API try to create a custom movie search web application.

Basic IMDB type of website  built in django web framework using Python.
using OMBD API key.


-Install the prerequisites
-Run the server

admin:
root
password:
root

### Prerequisites

You can install the Prerequisites by running the command: 

```
pip install -r requirements.txt
```

```
Django>=3.1.6,<3.2
uWSGI>=2.0.19,<2.1
requests
Pillow>=2.2.1,<2.3
gunicorn

```


# run by docker :


```
sudo docker-compose build 

```

then run project by

```
sudo docker-compose up   

```


#  run by virtual environment

you can run by create any python vertual environment  

then install requirements.txt files library

then after activate env 

run
```
python manage.py runserver

```
