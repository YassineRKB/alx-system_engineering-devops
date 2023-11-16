# puppet manifest to fix both soft and hard limits
exec { 'hard':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 6009/" /etc/security/limits.conf',
  provider => 'shell'
}
-> exec { 'soft':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 6969/" /etc/security/limits.conf',
  provider => 'shell'
}
