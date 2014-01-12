#!/usr/bin/env python
#
# A simple command-line tool for processing mountain files

import argparse
import csv
import requests
from datetime import datetime

timestamp = datetime.now()


def unicode_csv_dictreader(unicode_csv_data, **kwargs):
    """csv.py doesn't do Unicode, so encode as UTF-8"""

    csv_dictreader = csv.DictReader(unicode_csv_data, **kwargs)
    for row in csv_dictreader:
        yield dict((key, unicode(value, 'utf-8'))
                   for key, value in row.iteritems())

if __name__ == '__main__':
    """Download and parse mountain data files for name and altitude."""
    parser = argparse.ArgumentParser(description="Parse mountain data files")
    parser.add_argument("URL", help="A URL to a mountain data file.")
    args = parser.parse_args()
    print timestamp.strftime(u"%Y-%m-%d %H:%M:%S (%A)\n")
    # For potentially large downloads, stream the response, and iterate
    # over the lines.
    csvdata = requests.get(args.URL, stream=True).iter_lines()
    # Use a Unicode wrapper around DictReader
    mcsv = unicode_csv_dictreader(csvdata)
    for row in mcsv:
        name = row['Name']
        altitude = row['Altitude (m)']
        if altitude == 'null':
            altitude = 'unknown'
        print u"%s has an altitude of %s meters." % (name, altitude)
