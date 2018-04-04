#
# Cookbook:: was_master
# Recipe:: install_jython_scripts
#
# Copyright:: 2018, The Authors, All Rights Reserved.

directory node['was']['jython_path'] do
  owner node[:was][:run_user]
  group node[:was][:run_group]
  mode '0755'
  action :create
  recursive true
end

node[:was][:jython_scripts].each do |current_script|
  current_script_path = File.join( node[:was][:jython_path], current_script )

  cookbook_file current_script_path do
    source current_script
    action :create
    mode "0644"
    owner node[:was][:run_user]
    group node[:was][:run_group]
  end

end
