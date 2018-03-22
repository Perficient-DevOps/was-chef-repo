#
# Cookbook:: was_master
# Recipe:: create_web_server
#
# Copyright:: 2018, The Authors, All Rights Reserved.
jython_script_name = 'crtWebServer.py'

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

execute "Create Web Server" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption \"#{node['was']['java_option_first']}\" -javaoption \"#{node['was']['java_option_second']}\" -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['node_name']}\" \"#{node['was']['web_server_name']}\"
  \"#{node['was']['web_server_port']}\" \"#{node['was']['plugin_install_root']}\" \"#{node['was']['web_install_root']}\" \"#{node['was']['admin_user_id']}\" \"#{node['was']['admin_password']}\" \"#{node['was']['web_server_type']}\" \"YES\""
end

#Node name, web server name, web server port, pluginInstallRoot, webInstallRoot, adminUserID, adminPasswd, web server type ( SUN or IHS ), debug
