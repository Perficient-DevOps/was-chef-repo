#
# Cookbook:: was_master
# Recipe:: create_cluster
#
# Copyright:: 2018, The Authors, All Rights Reserved.

wsadmin 'Create Cluster' do
  script_path File.join( node[:was][:jython_path], 'crtCluster.py' )
  script_options "\"#{node['was']['create_cluster_name']}\" \"YES\""
  not_if { ::File.exist?( "#{node['was']['install_home']}profiles/#{node['was']['dmgr_profile_name']}/config/cells/#{node['was']['cell_name']}/clusters/#{node['was']['create_cluster_name']}")}
end
