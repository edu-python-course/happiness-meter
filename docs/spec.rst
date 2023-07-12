###############################################################################
                                Happiness Meter
###############################################################################

The Happiness Application is a Django RestFul application designed to monitor
the happiness levels of teams and team members. It allows users to join teams
or leave team their are already members. Also it provide a functionality to
report **happiness level** once per day for each user. These datas are used
to gather the statistics on an average **happiness level** for all teams, per
team or per a single user.

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
    mark accounts as deactivated. This action can be undone via admin site
    page.

Teams management
================

-   Only admin users can create, update or delete teams.
    Both API endpoint(s) and admin site page can be used for this.
-   Authenticated users can retrieve an average happiness level for a team
    their are assigned to for a current date.
-   Authenticated users can retrieve statistics for
-   Anonymous users or none-team members can retrieve an average happiness
    level for all registered teams.

Happiness levels
================

Happiness level is an integer number from 1 to 10 inclusively.

-   Happiness level can no be reported, modified or deleted via admin site.
-   Authenticated users can report their happiness level once per day via
    API endpoint. There are no limits for endpoint interactions per user,
    but the only one value per day is saved. In case users try to report
    their happiness level for the second time, the latest one value should
    be stored.
-   Team members can retrieve an average happiness level per their team.
-   Only active team members' reports are used to calculate current average
    happiness value.
