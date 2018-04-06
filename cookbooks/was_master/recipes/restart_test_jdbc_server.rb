#
# Cookbook:: was_master
# Recipe:: restart_test_jdbc_server
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Restart and Test JDBC Server' do
  script_path File.join( node[:was][:jython_path], 'restartTestJDBCServer.py' )
  script_options "\"#{node['was']['server_name']}\" \"#{node['was']['node_name']}\"  \"#{node['was']['data_source_name']}\" \"YES\""
end
