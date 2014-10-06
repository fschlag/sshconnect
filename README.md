sshconnect
==========

Simple ssh bookmark tool that can be used to connect to ssh servers.
I created it for my personal use but maybe it is useful for someone else. Feel free to us it. ;-)

Tested on
- Mac OS X 10.9
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
