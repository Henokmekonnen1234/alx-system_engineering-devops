file { '~/.ssh/config':
    ensure  => 'file',
    content => "
Host alxstudentserver
  HostName 52.201.221.223
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
  }
