###############################################################################
                                Happiness Meter
###############################################################################

The Happiness Application is a Django RestFul application designed to monitor
the happiness levels of teams and team members. It allows users to join teams
or leave team they are already members. Also, it provides a functionality to
report **happiness level** once per day for each user. These datas are used
to gather the statistics on an average **happiness level** for all teams, per
team or per a single user.

***********************
Functional requirements
***********************

Team membership
===============

A ``team`` is considered a container for its members. A member is a common user
assigned to a team. In case users aren't assigned to any team they are ``none``
team members. Each user can be assigned to one team at a time.

Authentication actions
======================

-   Anonymous users can register a new account or log into the existing one.
-   Authenticated users can log out from their accounts.
-   Authenticated users can delete their accounts.
    This action shouldn't remove the database records, instead it would just
    mark accounts as deactivated. This action can be undone via admin site.

Teams management
================

-   Only admin users can create, update or delete teams.
    Both API endpoint(s) and admin site can be used for this.
-   Authenticated users can retrieve an average happiness level for a team
    they are assigned to for a current date.
-   Authenticated users can retrieve statistics for
-   Anonymous users or none-team members can retrieve an average happiness
    level for all registered teams.

Happiness levels
================

Happiness level is an integer number from 1 to 10 inclusively.

-   Happiness level cannot be reported, modified or deleted via admin site.
-   An average happiness level (general or per team) is calculated for
    the current date.
-   Only active team members' reports are used to calculate current average
    happiness value.
-   Authenticated users can report their happiness level once per day via
    API endpoint. There are no limits for endpoint interactions per user,
    but the only latest one reported value is stored.
-   Team members can retrieve an average happiness level per their team.
-   Authenticated and unauthenticated users can get an average happiness level
    per all teams.

************
UML diagrams
************

Data models
===========

-   User has ``0+`` reports. But a report entity always has its reporter.
-   Team can store ``0+`` users. A user is a member of a single team or none
    team.

.. mermaid:: ./models.md
    :align: center
