mountains.py
============

A simple command line script that processes a remote URL, retreives a csv file
at that URL, and outputs the name and altitude (if known) for each.

Is tolerant of unicode csv data (by coercing to UTF-8), and of large files (by
streaming the results of the request).
