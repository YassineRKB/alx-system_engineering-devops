# puppet manifest to install and configure nginx + 404 page
exec { 'apt update':
  command => 'apt-get update',
  path    => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure     => 'installed',
}
file { 'nginx index.html':
  require => Package['nginx'],
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n'
}
file { 'nginx 404.html':
  require => Package['nginx'],
  path    => '/var/www/html/404.html',
  content => 'Ceci n\'est pas une page\n'
}
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-available/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
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
