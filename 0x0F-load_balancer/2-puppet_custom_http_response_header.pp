# Install NGINX package
package { 'nginx':
  ensure => present,
}

# Define a location block with a custom header
nginx::resource::location { '/etc/nginx/sites-available/default':
  location   => '/',
  add_header => {
    'X-Served-By' => $::hostname,
  },
}

# Ensure NGINX service is running
service { 'nginx':
  ensure => running,
}

