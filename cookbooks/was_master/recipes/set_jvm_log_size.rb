#
# Cookbook:: was_master
# Recipe:: set_jvm_log_size
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# depends on install_jython_scripts

wsadmin 'Set JVM Log Size' do
  script_path File.join( node[:was][:jython_path], 'setJVMLogSize.py' )
  script_options "\"#{node['was']['node_name']}\" \"#{node['was']['server_name']}\" \"#{node['was']['log_name']}\" \"#{node['was']['log_size']}\" \"#{node['was']['max_logs_to_keep']}\" \"YES\""
end
