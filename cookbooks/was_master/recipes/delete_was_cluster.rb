#
# Cookbook:: was_master
# Recipe:: delete_was_cluster
#
# Copyright:: 2018, The Authors, All Rights Reserved.

jython_script_name = 'dltCluster.py'

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

execute "Delete Cluster" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption #{node['was']['java_option_first'] -javaoption #{node['was']['java_option_second'] -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['create_cluster_name']}\" \"YES\""
end
