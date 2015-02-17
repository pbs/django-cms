CHANGELOG
=========

Revision fdd78c9 (17.02.2015, 10:33 UTC)
----------------------------------------

* LUN-2055

  * fixed double encoding when hitting cancel button

No other commits.

Revision 2e0b6f6 (06.02.2015, 13:17 UTC)
----------------------------------------

No new issues.

* Misc commits

  * small change
  * move page into closed/open page

Revision 182cafd (17.11.2014, 16:34 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Update cms version
  * added some comments to make the code more explicit.
  * Added some tests for multiple sites permission issues
  * Users with pages permissions should always have access to admin pages section on the sites they have access to.
  * Pages changelist should always show items from an allowed working site.

Revision 842b35f (22.10.2014, 14:27 UTC)
----------------------------------------

* LUN-1912

  * Fix plugin editing icons position, disable editing when icons are visible

No other commits.

Revision 866ddbf (15.10.2014, 12:07 UTC)
----------------------------------------

* LUN-986

  * LUN-1608: Apply LUN-986 (make iframe embedable in text plugin)

* LUN-1608

  * fix tests
  * remove debug
  * move iframe_HTML_decode.py to cms templatetags folder, minor code refactor
  * ignore case when replacing
  * rename plugin controls styles id
  * minor code refactor
  * remove logging
  * Apply LUN-986 (make iframe embedable in text plugin)
  * add edit and delete plugin controlls in tinymce

No other commits.

Revision 4c4b59a (09.09.2014, 09:00 UTC)
----------------------------------------

* LUN-1452

  * Removed unnecessary path updates on move. Title paths are correctly updated on move for all cases (in page post save signal): * moved page becomes homepage * moved page was homepage before save * all descendants title paths are updated

* LUN-1832

  * fixed overwrite_url disappearance

* Misc commits

  * Update version as instructed by bamboo

Revision 4b5f557 (18.08.2014, 12:39 UTC)
----------------------------------------

* LUN-1371

  * Move the fix for LUN-1371 from django-robots to cms, where the fix seems to be more suitable due to the intrisic knowledge about cms internals.

No other commits.

Revision f62e66b (05.08.2014, 12:32 UTC)
----------------------------------------

No new issues.

* Misc commits

  * get_object_queryset should return a queryset without evaluation; This is a performance improvement(even with the extra query) that doesn't change the previous logic.

Revision c6668cc (08.07.2014, 11:31 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Test moving home page down rewrites new home path.
  * pages should be cached only for sites that do not have pages in cache
  * fixed: page choices were always fetched from the databse even if they were in cache.
  * Update home only if the previous home was moved.
  * Save home to force removal of first slug.

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
