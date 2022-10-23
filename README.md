# Raseel Open Data Platform Theme
![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square)
![KeycloakVersion: 16.1.1](https://img.shields.io/badge/KeycloakVersion-16.1.1-yellowgreen)
![NginxVersion: 1.22.0](https://img.shields.io/badge/NginxVersion-1.22.0-orange)
![PostgresVersion: 14.3](https://img.shields.io/badge/PostgresVersion-14.3-blue)


**Homepage:** <https://dev-opendata.raseel.city>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Meriam Bouaouja | <mbo@softifi.com> |  |
| Hossam Badri | <hbadri@mda.gov.sa> |  |

***
This theme is based on: ckanext-raseel-theme


Requirements
============

This extension is compatible with CKAN 2.7 and higher.

Installation
============

To install ckanext-raseel-theme:

1.  Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2.  Install the package into your virtual environment:

        pip install ckanext-ozwillo_theme

3.  Add `ozwillo_theme` to the `ckan.plugins` setting in your CKAN
    config file (by default the config file is located at
    `/etc/ckan/default/production.ini`).

4.  Restart CKAN. For example if you've deployed CKAN with Apache on
    Ubuntu:

        sudo service apache2 reload

Config Settings
===============

The following configuration variables must be set:

* `ckanext.ozwillo_theme.plugin.ozwillo_url` (eg <https://www.ozwillo-preprod.eu>)
* `ckanext.ozwillo_theme.plugin.ozwillo_portal_url` (eg <https://portal.ozwillo-preprod.eu>)
* `ckanext.ozwillo_theme.plugin.ozwillo_ckan_app_id` (CKAN app UUID in Ozwillo portal)

You can customize the homepage with these parameters:

     # The parameters of the map display on the page (here are production parameters)
    ckanext.ozwillo_theme.view_id = 038a8703-6031-4386-a962-7d55029724df
    ckanext.ozwillo_theme.resource_id = c39c4c65-ffba-4a30-a164-bb29fa0e6fc1
    ckanext.ozwillo_theme.package_id = syn
    # To activate the location field, install ckanext-spatial and then set
    ckanext.ozwillo_theme.spatial_installed = true
    # To use OSM names typeahead suggestions, register and get a key, then complete the parameter
    ckanext.ozwillo_theme.osmnames_key = [your key]

Development Installation
========================

To install ckanext-raseel-theme for development, activate your CKAN
virtualenv and do:

    git clone https://github.com/ozwillo/ckanext-raseel-theme.git
    cd ckanext-raseel-theme
    python setup.py develop
    pip install -r dev-requirements.txt

Translations
============

In development mode, just do

    python setup.py compile_catalog

For more setup, just follow instructions here: <https://docs.ckan.org/en/2.8/extensions/translating-extensions.html> 
(you need a working installation of CKAN and an active virtualenv for it to work).

Running the Tests
=================

To run the tests, do:

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (`pip install coverage`) then run:

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.ozwillo_theme --cover-inclusive --cover-erase --cover-tests
