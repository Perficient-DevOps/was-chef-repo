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
  command "#{node['was']['install_home']}bin/wsadmin.sh -profileName #{node['was']['profile_name']} -lang jython -f #{temp_script} -user #{node['was']['was_user']} -password #{node['was']['was_pass']}"
  not_if { ::File.exist?( "#{node['was']['install_home']}profiles/#{node['was']['profile_name']}/config/cells/#{node['was']['cell_name']}/nodes/#{node['was']['node_name']}/servers/#{node['was']['server_name']}/server.xml")}
end

jython_script_name = 'syncNode.py'

directory "#{node['was']['jython_path']}" do
  owner node[:was][:run_user]
  group node[:was][:run_group]
  mode '0755'
  action :create
  recursive true
end

cookbook_file "#{node['was']['jython_path']}/#{jython_script_name}" do
  source jython_script_name
  owner node[:was][:run_user]
  group node[:was][:run_group]
  mode '0755'
  action :create
end

execute "Sync Node" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['node_name']}\" \"YES\""
end
