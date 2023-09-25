# puppet manifest to install and configure nginx + index + redirect_me + 404
exec { 'apt update':
  command => 'apt-get update',
  path    => '/usr/bin',
}
package { 'nginx':
  ensure => 'installed',
}
file { '/var/www/html/index.html':
  ensure  => 'file',
  require => Package['nginx'],
  content => 'Hello World!\n',
}
file { '/var/www/html/404.html':
  ensure  => 'file',
  require => Package['nginx'],
  content => "Ceci n'est pas une page\n",
}
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
    }
    error_page 404 /404.html;
    location  /404.html {
        internal;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
}
",
}
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [File['/etc/nginx/sites-available/default'], Package['nginx']],
}
