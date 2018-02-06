#
# Cookbook:: test_websphere
# Recipe:: setup_user
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# https://www.ibm.com/support/knowledgecenter/SSZJPZ_11.7.0/com.ibm.swg.im.iis.found.admin.common.doc/topics/appsvconfig_nonrootadmincreatnewuser.html

user node[:test_websphere][:run_user] do
  comment 'WebSphere run time user'
  home "/home/#{node[:test_websphere][:run_user]}"
  manage_home true
  shell '/bin/bash'
  password node[:test_websphere][:run_user_passwd]
end

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
