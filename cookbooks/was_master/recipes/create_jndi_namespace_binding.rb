#
# Cookbook:: was_master
# Recipe:: create_jndi_namespace_binding
#
# Copyright:: 2018, The Authors, All Rights Reserved.
jython_script_name = 'crtNameSpaceBinding.py'

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

execute "Create JNDI Namespace Binding" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption #{node['was']['java_option_first']} -javaoption #{node['was']['java_option_second']} -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['jndi_scope']}\" \"#{node['was']['node_name']}\" \"#{node['was']['server_or_cluster_name']}\" \"#{node['was']['binding_identifier']}\" \"#{node['was']['name_in_space']}\" \"#{node['was']['string_value']}\" \"YES\""
end

#Scope ( Cell, Node, Cluster, Server ), node name ( ‘none’ if scope is Cell or Cluster), server/cluster name ( ‘none’ if scope is Cell or Node), binding identifier (name), name in space, string value, debug
