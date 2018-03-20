#
# Cookbook:: was_master
# Recipe:: set_jvm_log_size
#
# Copyright:: 2018, The Authors, All Rights Reserved.

jython_script_name = 'setJVMLogSize.py'

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

execute "Set JVM Log Size" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -javaoption #{node['was']['jvm_size']} -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['node_name']}\" \"#{node['was']['server_name']}\" \"#{node['was']['log_name']}\" \"#{node['was']['log_size']}\" \"#{node['was']['max_logs_to_keep']}\" \"YES\""
end