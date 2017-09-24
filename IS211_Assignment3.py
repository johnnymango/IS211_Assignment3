#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imported Modules
import argparse
import urllib2
import csv
import re

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

    #Counts for the Image Hits
    total_image_count = 0
    jpeg_count = 0
    gif_count = 0
    png_count = 0

    #Dict to identify top browser.
    browsers = {'Firefox': 0,
                'IE': 0,
                'Safari': 0,
                'Chrome': 0}

    #Searches the file using RE for strings instances of the image type
    for row in mywebpage:
        #print row
        if re.search(r'.jpg$|.gif$|.png$|.JPEG$', row[0], re.IGNORECASE):
          total_image_count += 1
        if re.search(r'.jpg$|.JPEG$', row[0], re.IGNORECASE):
            jpeg_count += 1
        if re.search(r'.gif$', row[0], re.IGNORECASE):
            gif_count += 1
        if re.search(r'.png$', row[0], re.IGNORECASE):
            png_count += 1

    #Searches for browsers in User Agent string
        if re.search('Firefox', row[2]):
            browsers['Firefox'] += 1
        if re.search('MSIE', row[2]):
            browsers['IE'] += 1
        if re.search(r'Safari/\d{0,4}.\d{0,2}$', row[2]):
            browsers['Safari'] += 1
        if re.search(r'Chrome/\d{1,2}.\d{0,1}.\d{0,4}.\d{0,1}', row[2]):
            browsers['Chrome'] += 1

    #Calculates percentages for each image type
    percentjpg = (float(jpeg_count) / float(total_image_count))*100
    percentpng = (float(png_count) / float(total_image_count))*100
    percentgif = (float(gif_count) / float(total_image_count))*100

    #Finds the most popular browser in the browers dict
    popular_browser = max(browsers.iterkeys(), key=(lambda key: browsers[key]))

    #Prints Image Type Results
    print "There are a total of {} image requests found in the file.".format(total_image_count)
    print "GIF image requests account for {}% of all requests.".format(round(percentgif, 1))
    print "JPG image requests account for {}% of all requests.".format(round(percentjpg,1))
    print "PNG image requests account for {}% of all requests.".format(round(percentpng, 1))
    print

    #Prints the most popular browser.
    print "The browser results are: {}".format(browsers)
    print
    print "The most popular browser is {}.".format(popular_browser)



def main():
            mywebpage = downloadData(url)
            processImages(mywebpage)



if __name__ == "__main__":
    main()