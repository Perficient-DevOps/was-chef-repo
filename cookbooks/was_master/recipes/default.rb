#
# Cookbook:: was_master
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.

include_recipe "was_master::create_was_server"

include_recipe "was_master::start_was_server"

include_recipe "was_master::set_jvm_heap"

include_recipe "was_master::stop_was_server"

include_recipe "was_master::delete_was_server"
