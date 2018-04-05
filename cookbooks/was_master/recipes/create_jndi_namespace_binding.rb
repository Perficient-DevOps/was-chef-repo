#
# Cookbook:: was_master
# Recipe:: create_jndi_namespace_binding
#
# Copyright:: 2018, The Authors, All Rights Reserved.

wsadmin 'Create JNDI Namespace Binding' do
  script_path File.join( node[:was][:jython_path], 'crtNameSpaceBinding.py' )
  script_options "\"#{node['was']['jndi_scope']}\" \"#{node['was']['node_name']}\" \"#{node['was']['server_or_cluster_name']}\" \"#{node['was']['binding_identifier']}\" \"#{node['was']['name_in_space']}\" \"#{node['was']['string_value']}\" \"YES\""
end
