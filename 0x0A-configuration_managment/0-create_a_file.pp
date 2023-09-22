#task 0 puppet script to creat file

file { '/tmp/school':
    mode    =>  '0744',
    owner   =>  'www-data'
    group   =>  'www-data'
    content =>  'I love Puppet'
}
