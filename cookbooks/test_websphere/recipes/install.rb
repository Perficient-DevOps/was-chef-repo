#
# Cookbook:: test_websphere
# Recipe:: install
#
# Copyright:: 2018, The Authors, All Rights Reserved.




group node[:test_websphere][:run_group] do
  action :create
  members node[:test_websphere][:run_user]
  append true
end

# Ensure that directory ownership is correct
directory node[:test_websphere][:install_path] do
  action :create
  owner node[:test_websphere][:run_user]
  owner node[:test_websphere][:run_group]
end
