#
# Cookbook Name:: create_was_server
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.
temp_script= File.join( Chef::Config[:file_cache_path], 'create-server.py' )

template temp_script do
  source 'create-server.py.erb'
  variables({
    :node_name => node['was']['node_name'],
    :server_name => node['was']['server_name']
    })
end

execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -profileName #{node['was']['profile_name']} -lang jython -f #{temp_script}"
end
