#
# Cookbook:: nrg_websphere
# Recipe:: test_create_base_environment
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# Verify we can run commands
execute 'Run a test command' do
  command "#{node[:was][:install_home]}/bin/versionInfo.sh"
  user node[:was][:run_user]
end

execute 'Create Deployment Manager profile' do
  command "#{node[:was][:install_home]}/bin/manageprofiles.sh -create -profileName #{ node[:was][:dmgr_profile_name] } -startingPort #{ node[:was][:dmgr_starting_port]} -adminUserName #{ node[:was][:was_user] } -adminPassword '#{ node[:was][:was_pass] }' -cellName #{ node[:was][:cell_name] } -enableAdminSecurity true -nodeName #{ node[:was][:dmgr_node_name] } -templatePath dmgr -serverName #{ node[:was][:dmgr_server_name] }"
  user node[:was][:run_user]
  not_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{node['was']['dmgr_profile_name'] }" ) }
end

execute 'Start Deployment Manager' do
  command "#{node[:was][:install_home]}/profiles/#{node[:was][:dmgr_profile_name]}/bin/startManager.sh"
  user node[:was][:run_user]
  # TODO: Add guard here to avoid error with started running services
  not_if "#{node[:was][:install_home]}/profiles/#{node[:was][:dmgr_profile_name]}/bin/serverStatus.sh dmgr -username #{ node[:was][:was_user] } -password '#{ node[:was][:was_pass] }'|grep STARTED"
end

node[:was][:nodes].each do |cur_node|

  execute "Create #{cur_node[:profile_name]} Profile" do
    command "#{node[:was][:install_home]}/bin/manageprofiles.sh -create -profileName #{cur_node[:profile_name]} -templatePath managed -nodeName #{cur_node[:node_name]}"
    user node[:was][:run_user]
    not_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{cur_node[:profile_name]}" ) }
  end

  execute "Federate #{cur_node[:profile_name]}" do
    command "#{node[:was][:install_home]}/bin/addNode.sh #{ node[:was][:dmgr_host]} #{ node[:was][:dmgr_soap_port]} -profileName #{cur_node[:profile_name]} -startingport #{cur_node[:starting_port]} -username #{ node[:was][:was_user] } -password '#{ node[:was][:was_pass] }' "
    user node[:was][:run_user]
    not_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{ node[:was][:dmgr_profile_name]}/config/cells/#{ node[:was][:cell_name]}/nodes/#{cur_node[:node_name]}" ) }
    # TODO: Convert to a better test in the future
    #   export profile_name=Node1
    #  ./wsadmin.sh -profileName $profile_name -username wasadmin -password 'adminwas' -c 'set servers [$AdminConfig list Server]; foreach s $servers { if { [$AdminConfig showAttribute $s serverType]=="NODE_AGENT" } { puts $s; puts NODE_AGENT }  }'
    # end
  end

end # end nodes loop
