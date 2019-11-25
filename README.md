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

# Atom packages
*  atom-beautify@0.33.4
*  file-icons@2.1.36
*  highlight-selected@0.16.0
*  kite@0.175.0
*  language-docker@1.1.8
*  language-gherkin@1.0.4
*  language-groovy@0.7.0
*  markdown-preview-plus@3.11.5
*  minimap@4.29.9
*  minimap-highlight-selected@4.6.1
*  minimap-lens@0.3.0
*  platformio-ide-terminal@2.10.0
*  python-tools@0.6.9
*  script@3.25.0
*  split-diff@1.6.1
