# puppet manifest to config a server
exec { 'apt-operations':
  command => 'sudo apt update -y && sudo apt install nginx -y',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/test ! -f /etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        
        add_header X-Served-By $HOSTNAME;
        
        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
    }
  ',
  require => Exec['apt-update-install-nginx'],
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
