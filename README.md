About
-----

Simple website scraper built for the experince of building one....
Should scrape data from the Ripe Fruits page on sainsiburys.co.uk and then data from each product page that links from there...


Installation Notes
------------------

This app uses lmxml which is dependent upon a C lib called libxml2

To install lxml and its dependencies run:

>STATIC_DEPS=true pip install lxml

For other requirements, pip install:

>pip install -r requirements.txt


To run the tests
----------------

>python -m app.tests


To run the app
--------------

>python -m app.tests