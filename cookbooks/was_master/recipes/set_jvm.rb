#
# Cookbook Name:: was
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

temp_script= File.join( Chef::Config[:file_cache_path], 'was_jvm_update_settings.py' )

template temp_script do
  source 'was_jvm_update_settings.py.erb'
  variables({
    :profile_path => node['was']['profile_path'],
    :cell_name => node['was']['cell_name'],
    :node_name => node['was']['node_name'],
    :server_name => node['was']['server_name']
    })
  end


  execute "Update #{node['was']['server_name'] } JVM settings via wsadmin" do
   # command "#{ node['was']['profile_path'] }/bin/wsadmin.sh -lang jython -port #{ node['was']['soap_port'] } -username #{ node['was']['was_user'] } -password '#{ node['was']['was_pass'] }' -f #{temp_script}"
    command "#{ node['was']['profile_path'] }/bin/wsadmin.sh -lang jython -port #{ node['was']['soap_port'] } -f #{temp_script}"
  end
