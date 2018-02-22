#
# Cookbook:: was_cluster
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.

include_recipe 'was_master::create_was_cluster'
include_recipe 'was_master::create_was_cluster_member_first'
include_recipe 'was_master::create_was_cluster_member'
