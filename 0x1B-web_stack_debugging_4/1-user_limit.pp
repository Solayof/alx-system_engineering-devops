#change the ulimits for nginx

exec {'change the hard nofile'
  command => 'sed -i "s/5/1000/" /etc/security/limits.conf',
  path   => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    onlyif  => 'grep -q \'holberton hard nofile 5\' /etc/security/limits.conf',
}

exec {'change the soft nofile'
        command => 'sed -i "s/4/1000/" /etc/security/limits.conf',
        path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    onlyif  => 'grep -q \'holberton soft nofile 4\' /etc/security/limits.conf',
}
