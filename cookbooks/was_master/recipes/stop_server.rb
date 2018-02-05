#
# Cookbook Name:: was
# Recipe:: default
#
# Copyright (c) 2018 The Authors, All Rights Reserved.

execute "Stopping Server #{ node['was']['server_name']} " do
  command "#{ node['was']['profile_path'] }/bin/stopServer.sh #{ node['was']['server_name']} -profileName #{node['was']['profile_name']}"
end
