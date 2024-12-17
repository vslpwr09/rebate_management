# Rebate Management
## Installation (Docker)
### Prerequisites

#### 1. Install Docker
Install docker on local machine

#### 2. Clone git repository
```bash
$ git clone "https://github.com/vslpwr09/rebate_management.git"
$ cd rebate_management
```

#### 2. Run docker command
```bash
$ docker compose up
# your server is up on port 8000
```

## Installation(Without docker)

### Prerequisites

#### 1. Install Python
Install ```python-3.11.0``` and ```python-pip```.

#### 2. Clone git repository
```bash
$ git clone "https://github.com/vslpwr09/rebate_management.git"
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
#### Create Rebate Program: [http://localhost:8000/api/v1/rebate-program/](http://localhost:8000/api/v1/rebate-program/)
#### Create Transaction: [http://localhost:8000/api/v1/transaction/](http://localhost:8000/api/v1/transaction/)
#### Calculate Rebate: [http://localhost:8000/api/v1/transaction/calculate-rebate/id](http://localhost:8000/api/v1/transaction/calculate-rebate/<id>)
#### Claim Rebate: [http://localhost:8000/api/v1/rebate/claim/](http://localhost:8000/api/v1/rebate/claim/)
#### Update Claim status: [http://localhost:8000/api/v1/rebate/update/id](http://localhost:8000/api/v1/rebate/update/<id>)
#### Claim Report: [http://localhost:8000/api/v1/reports/claim-report/](http://localhost:8000/api/v1/reports/claim-report/)


