#
# Cookbook:: was_master
# Recipe:: datasource_min_max_connection_pool
#
# Copyright:: 2018, The Authors, All Rights Reserved.
jython_script_name = 'setDataSourceConnectionPool.py'

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

execute "Datasource Set Min Max Connection Pool" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}' -javaoption \"#{node['was']['java_option_first']\" -javaoption \"#{node['was']['java_option_second']\" -f #{node['was']['jython_path']}/#{jython_script_name} \"#{node['was']['data_source_name']}\" \"#{node['was']['data_source_min']}\" \"#{node['was']['data_source_max']}\" \"#{node['was']['reap_time']}\" \"#{node['was']['unused_timeout']}\" \"#{node['was']['aged_timeout']}\" \"#{node['was']['purge_policy']}\" \"#{node['was']['scope_level']}\" \"#{node['was']['data_source_cluster_or_server']}\" \"#{node['was']['node_name']}\" \"#{node['was']['provider_name']}\" \"YES\""
end

#1Data source name, 2min connections, 3maximum connections, reap time, unused timeout, aged timeout, Purge Policy ( FailingConnectionOnly, EntirePool), scope ( Cell, Cluster, Node, Server ), server or cluster name ( not used for node scope – use none ), node name ( not used for Cell or Cluster scope ), jdbc provider name associated with datasource, debug
