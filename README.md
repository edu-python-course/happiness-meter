# DJANGO PROJECT TEMPLATE

DISCLAIMER: this repository will help you to set up your environment for the
development, but you definitely should be able to do it yourself.

This repository's purpose is to help newcomers to get their first Django
project ready for the development as soon as possible. It has some minimalistic
dependencies and git ignore rules defined.

## Repository Creation

The main document is here:
[ref](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

In short, hit "Use this template" button and select "Create a new repository"
option. This will create your own repository using this template. After that,
you're free to do whatever you want with your OWN repository.

## Setting Up Virtual Environment

Virtual environment
: A cooperatively isolated runtime environment that allows Python users and
applications to install and upgrade Python distribution packages without
interfering with the behaviour of other Python applications running on
the same system.

The easiest way to start using virtual environments - is to use the built-in
[venv](https://docs.python.org/3/library/venv.html) library.

To create a new virtual environment just pass the path you want to place env
into to the `venv` package from the standard library.

```shell
python -m venv ${ENVIRONMENT_NAME}
```

This will create a new environment ready to use with your project. To activate
it do:

```shell
source ${ENVIRONMENT_NAME}/bin/activate  # if you are on MacOS or Linux
${ENVIRONMENT_NAME}\Scripts\activate     # if you are using Windows
```

To deactivate just type `deactivate` command to your terminal and hit Enter.

## Installing Dependencies

```shell
pip install -r requirements.txt
```

This project comes with a minimal list of dependencies. You can easily install
them using the command above. Here is some detail information on the deps list:

| Package         | Version | Package homepage           |
|:----------------|:-------:|:---------------------------|
| Django          |  4.2.3  | https://djangoproject.com/ |
| psycopg2-binary |  2.9.6  | https://www.psycopg.org/   |

Django
: Django is a high-level Python web framework that encourages rapid development
and clean, pragmatic design. Built by experienced developers, it takes care of
much of the hassle of web development, so you can focus on writing your app
without needing to reinvent the wheel. It’s free and open source.

psycopg
: Psycopg is the most popular PostgreSQL adapter for the Python programming
language. Its core is a complete implementation of the Python DB API 2.0
specifications. Several extensions allow access to many of the features
offered by PostgreSQL. `psycopg2-binary` is meant for beginners to start
playing with Python and postgres without need to meet build requirements
for `psycopg2` package. However, you should not use it on production. But it
will suit the training  project needs.

## Starting Django Project

```shell
django-admin startproject ${PROJECT_NAME} /path/to/project/root/directory
```

## Connecting Django to the PostgreSQL Server

Make sure you have postgres server running and available over your network.
Adjust **settings.py** module to set postgres as your default database backend.
Note, that you need to have `psycopg2` package installed in your environment to
use PostgreSQL as a database backend.

Adjust the actual value to meet your database setup.

```python
DATABASE = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "DATABASE_NAME",  # e.g. "ecommerce", "blog_site", "taskboard"
        "HOST": "POSTGRESQL_HOST",  # e.g. "localhost", "postgresql.server.com"
        "PORT": "POSTGRESQL_PORT",  # e.g. "5432", 12345
        "USER": "POSTGRESQL_USER",  # e.g. "johndoe", "foobar"
        "PASSWORD": "POSTGRESQL_PASSWORD",  # e.g. "123456", "qwerty"
    }
}
```

## Using Docker Compose

Prerequisites:

* docker compose installed

This project comes with a docker compose file to deploy services recommended
for the Django training. If you are not familiar with docker compose, it is
a tool for containers management
([Would you like to know more?](https://docs.docker.com/compose/)).

The installation process is described
[here](https://docs.docker.com/compose/install/).

The compose file defines a minimalistic set of database server and GUI client
running in individual containers. You need to map ports from your machine to
docker containers to get things working well. Default mapped ports are:

* 5432 for the `postgres` service
* 5050 for the `pgadmin` service
* 8080 for the `static` service

You can change these values by modifying environment variables.

The containers management is simple as:

```shell
docker compose up -d  # start all containers
docker compose down   # stop all containers
```

### Setting up env variables

Some settings declared in the compose file may be overriden by setting up
environment variables. If you aren't familiar with them
[here](https://en.wikipedia.org/wiki/Environment_variable) is a Wiki article.

Just type to the terminal:

```shell
SET VARIABLE=value     # for Windows users
EXPORT VARIABLE=value  # for Unix users (Linux and MacOS)
```

### PostgreSQL

The `db` service will run the PostgreSQL server container. It exposes 5432-port
to the host machine, so you can use it just as if you got postgres running on
your own system. The default ports mapping is "5432:5432". In case you have
already 5432-port occupied by other software, you may set up any available port
by using `POSTGRES_PORT` environment variable.

The pre-defined credentials are:

| Option   | Value    |
|:---------|:---------|
| username | postgres |
| password | postgres |

You can run this service separately from other services defined in the compose
file by:

```shell
docker compose up -d db
```

### pgAdmin

pgAdmin is one of the most famous PostgreSQL clients. From the version 4.x it
uses a web-based UI running in your web browser. The pgAdmin container exposes
its 80-port to the host machine. By default, this port is mapped to 5050. In
case you have already 5050-port occupied by other software, you may set up any
available port by using `PGADMIN_PORT` environment variable. After running
the pgAdmin visit http://localhost:5050 in your web browser (adjust the port
number if needed).

The pre-defined credentials to connect pgAdmin are:

| Option   | Value                         |
|:---------|:------------------------------|
| email    | pgadmin@edu-python-course.org |
| password | pgadmin                       | 

While connecting to the PostgreSQL server via pgAdmin the alias for the db
container is "postgresql-server". This connection is already defined in the
"servers.json" file under the "docker" directory and there is no need to it
connect manually.

Note this may take some time to set up container and run internal server.

### Nginx

Nginx (pronounced "engine-x") is a popular open-source web server and reverse
proxy server. It is designed to handle high concurrency, provide fast and
efficient delivery of web content, and offer various features for web
application deployment and performance optimization.

This container has been added to serve any static file via HTTP and simulate
production environment. The container exposes its 80-port to the host machine.
By default, this port is mapped to 8000. In case you have already 8000-port
occupied by other software, you may set up any available port by using
`STATIC_PORT` environment variable.

Local storage for static files is "static" directory. Place your content to
it, and it will appear available at http://localhost:8080/path/to/file.
This directory can be used as `STATIC_ROOT` setting during development:

```python
# noinspection PyUnresolvedReferences
STATIC_ROOT = BASE_DIR / "static"
```

You can run this service separately from other services defined in the compose
file by:

```shell
docker compose up -d static
```

After running the container visit http://localhost:8080 in your web browser
(adjust the port number if needed).

## Check Lists

So far and don't know how to start? Here's a simple checklist to help you with
your first step with learning Django framework.

### Project set up

- [ ] Create local virtual environment
- [ ] Install base dependencies from the requirements file or manually
- [ ] Start new Django project
- [ ] Update README file with the information relevant for your project

### Delivering feature into the code base

- [ ] Switch to a newly created branch
- [ ] Do the things...
- [ ] Push working branch to the remote repository
- [ ] Create pull request to merge new feature into the trunk
- [ ] Wait for PR approve
- [ ] Merge it
