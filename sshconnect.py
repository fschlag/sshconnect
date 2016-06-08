#!/usr/bin/env python
import sys, getopt, json
from subprocess import call
from os.path import expanduser

##############
# SSHCONNECT #
############## 
APPNAME = "sshconnect.py"
VERSION = 0.3

# Path to configuration file
HOME = expanduser("~")
CONFIG_FILE = HOME + "/.sshconnect"

# Util Variables
enableX11 = False
verboseMode = False

##################################################
# Do not change anything below here
##################################################
def main(argv):
	preSelectedCon = -1;
	try:
		opts, args = getopt.getopt(argv, "XhvVc:", ["help","version","connection=","X11"])
	except getopt.GetoptError:
		print 'Wrong parameter(s): ' + ' '.join(argv)
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
		elif opt in ("-X"):
			setX11(True)
		elif opt in ("-v", "--verbose"):
			setVerboseMode(True)
			
			
	config = openConfig()
	if config is not None:
		con = preSelectedCon
		if con < 1:
			con = chooseConnection(config)
		if con is not None:
			connectTo(con, config['connections'])

def setX11(value):
	global enableX11
	enableX11 = value

def setVerboseMode(value):
	global verboseMode
	verboseMode = value

def help():
	print "Usage:", APPNAME, "[-c connection no]"
	print " -h                This message"
	print " -c, --connection  Preselect a connection by its number"
	print " -X,  	 	 	  Enable X11 Forwarding"
	print " -v, --verbose     Print the command "
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
				
				args = []
				
				# Connect with X11 forwarding
				if enableX11 == True or 'enableX11' in conn:
					args.append("-X");
				# Connect with ssh key
				if 'key' in conn:
					args.append("-i" + conn['key']);
				# Connect to specific port
				if len(conn['port']) > 1:
					args.append("-p" + conn['port']);
				
				#  Builds the SSH Command
				command = "ssh " + ' '.join(args) + ' ' + conn['user']+"@"+conn['host']

				# Print the command
				if verboseMode == True:
					print command

				
				call(command, shell=True)
				

				
				#check_output(["ssh", ','.join(args), conn['connection']])
				#call(command)
			except KeyboardInterrupt:
				print "Connection aborted by user"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
