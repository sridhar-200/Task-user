# Task Instruction

A user management system developed by **Sridhar**. This project provides a basic setup for user authentication, including login, registration, and other user-related functionalities.

---

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x** (preferably the latest version)
- **pip** (comes with Python 3)
- **Virtualenv** (recommended for creating isolated environments)

### Optional

- **Git** (if you are cloning from a repository)

## Installation and Setup

### Step 1: Clone the Repository

Clone the repository to your local machine. Replace `your-repo-url` with the actual URL of your repository:

```bash
git clone https://github.com/sridhar-200/usermanagement.git
cd usermanagement

### Step 2: venv env
python -m venv env

env\Scripts\activate


### Step 3: install the requirements

pip install -r requirements.txt

### Step 4: makemigrations


python manage.py makemigrations
python manage.py migrate

### Step 5: after complete previous step run using this comment

python manage.py runserver

python manage.py test


# if not working
pip install --upgrade pip
pip install -r requirements.txt


# Post API ENDPOINT

http://127.0.0.1:8000/api/users/


# body data
   {

        "email": "123@gmail.com",
        "password": "*****",
        "first_name": "John",
        "last_name": "Doe"
    }


-------------------------------------------------------------------------------------------------------------------------------------------


# GET API ENDPOINt

http://localhost:8000/api/users/

# Response
[
    {
        "id": 1,
        "email": "123@gmail.com",
        "first_name": "John",
        "last_name": "Doe"
    }
]


---------------------------------------------------------------------------------------------------------------------------------------------------------
# DETETE API ENDPOINT

http://localhost:8000/api/users/1/

Authorization  :   Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMTcyNDY0LCJpYXQiOjE3MzAxNzIxNjQsImp0aSI6IjNiMWM2NDdkN2RiMjRhNzE4MjI0NDdhMzA2NjY0MWFiIiwidXNlcl9pZCI6Mn0.E56S6zXMlOJVmMf5-8YAGZ2Sxd96zpjBRt8OF_M4IQQ


------------------------------------------------------------------------------------------------------------------------------------------------------

# UPDATE API ENDPOINT PUT

http://localhost:8000/api/users/1/

Authorization  :   Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMTcyNDY0LCJpYXQiOjE3MzAxNzIxNjQsImp0aSI6IjNiMWM2NDdkN2RiMjRhNzE4MjI0NDdhMzA2NjY0MWFiIiwidXNlcl9pZCI6Mn0.E56S6zXMlOJVmMf5-8YAGZ2Sxd96zpjBRt8OF_M4IQQ


# ENPOINT FOR DOWNLOAD CSV FILE 

http://127.0.0.1:8000/api/users/export/csv/

# ENPOINT FOR DOWNLOAD PDF FILE 

http://127.0.0.1:8000/api/users/export/pdf/



PIhttp://127.0.0.1:8000/api/users/export/pdf/


# TOKEN API (exp in 1 day)

http://127.0.0.1:8000/api/token/

# REFERESH  TOKEN API 


http://127.0.0.1:8000/api/token/refresh/

```
