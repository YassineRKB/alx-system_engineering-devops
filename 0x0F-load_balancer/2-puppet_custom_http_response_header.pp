# puppet manifest to config a server
exec { 'apt operations':
  command     => 'sudo apt-get -y update; sudo apt-get -y install nginx',
  provider => shell,
}
-> exec { 'seeding the configuration':
  command => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  provider => shell,
}
-> exec { 'service nginx restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
