#!/usr/bin/python
import argparse
import os
import re
import time
from datetime import datetime

parser = argparse.ArgumentParser(description='Create a new post')
parser.add_argument('-n','--name', help='Name for the markdown file', required=False, default=None)
parser.add_argument('-d','--date', help='Date of the post: YYYY-MM-DD', required=False, default=None)

args = vars(parser.parse_args())

# Check if a date is valid and returns it with a valid format
# If empty return current date
def validateDate(date):
	if date == None:
		return None
	try:
		if date == "":
			date = time.strftime('%Y-%m-%d')
		else:
			date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
	except ValueError:
		date = None
	return date

# Ask for the date and return a validate string with format: YYYY-MM-DD
def getDate():
	date = validateDate(args['date'])
	while date == None:
		print "\nPlease specify a date with the format: YYYY-MM-DD"
		print "Press enter again to use current date.\n"
		date = raw_input("--> ")
		date = validateDate(date)
	return date

# Clean non-word characters and whitespaces
def clearString(s):
	# Remove all duplicated whitespaces
	s = re.sub(' +', ' ', s).strip()
	# Remove all non-word characters (everything except numbers and letters)
	s = re.sub(r"[^\w\s-]", '', s).strip()
	# Replace all runs of whitespace with a single dash
	s = re.sub(r"\s", '-', s).strip()
	# If the string was empty or just containing one single whitespace then return None
	if s == '-' or s == '':
		return None
	return s

# Ask for filename
def getFilename():
	filename = clearString(args['name'] if args['name'] != None else "")
	if filename == "":
		filename = None

	while filename == None:
		filename = getValidRawInput("Please specify a FILENAME for the .md file:")
		filename = clearString(filename)
		if filename == "":
			filename = None

	return filename

# Returns an input string
def getValidRawInput(prompt):
	title = None
	while title == None:
		print "\n" + prompt + "\n"
		title = raw_input("--> ").strip()
		if title == "":
			title = None
	return title

# Create the markdown file for the new post.
def createMarkdownFile(filename, date, title, text):
	root = os.path.dirname(os.path.realpath(__file__))
	md_path = (root + '/_posts/' + date + '-' + filename + '.md')
	f = open(md_path,'w')
	f.write('---\nlayout: post\n') # python will convert \n to os.linesep
	f.write('title: %s\n' % title)
	f.write('summary: %s\n' % text)
	f.write('---\n')
	f.close() # you can omit in most cases as the destructor will call it

# Get all important data
date = getDate()
filename = getFilename()
title = getValidRawInput("Please specify a TITLE for the new post:")
text = getValidRawInput("Please specify a DESCRIPTION TEXT for the new post:")

# Create thumbnail, large image and post.
createMarkdownFile(filename, date, title, text)
