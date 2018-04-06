#
# Cookbook:: was_master
# Recipe:: restart_test_jdbc_cluster
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Restart and Test JDBC Cluster' do
  script_path File.join( node[:was][:jython_path], 'restartTestJDBCCluster.py' )
  script_options "\"#{node['was']['create_cluster_name']}\" \"#{node['was']['data_source_name']}\" \"YES\""
end
