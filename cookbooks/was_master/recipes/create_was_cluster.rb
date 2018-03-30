#
# Cookbook:: was_master
# Recipe:: create_cluster
#
# Copyright:: 2018, The Authors, All Rights Reserved.

wsadmin 'Create Cluster' do
  script_path File.join( node[:was][:jython_path], 'crtCluster.py' )
  script_options "\"#{node['was']['create_cluster_name']}\" \"YES\""
end
