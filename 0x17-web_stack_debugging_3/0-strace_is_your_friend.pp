# wordpress fix
exec { 'wordpres_fix':
  command  => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  provider => 'shell',
}
