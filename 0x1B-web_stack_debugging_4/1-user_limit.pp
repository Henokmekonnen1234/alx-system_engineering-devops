# Puppet Manifest to configure OS for holberton user

user { 'holberton':
  ensure => present,
  shell  => '/bin/bash',
}

file { '/home/holberton':
  ensure  => 'directory',
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0755',
  recurse => true,
}

file { '/home/holberton/.ssh':
  ensure  => 'directory',
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0700',
}

file { '/home/holberton/.ssh/authorized_keys':
  ensure  => 'file',
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0600',
  content => 'your_ssh_public_key_here',
}

