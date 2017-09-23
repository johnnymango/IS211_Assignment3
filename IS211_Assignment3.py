#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imported Modules
import argparse
import urllib2
import csv
import re
from StringIO import StringIO

# Sets up the argparse to accept the url argument when the py file is executed.
parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, required=True)
args = parser.parse_args()
url = args.url


# Function downloads the data from the argparse URL argument, reads and returns the data as csv
def downloadData(urlname):
    response = urllib2.urlopen(urlname)
    mywebpage = csv.reader(response)
    return mywebpage

#Function counts total image counts, calculates their percentages and displays results.
def processImages(mywebpage):
    total_image_count = 0
    jpeg_count = 0
    gif_count = 0
    png_count = 0

    #Searches the file using RE for strings instances of the image type
    for row in mywebpage:
        if re.search(r'.jpg$|.gif$|.png$|.JPEG$', row[0], re.IGNORECASE):
          total_image_count += 1
        if re.search(r'.jpg$|.JPEG$', row[0], re.IGNORECASE):
            jpeg_count += 1
        if re.search(r'.gif$', row[0], re.IGNORECASE):
            gif_count += 1
        if re.search(r'.png$', row[0], re.IGNORECASE):
            png_count += 1

    #Calculates percentages for each image type
    percentjpg = (float(jpeg_count) / float(total_image_count))*100
    percentpng = (float(png_count) / float(total_image_count))*100
    percentgif = (float(gif_count) / float(total_image_count))*100

    #Print
    print "There are a total of {} image requests found in the file.".format(total_image_count)
    print "GIF image requests account for {}% of all requests.".format(round(percentgif, 1))
    print "JPG image requests account for {}% of all requests.".format(round(percentjpg,1))
    print "PNG image requests account for {}% of all requests.".format(round(percentpng, 1))


def processBrowser(mywebpage):
    pass


def main():
            mywebpage = downloadData(url)
            processImages(mywebpage)
            processBrowser(mywebpage)



if __name__ == "__main__":
    main()