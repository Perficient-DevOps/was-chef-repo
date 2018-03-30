#
# Cookbook:: was_master
# Recipe:: set_jdbc_provider
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Create JDBC Provider' do
  script_path File.join( node[:was][:jython_path], 'crtJDBCProvider.py' )
  script_options "\"#{node['was']['cluster_or_server_name']}\" \"#{node['was']['db_type']}\" \"#{node['was']['jdbc_provider']}\" \"#{node['was']['data_source_implementation_type']}\" \"#{node['was']['provider_name']}\" \"#{node['was']['provider_jar_path']}\"  \"#{node['was']['provider_description']}\" \"#{node['was']['implementation_class_name']}\" \"#{node['was']['scope_level']}\" \"#{node['was']['node_name']}\" \"YES\""
end
