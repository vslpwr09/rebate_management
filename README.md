# Rebate Management
## Installation (Local enviroment)

### Prerequisites

#### 1. Install Python
Install ```python-3.11.0``` and ```python-pip```.

#### 2. Clone git repository
```bash
$ git clone "https://github.com/Manisha-Bayya/simple-django-project.git"
$ cd rebate_management
```
#### 3. Setup virtual environment
```bash
Install virtual environment
$ pip install virtualenv
$ python3 -m venv venv
```

#### 4. Install requirements
```bash
$ pip install -r requirements.txt
```

#### 5. Run the server
```bash
# Make migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Run the server
$ python manage.py runserver 0:8000

# your server is up on port 8000
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.

### 6. URLs
#### Create Rebate Program: [http://localhost:8001/signup](http://localhost:8001/signup)
#### Create Transaction: [http://localhost:8001/login](http://localhost:8001/login)
#### Calculate Rebate: [http://localhost:8001/](http://localhost:8001/)
#### Claim Rebate: [http://localhost:8001/country/kenya](http://localhost:8001/country/kenya)
#### Claim Report: [http://localhost:8001/logout](http://localhost:8001/logout)


## Installation (Docker)


