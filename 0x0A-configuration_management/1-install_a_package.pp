# installes the flask from pip
iipackage  {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
