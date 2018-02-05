#
# Cookbook Name:: delete_was_server
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.
temp_script= File.join( Chef::Config[:file_cache_path], 'delete-server.py' )

template temp_script do
  source 'delete-server.py.erb'

  variables({
    :node_name => node['was']['node_name'],
    :server_name => node['was']['server_name']
    })
end

execute "Run Jython" do
  command "/opt/IBM/WAS8.5.5/bin/wsadmin.sh -profileName #{node['was']['profile_name']} -lang jython -f #{temp_script}"
end
