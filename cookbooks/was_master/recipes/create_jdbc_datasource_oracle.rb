#
# Cookbook:: was_master
# Recipe:: create_jdbc_datasource_oracle
#
# Copyright:: 2018, The Authors, All Rights Reserved.
jython_script_name = 'crtJDBCDataSourceOracle.py'

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

execute "Create JDBC Oracle Datasource" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption #{node['was']['java_option_first'] -javaoption #{node['was']['java_option_second'] -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['data_source_name']}\" \"#{node['was']['data_source_jndi']}\" \"#{node['was']['data_source_description']}\" \"#{node['was']['data_source_scope']}\" \"#{node['was']['jdbc_provider_scope']}\" \"#{node['was']['provider_name']}\" \"#{node['was']['database_url']}\" \"#{node['was']['data_source_helper_class']}\" \"#{node['was']['component_managed_persistence']}\" \"#{node['was']['data_source_cluster_or_server']}\" \"#{node['was']['container_managed_persistence']}\" \"#{node['was']['jaas_alias_name']}\" \"#{node['was']['node_name']}\" \"YES\""
end




# "BruceOracleDataSource" "jdbc/bruceOracle" "DataSource Description" "Cell" "Cell" "Bruce Oracle Provider" "jdbc:oracle:thin:@TXAIXEBNDBD02:1536:ECPD2X" "com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper" "true" "DevCluster" "true" "myName" "YES"
