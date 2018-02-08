#
# Cookbook Name:: was
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

#temp_script= File.join( Chef::Config[:file_cache_path], 'was_jvm_update_settings.py' )

#template temp_script do
#  source 'was_jvm_update_settings.py.erb'
#  variables({
#    :profile_path => node['was']['profile_path'],
#    :cell_name => node['was']['cell_name'],
#    :server_name => node['was']['server_name']
#    })
#  end


execute "Run Jython" do
  command "#{node['was']['install_home']}bin/wsadmin.sh -conntype SOAP -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] } -lang jython -user #{node['was']['was_user']} -password #{node['was']['was_pass']} -f #{node['was']['jython_path']}setJVMHeap.py \"#{node['was']['node_name']}\" \"#{node['was']['server_name']}\" \"#{node['was']['server_min_heap']}\" \"#{node['was']['server_max_heap']}\" \"YES\""
end
