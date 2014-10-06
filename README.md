sshconnect
==========

Simple ssh bookmark tool that can be used to connect to ssh servers.

Tested on
- Mac OS X 10.9
- Debian 7
- CentOS 6.4

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
