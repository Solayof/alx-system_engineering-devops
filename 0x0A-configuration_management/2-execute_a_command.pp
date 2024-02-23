#script that kill a process called menow

exec {
  'pkill':
    command  => 'pkill killmenow',
    provider => 'shell',
}
