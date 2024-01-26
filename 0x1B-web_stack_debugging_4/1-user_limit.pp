# Apply this manifest to configure the OS for the holberton user

# Create holberton user
user { 'holberton':
  ensure => present,
  home   => '/home/holberton',
  shell  => '/bin/bash',
}

# Allow passwordless sudo for holberton user
file { '/etc/sudoers.d/holberton':
  ensure  => present,
  content => 'holberton ALL=(ALL:ALL) NOPASSWD:ALL',
}

# Set permissions on /home/holberton directory
file { '/home/holberton':
  ensure  => directory,
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0755',
  require => User['holberton'],
}

# Apply custom configuration to /etc/ssh/sshd_config
file { '/etc/ssh/sshd_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('profile/ssh/sshd_config.erb'),
  notify  => Service['sshd'],
}

# Restart SSH service when sshd_config is modified
service { 'sshd':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => File['/etc/ssh/sshd_config'],
}

