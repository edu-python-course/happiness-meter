###############################################################################
                                Happiness Meter
###############################################################################

Happiness Meter is a Django RestFul application designed to monitor
the happiness levels of teams and team members. It allows users to
create, retrieve, update, and delete teams and members, as well as
manage teams and members through the admin panel. Members can set
their daily happiness level, and they can be connected or disconnected
from any available team. The application provides statistics on team member
happiness and calculates the average happiness for all teams.

Getting started
===============

#.  Clone this repository to your local machine.
#.  Create a virtual environment (optionally, but recommended).
#.  Install the dependencies.
    This repository comes with dependencies suitable both for `pip`_ and
    `poetry`_ package managers.

    -   To install dependencies via ``pip`` do:

        .. code-block::

            pip install -r requirements.txt

    -   To install dependencies via ``poetry`` do:

        .. code-block::

            poetry install

.. _pip: https://pip.pypa.io/
.. _poetry: https://python-poetry.org/

Using Docker Compose
====================

Prerequisites:

-   docker compose installed

This project comes with a docker compose file to deploy services recommended
for the Django training. If you are not familiar with docker compose, it is
a tool for containers management
(`Would you like to know more? <https://docs.docker.com/compose/>`_).

The installation process is described
`here <https://docs.docker.com/compose/install/>`_.

The compose file defines a minimalistic set of database server and GUI client
running in individual containers. You need to map ports from your machine to
docker containers to get things working well. Default mapped ports are:

* 5432 for the ``postgres`` service
* 5050 for the ``pgadmin`` service
* 8080 for the ``static`` service

You can change these values by modifying environment variables.

The containers management is simple as:

.. code-block::

    docker compose up -d  # start all containers
    docker compose down   # stop all containers

Setting up env variables
------------------------

Some settings declared in the compose file may be overriden by setting up
environment variables. If you aren't familiar with them
[here](https://en.wikipedia.org/wiki/Environment_variable) is a Wiki article.

Just type to the terminal:

.. code-block::

    SET VARIABLE=value     # for Windows users
    EXPORT VARIABLE=value  # for Unix users (Linux and MacOS)

PostgreSQL
----------

The ``db`` service will run the PostgreSQL server container.
It exposes 5432-port to the host machine, so you can use it just as if you
got postgres running on your own system.
The default ports mapping is "5432:5432". In case you have already 5432-port
occupied by other software, you may set up any available port by using
``POSTGRES_PORT`` environment variable.

The pre-defined credentials are:

+----------+----------+
| Option   | Value    |
+==========+==========+
| username | postgres |
+----------+----------+
| password | postgres |
+----------+----------+


You can run this service separately from other services defined in the compose
file by:

.. code-block::

    docker compose up -d db

pgAdmin
-------

pgAdmin is one of the most famous PostgreSQL clients. From the version 4.x it
uses a web-based UI running in your web browser. The pgAdmin container exposes
its 80-port to the host machine. By default, this port is mapped to 5050. In
case you have already 5050-port occupied by other software, you may set up any
available port by using ``PGADMIN_PORT`` environment variable. After running
the pgAdmin visit http://localhost:5050 in your web browser (adjust the port
number if needed).

The pre-defined credentials to connect pgAdmin are:

+----------+-------------------------------+
| Option   | Value                         |
+==========+===============================+
| email    | pgadmin@edu-python-course.org |
+----------+-------------------------------+
| password | pgadmin                       |
+----------+-------------------------------+

While connecting to the PostgreSQL server via pgAdmin the alias for the db
container is "postgresql-server". This connection is already defined in the
"servers.json" file under the "docker" directory and there is no need to it
connect manually.

Note this may take some time to set up container and run internal server.

Nginx
-----

Nginx (pronounced "engine-x") is a popular open-source web server and reverse
proxy server. It is designed to handle high concurrency, provide fast and
efficient delivery of web content, and offer various features for web
application deployment and performance optimization.

This container has been added to serve any static file via HTTP and simulate
production environment. The container exposes its 80-port to the host machine.
By default, this port is mapped to 8000. In case you have already 8000-port
occupied by other software, you may set up any available port by using
``STATIC_PORT`` environment variable.

Local storage for static files is "static" directory. Place your content to
it, and it will appear available at http://localhost:8080/path/to/file.
This directory can be used as ``STATIC_ROOT`` setting during development:

.. code-block::

    STATIC_ROOT = BASE_DIR / "static"

You can run this service separately from other services defined in the compose
file by:

.. code-block::

    docker compose up -d static

After running the container visit http://localhost:8080 in your web browser
(adjust the port number if needed).
