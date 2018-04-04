#
# Cookbook:: was_master
# Recipe:: create_was_cluster_member_first
#
# Copyright:: 2018, The Authors, All Rights Reserved.

wsadmin 'Create First Cluster Member' do
  script_path File.join( node[:was][:jython_path], 'crtClusterMemberFirst.py' )
  script_options "\"#{node['was']['create_cluster_name']}\" \"#{node['was']['cluster_first_member_name']}\" \"#{node['was']['cluster_first_node_name']}\" \"YES\""
  not_if { ::File.readlines( "#{node['was']['install_home']}profiles/#{node['was']['dmgr_profile_name']}/config/cells/#{node['was']['cell_name']}/clusters/#{node['was']['create_cluster_name']}/cluster.xml").grep("#{node['was']['create_cluster_name']}").empty? }
end
