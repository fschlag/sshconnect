sshconnect
==========

Simple ssh bookmark tool that can be used to connect to ssh servers.
I created it for my personal use but maybe it is useful for someone else. Feel free to use it. ;-)

Tested on
- Mac OS X 10.9 & 10.10.1
- Debian 7
- CentOS 6.4

Requires Python 2.6 or greater.

Sample config
----------

	{
		"connections": [
	 		{
	 			"name": "Name of first connection",
	 			"connection": "username@server",
	 			"key": ""
	 		},
	 		{
	 			"name": "Name of second connection",
	 			"connection": "username@server2",
	 			"key": "/Path/to/identity/file"
	 		}
	 	]
	}
	
How to use
----------
Save your configuration inside your home directory e.g. ~/.sshconnect

- /home/<your username>/.sshconnect on Linux
- /Users/<your username>/.sshconnect on Mac OS X

Run the application by executing 

	python sshconnect.py

alternatively you can create a symbolic link under /usr/bin 

	sudo ln -s /path/to/sshconnect.py /usr/bin/sshconnect

