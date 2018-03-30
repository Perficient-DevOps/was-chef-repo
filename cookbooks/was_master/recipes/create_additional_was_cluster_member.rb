#
# Cookbook:: was_master
# Recipe:: create_was_cluster_member
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Create First Cluster Member' do
  script_path File.join( node[:was][:jython_path], 'crtClusterMember.py' )
  script_options"\"#{node['was']['create_cluster_name']}\" \"#{node['was']['cluster_subsequent_member_name']}\" \"#{node['was']['cluster_subsequent_node_name']}\" \"YES\""
end
