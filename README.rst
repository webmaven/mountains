mountains.py
============

A simple command line script that processes a remote URL, retreives a csv file
at that URL, and outputs a timestamp and the name and altitude (if known) for
each.

Is tolerant of unicode csv data (by coercing to UTF-8), and of large files (by
streaming the results of the request).

Usage::
    
    mountains.py [-h] URL
    
    positional arguments:
    URL         A URL to a mountain data file.
    
    optional arguments:
      -h, --help  show this help message and exit

Example::

    [user@host]$python ./abc/mountains.py 'http://www.catalystsecure.com/public/tasks/mountains/mountains-1.csv'
    2014-01-16 15:42:29 (Friday)
    
    Angel Peak has an altitude of 6858 meters.
    Queen Charlotte Island has an altitude of unknown meters.
    Anticosti Island has an altitude of unknown meters.
    Qaqqarsuaq has an altitude of 1157 meters.
    Tarajornitsut has an altitude of 300 meters.
    Nipisat has an altitude of unknown meters.
    Akilia has an altitude of unknown meters.
    Elm Point has an altitude of 324 meters.
    Indian Hill has an altitude of 408 meters.
    Oak Island has an altitude of 326 meters.
    [user@host]$

