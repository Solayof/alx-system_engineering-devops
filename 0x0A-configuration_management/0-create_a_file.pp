#Script that create file "school" at /tmp directory

file {
  '/tmp/school':
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
