#
# Cookbook Name:: was
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

jython_script_name = 'setJVMHeap.py'

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

execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['node_name']}\" \"#{node['was']['server_name']}\" \"#{node['was']['server_min_heap']}\" \"#{node['was']['server_max_heap']}\" \"YES\""
end
