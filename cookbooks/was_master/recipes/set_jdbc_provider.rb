#
# Cookbook:: was_master
# Recipe:: set_jdbc_provider
#
# Copyright:: 2018, The Authors, All Rights Reserved.

jython_script_name = 'crtJDBCProvider.py'

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


execute "Set JDBC Provider" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption \"#{node['was']['java_option_first']\" -javaoption \"#{node['was']['java_option_second']\" -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['cluster_or_server_name']}\" \"#{node['was']['db_type']}\" \"#{node['was']['jdbc_provider']}\" \"#{node['was']['data_source_implementation_type']}\" \"#{node['was']['provider_name']}\" \"#{node['was']['provider_jar_path']}\"  \"#{node['was']['provider_description']}\" \"#{node['was']['implementation_class_name']}\" \"#{node['was']['scope_level']}\" \"#{node['was']['node_name']}\" \"YES\""
end

# 1Cluster/server  name, 2database type, 3provider type, 4implementation type, 5provide descriptive name, 6classpath, 7description, 8implementation class name, 9Scope, 10Node name, debug.
# Scope: “Cell” , “Cluster”, “Node” or “Server”
#
# 1Cluster name, 2database type, 3provider type, 4implementation type, 5provide descriptive name, 6classpath, 7description, 8implementation class name, 9Scope, debug.
# Scope: “Cell” or “Cluster”
# If “Cluster” is specified for scope, then “Cluster name” parameter must contain valid cluster name.
#
#
# Example to create Oracle provider at cell level:
#./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -user wasadmin -password adminwas -f /WorkingData/jythonScripts/crtJDBCProvider.py 1"DevCluster" 2"Oracle" 3"Oracle JDBC Driver" 4"Connection pool data source" 5"Cell Oracle Provider" 6"/home/wasadmin/ojdbc6.jar" 7"Oracle provider description text" 8"oracle.jdbc.pool.OracleConnectionPoolDataSource" 9"Cell" "YES"
#Example to create Oracle provider at cluster level:
#./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -user wasadmin -password adminwas -f /WorkingData/jythonScripts/crtJDBCProvider.py "DevCluster" "Oracle" "Oracle JDBC Driver" "Connection pool data source" "Cell Oracle Provider" "/home/wasadmin/ojdbc6.jar" "Oracle provider description text" "oracle.jdbc.pool.OracleConnectionPoolDataSource" "Cluster" "YES"
