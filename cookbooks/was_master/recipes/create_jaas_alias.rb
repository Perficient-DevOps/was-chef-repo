#
# Cookbook:: was_master
# Recipe:: create_jaas_alias
#
# Copyright:: 2018, The Authors, All Rights Reserved.
jython_script_name = 'crtJAASAlias.py'


wsadmin 'Create JAAS Alias' do
  script_path File.join( node[:was][:jython_path], 'crtJAASAlias.py' )
  script_options "\"#{node['was']['jaas_alias_name']}\" \"#{node['was']['jaas_object_username']}\" \"#{node['was']['jaas_object_password']}\" \"#{node['was']['jaas_description']}\" \"YES\""
end

#"myName" "userName" "mypassword" "my description"
