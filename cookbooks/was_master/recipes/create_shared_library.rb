#
# Cookbook:: was_master
# Recipe:: create_shared_library
#
# Copyright:: 2018, The Authors, All Rights Reserved.


wsadmin 'Create Shared Library' do
  script_path File.join( node[:was][:jython_path], 'crtSharedLib.py' )
  script_options "\"#{node['was']['library_scope']}\" \"#{node['was']['node_name']}\" \"#{node['was']['server_or_cluster_name']}\" \"#{node['was']['shared_library_name']}\" \"#{node['was']['shared_library_classpath']}\" \"#{node['was']['shared_library_description']}\" \"#{node['was']['native_library_path']}\" \"#{node['was']['isolated_class_loader']}\" \"YES\""
end
