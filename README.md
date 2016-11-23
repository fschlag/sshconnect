sshconnect
==========

Simple ssh bookmark tool that can be used to connect to ssh servers.
I created it for my personal use but maybe it is useful for someone else. Feel free to use it. ;-)

Tested on
- Mac OS X 10.10.x
- Debian 7
- CentOS 6.4

Requires Python 2.6 or greater.

Changelog
----------
#### Version 0.3
- Now its possible to define port to connection
- Added X11 Forwarding resource


#### Version 0.2
- Preselect a connection by its connection number
- Print help message
- Print version number
- Improved error handling
- Refactoring

#### Version 0.1
- Initial release

Sample config
----------

{
	"connections": [
 		{
 			"name": "Name of first connection",
 			"host": "ip",
 			"password": "****",
 			"key": "/Path/to/identity/file"
 			"user": "login",
			"port": "22222",
			"enableX11":"Yes"
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

- /home/&lt;your username&gt;/.sshconnect on Linux
- /Users/&lt;your username&gt;/.sshconnect on Mac OS X

Run the application by executing 

	python sshconnect.py

alternatively you can create a symbolic link under /usr/bin 

	sudo ln -s /path/to/sshconnect.py /usr/bin/sshconnect

