#
# Cookbook Name:: start_server
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.
execute "Starting Server #{ node['start_server']['server_name']} " do
  command "#{ node['start_server']['profile_path'] }/bin/startServer.sh #{ node['start_server']['server_name']} -profileName #{node['start_server']['profile_name']}"
end
