
2016-11-01
* Databases other than MySQL are now supposed, such as SqlLite3. It will just use the databases from the SETTINGS file. Make sure that the correct libraries are installed.
* New class: ProfileGroup – which has a 1:1 with Profile. It allows us to extend Profile. This is useful so that we can apply a preset filter to a user group.
* New class: Perspective – which is a collection of dashboards and pages. User groups are assigned a perspective, and a perspective determines what a particular user can see. For example, you can have a facility, or district perspective.

2016-01-15
* Fixed a bug with users that don't have a profile
* Filters are now loaded for users and groups, users they precedent

