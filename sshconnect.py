#!/usr/bin/env python
import sys, getopt, json
from subprocess import call
from os.path import expanduser
#
#
# Simple ssh bookmark tool
# Configuration structure is:
# 
# {
# 	"connections": [
# 		{
# 			"name": "Name of first connection",
# 			"connection": "username@server",
# 			"key": ""
# 		},
# 		{
# 			"name": "Name of second connection",
# 			"connection": "username@server2",
# 			"key": "/Path/to/identity/file"
# 		}
# 	]
# }
#
# Copyright 2014 by Florian Schlag
APPNAME = "sshconnect.py"
VERSION = 0.2

# Path to configuration file
HOME = expanduser("~")
CONFIG_FILE = HOME + "/.sshconnect"


##################################################
# Do not change anything below here
##################################################
def main(argv):
	preSelectedCon = -1;
	try:
		opts, args = getopt.getopt(argv, "hVc:", ["help","version","connection="])
	except getopt.GetoptError:
		print 'Wrong parameter(s)'
		help()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			help()
			sys.exit(0)
		elif opt in ("-V", "--version"):
			print APPNAME, VERSION
			sys.exit(0)
		elif opt in ("-c", "--connection"):
			preSelectedCon = int(arg)

	config = openConfig()
	if config is not None:
		con = preSelectedCon
		if con < 1:
			con = chooseConnection(config)
		if con is not None:
			connectTo(con, config['connections'])

def help():
	print "Usage:", APPNAME, "[-c connection no]"
	print " -h                This message"
	print " -c, --connection  Preselect a connection by its number"
	print " -V, --version     Print the version number"

def openConfig():
	try:
		config = json.loads(open(CONFIG_FILE).read())
		return config
	except IOError:
		print "Config file: \"" + CONFIG_FILE + "\" not found"
	return None

def chooseConnection(config):
	while True:
		numConnections = printMenu(config['connections'])
		try:
			print "Choose connection:",
			conn = int(raw_input())	# Read connection number
			if conn > numConnections or conn < 1:
				print "Invalid connection number. Please try again!"
			else:
				return conn
		except ValueError:
			print "Only digits are allowed! Please try again!"
		except KeyboardInterrupt:
			print ""
			break
	return None

def printMenu(connections):
	num = 0
	print "Available connections:"
	for conn in connections:
		num += 1
		print "   " + str(num) + "\t" + conn['name']
	return num

def connectTo(conNumber, connections):
	num = 0
	for conn in connections: # Find the selected connection
		num += 1
		if num == conNumber:
			try:
				if len(conn['key']) > 1: # Connect with ssh key
					call(["ssh", "-i" + conn['key'], conn['connection']])
				else: # Connect without ssh key
					call(["ssh", conn['connection']])
			except KeyboardInterrupt:
				print "Connection aborted by user"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))