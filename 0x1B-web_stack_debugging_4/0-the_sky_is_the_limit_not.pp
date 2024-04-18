#change the ulimits for nginx

exec {"change limit on open files"
	command => 'sed -i "s/15/10000/" /etc/defualt/nginx && service nginx restart',
	path 	=> "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}
