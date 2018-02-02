#
# Cookbook Name:: set_jvm
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

temp_script= File.join( Chef::Config[:file_cache_path], 'was_jvm_update_settings.py' )

template temp_script do
  source 'was_jvm_update_settings.py.erb'
  variables({
    :profile_path => node['set_jvm']['profile_path'],
    :cell_name => node['set_jvm']['cell_name'],
    :node_name => node['set_jvm']['node_name'],
    :server_name => node['set_jvm']['server_name']
    })
  end


  execute "Update #{node['set_jvm']['server_name'] } JVM settings via wsadmin" do
   # command "#{ node['set_jvm']['profile_path'] }/bin/wsadmin.sh -lang jython -port #{ node['set_jvm']['soap_port'] } -username #{ node['set_jvm']['was_user'] } -password '#{ node['set_jvm']['was_pass'] }' -f #{temp_script}"
    command "#{ node['set_jvm']['profile_path'] }/bin/wsadmin.sh -lang jython -port #{ node['set_jvm']['soap_port'] } -f #{temp_script}"
  end

