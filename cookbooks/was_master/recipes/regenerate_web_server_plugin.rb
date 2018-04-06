#
# Cookbook:: was_master
# Recipe:: regenerate_web_server_plugin
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Regen Webserver Plugin' do
  script_path File.join( node[:was][:jython_path], 'regenWebServerPlugin.py' )
  script_options "\"#{node['was']['web_node_name']}\" \"#{node['was']['web_server_name']}\" \"YES\""
end
