tweeter3
=======
Adapted from https://github.com/nnja/tweeter3

Tweeter3 is a basic example Django application that uses [Django Rest Framework](https://github.com/encode/django-rest-framework)


## Installation Instructions

1. In the project's directory, create a new virtual environment using Python 3.7 and activate it.

    On Windows:
     ```shell
    $ py -m venv env
    $ env\Scripts\activate
    ```
    On MacOs/Linux:
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
    
1. Install dependencies from requirements.txt:
    On MacOs/Linux:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
1. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```
1. *(Optionally)* load sample fixtures that will populate the database with a handful of users and tweeters.

    **Note:** If fixtures are loaded, a sample user named 'Bob' will always be logged in by default.
    ```shell
    (env)$ python manage.py loaddata initial_data
    ```
1. Run the local server via:
    ```shell
    (env)$ python manage.py runserver
    ```

### Done!
The local application will be available at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>, and the browsable api will be available at <a href="http://localhost:8000/api" target="_blank">http://localhost:8000/api</a>

