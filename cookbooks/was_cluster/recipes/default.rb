#
# Cookbook:: was_cluster
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.

include_recipe 'was_master::create_was_cluster'
include_recipe 'was_master::create_first_was_cluster_member'
include_recipe 'was_master::create_additional_was_cluster_member'
include_recipe 'was_master::start_was_cluster'
