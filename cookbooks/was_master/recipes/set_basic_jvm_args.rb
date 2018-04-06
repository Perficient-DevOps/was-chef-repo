#
# Cookbook:: was_master
# Recipe:: set_basic_jvm_props
#
# Copyright:: 2018, The Authors, All Rights Reserved.

wsadmin 'Set Generic JVM Arguments' do
  script_path File.join( node[:was][:jython_path], 'setJVMGenArgs.py' )
  script_options "\"#{node['was']['node_name']}\" \"#{node['was']['server_name']}\" \"#{node['was']['jvm_arguments']}\" \"YES\""
end
