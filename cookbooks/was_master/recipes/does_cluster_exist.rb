#
# Cookbook:: was_master
# Recipe:: does_cluster_exist
#
# Copyright:: 2018, The Authors, All Rights Reserved.


jython_script_name = 'existsCluster.py'

wsadmin 'Does Cluster Exist' do
  script_path File.join( node[:was][:jython_path], 'existsCluster.py' )
  script_options "\"#{node['was']['create_cluster_name']}\" \"YES\""
end
