#
# Cookbook:: was_master
# Recipe:: start_was_server
#
# Copyright:: 2018, The Authors, All Rights Reserved.

execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f /../../jythonScripts/startAppServer.py \"#{node['was']['node_name']}\" \"#{node['was']['server_name']}\" \"YES\""
end
