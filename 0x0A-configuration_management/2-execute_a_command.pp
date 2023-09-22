#task 2: manifest to kill process named killmenow
exec {'kill killmenow':
    command => '/usr/bin/pkill -f kilmenow',
}