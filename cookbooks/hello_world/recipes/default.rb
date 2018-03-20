#
# Cookbook:: hello_world
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.
file "#{ENV[‘HOME’]}/x.txt" do
content ‘HELLO WORLD’
end
