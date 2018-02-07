#
# Cookbook Name:: start_server
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.
execute "Starting Server #{ node['was']['server_name']} " do
  command "#{ node['was']['profile_path'] }/bin/startServer.sh #{ node['was']['server_name']} -profileName #{node['was']['profile_name']}"
end
