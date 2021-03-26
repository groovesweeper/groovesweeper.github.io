# Python Modules
import os
import lyricsgenius
import json

# Custom classes
from Filter import *
import Song
import Playlist

def add2Filter(wordstr, filt):
	wordstr = wordstr.split(",")
	for cuss in wordstr:
		filt.addWord(cuss.strip().lower())
	return

def removeFromFilter(wordstr, filt):
	wordstr = wordstr.split(",")
	for cuss in wordstr:
		filt.removeWord(cuss.strip().lower())
	return

if __name__ == "__main__":
	'''
	Dict holds exactly
	CLIENT_ID:<ID from genius API>
	CLIENT_SECRET:<secret from Genius API>
	CLIENT_TOKEN:<token from Genius API>
	'''
	client_details = {}
	with open("client_details.txt") as f:
		for line in f:
			(key, val) = line.split(":")
			client_details[key] = val
	genius = lyricsgenius.Genius(client_details["CLIENT_TOKEN"])
	filter = Filter.getInstance()

	print("Current filtered words: ", filter.getFullFilter())

	while True:
		# Main engine of the code. This will all be UI features on the main site.
		cmd = input ("Enter 'Filter', 'Search', or 'Quit': ")

		if (cmd.lower() == 'filter'):
			# This is how words are added or removed from the filter
			print("Current filtered words: ", filter.getFullFilter())
			cmd = input("Enter ADD or RMV then any number of words/phrases separated by a comma, or 'back' to go back: ")
			if (cmd == 'back'):
				continue
			elif (cmd[0:4].lower() == 'add '):
				add2Filter(cmd[4:], filter)
				print("Current filtered words", filter.getFullFilter())
			elif (cmd[0:4].lower() == 'rmv '):
				removeFromFilter(cmd[4:], filter)
				print("Current filtered words", filter.getFullFilter())
			else:
				print("Command not found")
				continue

		elif (cmd.lower() == "search"):
			cmd = input ("Enter a term to search for: ")
			ret = genius.search(cmd)
			#print(ret)
			continue

		elif (cmd.lower() == "quit"):
			# Exits the program
			break

		else:
			print("Command not found")
			continue
