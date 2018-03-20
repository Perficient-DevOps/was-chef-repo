#
# Cookbook:: was_jdbc
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.


include_recipe 'was_master::set_jdbc_provider'
include_recipe 'was_master::set_jdbc_datasource'
