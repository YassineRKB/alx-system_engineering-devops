# setting a server coniguration using puppet manifest
file_line {'alxServConf'
  path => '/etc/ssh/ssh_config',
  line => 'Host 35.153.16.204
  	HostName 35.153.16.204
	User ubuntu
	IdentityFile ~/.ssh/school
	PasswordAuthentication no',
}
