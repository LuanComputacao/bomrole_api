# Bom Rolê

Wow! That was a awesome challenge. I used a lot of time searching technologies to solve the stories and have the best
fit between the framework and the plugins used here.

## List of new knowleges

*  

# Description

# How to run in development

## Serving the application

### Python Virtual Environment
* Check the __requirements__
  * Python __3.7__
  * Python `pip`
  * Python `virtualenv` 
  * linux softwares
    * `gdal-bin`
    * `binutils`
    * `libsqlite3-mod-spatialite`
* Create the virtual environment
    ```shell script
    $ python -m venv venv
    ```
* Load the virtual environment
    ```shell script
    $ source venv/bin/activate
    ```
* Install the packages
    ```shell script
    $ pip install -r requirements.txt
    ```
* Run on your own network
    ```shell script
    $ ./manage.py runserver 0.0.0.0:8000
    ```
### Using docker
* Check the __requirements__
  * Docker
  * Docker Compose
* Run the dev environment
  ```shell script
  $ docker-compose up --build
  ```
