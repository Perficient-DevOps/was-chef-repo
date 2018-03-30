#
# Cookbook:: was_master
# Recipe:: prerequisites
#
# Copyright:: 2018, The Authors, All Rights Reserved.


# https://www.ibm.com/support/knowledgecenter/SSZJPZ_11.7.0/com.ibm.swg.im.iis.found.admin.common.doc/topics/appsvconfig_nonrootadmincreatnewuser.html

user node[:was][:run_user] do
  comment 'WebSphere run time user'
  home "/home/#{node[:was][:run_user]}"
  manage_home true
  shell '/bin/bash'
  password node[:was][:run_user_passwd]
end

group node[:was][:run_group] do
  action :create
  members node[:was][:run_user]
  append true
end

# Update users ulimits
# /etc/security/limits.conf
#

# FIXME: move to install recipe
execute "Update #{node[:was][:install_home]} directory ownership" do
  command "chown -R #{node[:was][:run_user]}:#{node[:was][:run_group]} #{node[:was][:install_home]}"
end

# Setup for jython scripting
include_recipe 'was_master::install_jython_scripts'
