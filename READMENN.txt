To set up a silcc server instance:

1) Create a Python virtualenv

2) In the this distribution run:

$ python setup.py develop

This should install all needed libraries in your virtual environment.

3) You also need to install nltk. Download it from the following location:

$ wget http://nltk.googlecode.com/files/nltk-2.0b8.zip
$ unzip nltk-2.0b8.zip
$ cd nltk-2.0b8.zip

Now make sure you have activated the virtualenv created in step 1.

If you are sure its activated, issue the following to install nltk into
your virtualenv.

$ python setup.py install

4) After installing nltk you need to download one
of the Treebank Corpus for the part-of-speech tagger to work:

$ python
>>> import nltk
>>> nltk.download()

This will take you into an interactive download environment.
The corpus you want to download is: maxent_treebank_pos_tagger
After downloading it quit python.

5) Create the database. The scripts/schema.sql file
contains the table definitions. If using MySQL:

$ mysql -u root -p

Once in the mysql environment:

>>> create database silcc default charset utf8;
>>> grant all on silcc.* to silcc@localhost identified by 'password';

Make sure the .ini file contains a DB URI to the above database.

6) Now populate the place names database using the script provided:

First download the free place names data from:
http://download.geonames.org/export/dump/allCountries.zip

Unzip the file, then: 

python scripts/load_place_names.py allCountries.txt

7) To start the server:

$ paster serve prod.ini

