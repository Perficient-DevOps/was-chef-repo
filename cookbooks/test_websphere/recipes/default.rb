#
# Cookbook:: test_websphere
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.


include_recipe "test_websphere::prerequisites"

include_recipe "test_websphere::install"

include_recipe "test_websphere::create_profiles"
