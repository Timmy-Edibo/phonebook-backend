# phonebook-backend


This is an API for the phonebook backend, a simple application \
that provides endpoint for users to create, delete, updates and \
delete users from the phonebook application.

## How to setup the phonebook backend App

1. Clone the project from github using:
### `git clone https://github.com/Timmy-Edibo/phonebook-backend.git`

2. Create a virtual environment for the phonebook backend using:
### `python3 -m venv venv`

3. Activate  the virtual environment using thsi command:
### `source venv/bin/activate`

4. Install Dependencies and libraries for the project using a requirements.txt \
file contained in the project root directory using this command:

### `pip install -r requirements.txt`

# Setting up Database
This project was created using postgresql, you can also use any SQL database of your choice, but the \ instructions below will guide you through if you're using postgresql


Access the PostgreSQL command line by running the following command in your terminal:
### `psql -U postgres`
This assumes you're logging in as the default postgres user. 
If you're using a different user, replace postgres with the appropriate username.

1. Create a new database using the following command:
### `CREATE DATABASE phonebook;`

2. Create a new database user e.g:
### `CREATE USER admin WITH PASSWORD 'mypassword';`

3. Grant user permission to to manage the database
### `ALTER ROLE admin SET client_encoding TO 'utf8'; `
### `ALTER ROLE admin SET default_transaction_isolation TO 'read committed';`
### `ALTER ROLE admin SET timezone TO 'UTC';`

### `GRANT ALL PRIVILEGES ON DATABASE phonebook TO 'admin';`


# Create a .env file in root directory to store secret credentials
1. Command to create file
### touch .env

2. Use this template below to store secret credentials in file
    DATABASE_NAME=phonebook
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_PORT=5432

    SECRET_KEY=add secret key here
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=60


4. Finally, Run the project in developement mode using the following command:
### `uvicorn app.main:app --reload`
In the project directory, you can run:
