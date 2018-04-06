#
# Cookbook:: was_master
# Recipe:: create_unmanaged_node
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Create Unmanaged Node' do
  script_path File.join( node[:was][:jython_path], 'crtUnManagedNode.py' )
  script_options "\"#{node['was']['node_name']}\" \"#{node['was']['node_host_name']}\" \"#{node['was']['node_os']}\" \"YES\""
end
