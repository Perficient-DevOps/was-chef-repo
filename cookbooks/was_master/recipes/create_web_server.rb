#
# Cookbook:: was_master
# Recipe:: create_web_server
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Create Web Server' do
  script_path File.join( node[:was][:jython_path], 'crtWebServer.py' )
  script_options "\"#{node['was']['node_name']}\" \"#{node['was']['web_server_name']}\" \"#{node['was']['web_server_port']}\" \"#{node['was']['plugin_install_root']}\" \"#{node['was']['web_install_root']}\" \"#{node['was']['admin_user_id']}\" \"#{node['was']['admin_password']}\" \"#{node['was']['web_server_type']}\" \"YES\""
end
