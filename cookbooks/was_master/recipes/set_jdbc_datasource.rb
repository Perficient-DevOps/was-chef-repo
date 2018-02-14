#
# Cookbook:: was_master
# Recipe:: set_jdbc_datasource
#
# Copyright:: 2018, The Authors, All Rights Reserved.


execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f /WorkingData/jythonScripts/crtJDBCDataSource.py \"#{node['was']['data_source_name']}\" \"#{node['was']['data_source_jndi']}\" \"#{node['was']['data_source_description']}\" \"Cell\" \"Cell\" \"#{node['was']['provider_name']}\" \"#{node['was']['database_path']}\" \"#{node['was']['db_adapter']}\" \"true\" \"#{node['was']['cluster']}\" \"YES\""
end
