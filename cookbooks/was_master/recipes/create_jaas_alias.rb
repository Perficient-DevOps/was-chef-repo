#
# Cookbook:: was_master
# Recipe:: create_jaas_alias
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# Wrapper script options:
#   "myName" "userName" "mypassword" "my description"

wsadmin 'Create JAAS Alias' do
  script_path File.join( node[:was][:jython_path], 'crtJAASAlias.py' )
  script_options "\"#{node['was']['jaas_alias_name']}\" \"#{node['was']['jaas_object_username']}\" \"#{node['was']['jaas_object_password']}\" \"#{node['was']['jaas_description']}\" \"YES\""
  not_if { ::File.readlines( "#{node['was']['install_home']}profiles/#{node['was']['dmgr_profile_name']}/config/cells/#{node['was']['cell_name']}/security.xml").grep("#{node['was']['jaas_alias_name']}").empty? }
end
