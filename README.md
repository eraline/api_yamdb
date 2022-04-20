# Yamdb API
API for the Review Service. Authorization was made using the JWT token. 
Users can write reviews on films, music or book, also they can leave comments on any reviews.

This project was made in collaboration with @sproggi and @menyanet73.
My part of this project was to build scoring, reviews and comment sections.
Also I made a huge effort in coordination between the developers, so we went through it smoothly.

#### Stack: 
Python 3, Django 2.2, DRF, PyJWT

## How start project:

Clone a repository and go to command line:

```sh
git clone https://github.com/eraline/api_yamdb.git
```

```sh
cd api_yamdb
```

Create and activate virtual environment:

```sh
python3 -m venv env
```
For Windows:
```sh
source env/Scripts/activate  
```
For Linux:
```sh
source env/bin/activate  
```

Install dependencies from a file requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Apply migrations:


```sh
cd api_yamdb
```

```sh
python3 manage.py migrate
```

Start project:

```sh
python3 manage.py runserver
```

### Documentation of API will be aviable in
```sh
127.0.0.1:8000/redoc/
```
