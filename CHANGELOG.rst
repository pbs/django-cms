CHANGELOG
=========

Revision c975832 (03.07.2014, 07:43 UTC)
----------------------------------------

* LUN-1562

  * Made the 'table row' (in fact it's made with divs) in the cms pages admin view not to overlap

No other commits.

Revision 46802f2 (13.06.2014, 12:31 UTC)
----------------------------------------

* LUN-1596

  * Set callback to delete empty plugin image in text editor

* LUN-1633

  * page choices should be cached only for the sites that are in cache. Fixes the following problem: a site is created through the dbshell and the cache is not invalidated since the post save signals are not called.

No other commits.

Revision 6250c2b (30.05.2014, 10:50 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Added tests for cache invalidation on page/site choices for page form field.
  * Pages choices are now cahced per site.
  * (tox) Fixed test results destination
  * Improved performance for fetching page field choices.
  * (tox) Added tox.ini

Revision 9c9ddef (17.04.2014, 13:11 UTC)
----------------------------------------

Changelog history starts here.
