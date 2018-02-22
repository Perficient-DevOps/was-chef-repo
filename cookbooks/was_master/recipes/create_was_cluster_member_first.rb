#
# Cookbook:: was_master
# Recipe:: create_was_cluster_member_first
#
# Copyright:: 2018, The Authors, All Rights Reserved.

jython_script_name = 'crtClusterMemberFirst.py'

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

execute "Start Cluster" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['create_cluster_name']}\" \"#{node['was']['cluster_first_member_name']}\" \"#{node['was']['cluster_first_node_name']}\" \"YES\""
end

#cluster_name cluster_member_name cluster_node_name
