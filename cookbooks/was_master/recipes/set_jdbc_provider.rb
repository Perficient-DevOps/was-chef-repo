#
# Cookbook:: was_master
# Recipe:: set_jdbc_provider
#
# Copyright:: 2018, The Authors, All Rights Reserved.

execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f /WorkingData/jythonScripts/crtJDBCProvider.py \"#{node['was']['cluster']}\" \"#{node['was']['db_name']}\" \"#{node['was']['jdbc_provider']}\" \"#{node['was']['data_source_implementation_provider']}\" \"#{node['was']['provider_name']}\" \"#{node['was']['provider_jar_path']}\" \"#{node['was']['provider_description']}\" \"#{node['was']['data_source_namespace']}\" \"#{node['was']['scope_level']}\" \"YES\""
end
