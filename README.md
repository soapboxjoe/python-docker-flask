# Flask application using a Docker container as dev env
Run your development environment in a docker container using docker compose

## How to run ##

````
$ docker-compose build
$ docker-compose up
````

Now navigate to http://localhost:5000

Auto-reload is enabled but when adding new dependancies you need to do the following:

* Stop the running container
* run the command

````
$ pipenv shell
$ pipenv install [package]
$ docker-compose build
````
