# Install NGINX package
package { 'nginx':
  ensure => present,
}

# Define a location block with a custom header
nginx::resource::location { 'example_location':
  location   => '/',
  add_header => {
    'Custom-Header' => 'Your-Header-Value',
  },
}

# Ensure NGINX service is running
service { 'nginx':
  ensure => running,
}

