#
# Cookbook:: was_master
# Recipe:: set_jdbc_provider
#
# Copyright:: 2018, The Authors, All Rights Reserved.

execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f /WorkingData/jythonScripts/crtJDBCProvider.py \"#{node['was']['cluster']}\" \"#{node['was']['db_name']}\" \"#{node['was']['jdbc_provider']}\" \"#{node['was']['data_source_implementation_provider']}\" \"#{node['was']['provider_name']}\" \"#{node['was']['provider_jar_path']}\" \"#{node['was']['provider_description']}\" \"#{node['was']['data_source_namespace']}\" \"Cluster\" \"YES\""
end
#./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -user wasadmin -password adminwas -f /WorkingData/jythonScripts/crtJDBCProvider.py "DevCluster" "Derby" "Derby JDBC Provider" "XA data source" "Bruce Provider" "/opt/IBM/WebSphere/AppServer/derby/lib/derby.jar" "description" "org.apache.derby.jdbc.EmbeddedXADataSource" "YES"
