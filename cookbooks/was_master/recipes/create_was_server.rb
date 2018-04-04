#
# Cookbook Name:: create_was_server
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

current_script= File.join( Chef::Config[:file_cache_path], 'create-server.py' )

template current_script do
  source 'create-server.py.erb'
  variables({
    :node_name => node['was']['node_name'],
    :server_name => node['was']['server_name']
    })
end

wsadmin 'Create WebSphere Server' do
  script_path current_script
  script_options ""
  not_if { ::File.exist?( "#{node['was']['install_home']}profiles/#{node['was']['dmgr_profile_name']}/config/cells/#{node['was']['cell_name']}/nodes/#{node['was']['node_name']}/servers/#{node['was']['server_name']}/server.xml")}
end
