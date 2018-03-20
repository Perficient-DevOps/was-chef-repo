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

execute "Create a WAS Application Server" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -profileName #{node['was']['profile_name']} -lang jython  -f #{temp_script} -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}'"
  not_if { ::File.exist?( "#{node['was']['install_home']}profiles/#{node['was']['profile_name']}/config/cells/#{node['was']['cell_name']}/nodes/#{node['was']['node_name']}/servers/#{node['was']['server_name']}/server.xml")}
end
