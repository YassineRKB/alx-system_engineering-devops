#task 2: manifest to kill process named killmenow
exec {'pkill killmenow':
    command => '/usr/bin/pkill kilmenow',
}