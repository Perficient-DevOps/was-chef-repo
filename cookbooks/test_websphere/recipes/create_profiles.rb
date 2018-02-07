#
# Cookbook:: test_websphere
# Recipe:: create_profiles
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# Verify we can run commands
execute 'Run a test command' do
  command "#{node[:test_websphere][:install_location]}/bin/versionInfo.sh"
  user node[:test_websphere][:run_user]
end

execute 'create Dmgr profile' do
  command "#{node[:test_websphere][:install_location]}/bin/manageprofiles.sh -create -templatePath #{node[:test_websphere][:install_location]}/profileTemplates/cell/dmgr -nodeProfilePath #{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:appsrv_profilename]} -profileName #{node[:test_websphere][:dmgr_profilename]} -cellName #{node[:test_websphere][:cell_name]} -nodeName #{node[:test_websphere][:dmgr_node_name]} -appServerNodeName #{node[:test_websphere][:appsrv_node_name]}"
  user node[:test_websphere][:run_user]
  not_if { ::File.exist?( "#{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:dmgr_profilename]}" ) }
end

execute 'create Application Server profile' do
  command "#{node[:test_websphere][:install_location]}/bin/manageprofiles.sh -create -templatePath #{node[:test_websphere][:install_location]}/profileTemplates/cell/default -dmgrProfilePath #{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:dmgr_profilename]} -portsFile #{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:dmgr_profilename]}/properties/portdef.props -nodePortsFile #{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:dmgr_profilename]}/properties/nodeportdef.props -profileName #{node[:test_websphere][:appsrv_profilename]} -cellName #{node[:test_websphere][:cell_name]} -nodeName #{node[:test_websphere][:dmgr_node_name]} -appServerNodeName #{node[:test_websphere][:appsrv_node_name]}"
  user node[:test_websphere][:run_user]
  not_if { ::File.exist?( "#{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:appsrv_profilename]}" ) }
end

# Start servers
execute 'Start Dmgr' do
  command "#{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:dmgr_profilename]}/bin/startManager.sh"
  user node[:test_websphere][:run_user]
  # TODO: Add guard here to avoid error with started running services
  not_if "#{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:dmgr_profilename]}/bin/serverStatus.sh dmgr|grep STARTED"
end

# Start servers
execute 'Start AppServer' do
  command "#{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:appsrv_profilename]}/bin/startNode.sh"
  user node[:test_websphere][:run_user]
  # TODO: Add guard here to avoid error with started running services
  not_if "#{node[:test_websphere][:install_location]}/profiles/#{node[:test_websphere][:appsrv_profilename]}/bin/serverStatus.sh nodeagent| grep STARTED"
end
