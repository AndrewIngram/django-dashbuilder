Django Dashbuilder
==================

**This project is still in very early development and is still missing a lot of important functionality that would make it usable. It also depends on Django 1.4 (alpha).**

The goal of this library is to provide an alternative dashboad for situations where Django's existing admin app isn't flexible enough. Dashbuilder isn't intended to be a complete replacement, but rather a starting point for rolling your own dashbboards quickly.

Dashbuilder is...
-----------------

1. Declarative. Django's declative models, forms and admin site are a good thing, so more of the same makes sense.
2. Explicit. No iterating over INSTALLED_APPS looking for modules happens, if you want something in the dashboard it's up to you to add it. You have complete control over how things are orgnaised
3. Familiar. Django's class-based views are used heavily, as well as my own formset views from django-extra-views.
4. Hierarchical. Each app is aware of its parent apps.