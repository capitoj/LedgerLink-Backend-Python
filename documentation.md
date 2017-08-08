# Overview

This is a sample project demonstrating the use of the UC Dashboard app,
a Django project to quickly develop dashboards. There is a lot to know, and
this documentation is a work in progress.

## Pycharm

You need Pycharm to run this example, and you need to set up a Virtual
Environment with a couple of items configured, including Django 1.9.

# About UC Dashboards

### Standard pages
Standard (minimum) recommended set of pages:
* Welcome (slug: welcome) – this is the page that people will see when
they are not logged on.
* Overview (slug: overview) – this is the page that the logon will redirect
to after logging on.
* About: (slug: about) – the standard about page to be used for your project

# Perspectives [NEW]
A perspective is a group of pages (dashboards). A perspective has a code, 
which is used to define preset filters. Preset filters are useful to pre-assign
filters to either individual user accounts, or user groups. This enables
a dashboard always see a dashboard for a particular country or district.

## Filters
Perspectives have a code, and this code is used to pre-assign filters. When a
user loads a perspecive, the system loads the pages that are part of the perspective. 
The system will then load the preset filters for the user, by first going
through the filters assigned to the group(s) the user is a part of, and
then the user account.

Currently, only one filter can be set per user, and user account filters
override group filters. Filters for multiple dashboards can be set for
a user and/or a group. For example:

national:'country=uganda'
district:'district=jinja'

When the user loads the National perspective, the filter country=uganda will
automatically be appended to the querystring of widgets. When the user
selects the District perspective, the district=jinja filter will be
applied. Note that _national_ and _district_ here are the codes of the
perspectives.

It is also possible to use a * as a district code, this means that
the filter will be applied to all perspectives for that user or group.


## Filters and the querystring
Note that when filters are preset, they do not show in the querystring,
but they are automatically applied to any widgets. The user cannot undo this,
but if a filterbar is available the user may be override the preset
filter if the filterbar provides an option for that filter.

## Python 3
Installing Python 3:
http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/

We are moving there soon

## Django 1.11








