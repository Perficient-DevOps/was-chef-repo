#
# Cookbook:: was_master
# Recipe:: create_shared_library
#
# Copyright:: 2018, The Authors, All Rights Reserved.

jython_script_name = 'crtSharedLib.py'

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

execute "Create Shared Library" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption \"#{node['was']['java_option_first']}\" -javaoption \"#{node['was']['java_option_second']}\" -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['library_scope']}\" \"#{node['was']['node_name']}\" \"#{node['was']['server_or_cluster_name']}\" \"#{node['was']['shared_library_name']}\" \"#{node['was']['shared_library_classpath']}\" \"#{node['was']['shared_library_description']}\" \"#{node['was']['native_library_path']}\" \"#{node['was']['isolated_class_loader']}\" \"YES\""
  live_stream true
end

#1Scope ( Cell, Node, Cluster, Server ), @node name ( ‘none’ if scope is Cell or Cluster), server/cluster name ( ‘none’ if scope is Cell or Node), shared library name, class path, description, native library path ( ‘none’ if none specified), isolated class loader ( ‘true’ or ‘false’), debug
