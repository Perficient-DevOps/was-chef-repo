#
# Cookbook:: was_master
# Recipe:: create_jdbc_datasource_oracle
#
# Copyright:: 2018, The Authors, All Rights Reserved.

wsadmin 'Create Oracle JDBC Provider' do
  script_path File.join( node[:was][:jython_path], 'crtJDBCDataSourceOracle.py' )
  script_options "\"#{node['was']['data_source_name']}\" \"#{node['was']['data_source_jndi']}\" \"#{node['was']['data_source_description']}\" \"#{node['was']['data_source_scope']}\" \"#{node['was']['jdbc_provider_scope']}\" \"#{node['was']['provider_name']}\" \"#{node['was']['database_url']}\" \"#{node['was']['data_source_helper_class']}\" \"#{node['was']['component_managed_persistence']}\" \"#{node['was']['data_source_cluster_or_server']}\" \"#{node['was']['container_managed_persistence']}\" \"#{node['was']['jaas_alias_name']}\" \"#{node['was']['node_name']}\" \"YES\""
  not_if { ::File.readlines( "#{node['was']['install_home']}profiles/#{node['was']['dmgr_profile_name']}/config/cells/#{node['was']['cell_name']}/resources.xml").grep("#{node['was']['data_source_name']}").empty? }
end
