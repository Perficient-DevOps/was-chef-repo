#
# Cookbook Name:: stop_server
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

execute "Stopping Server #{ node['stop_server']['server_name']} " do
  command "#{ node['stop_server']['profile_path'] }/bin/stopServer.sh #{ node['stop_server']['server_name']} -profileName #{node['stop_server']['profile_name']}"
end
