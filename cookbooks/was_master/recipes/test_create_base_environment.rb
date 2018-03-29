#
# Cookbook:: test_websphere
# Recipe:: create_profiles
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# Verify we can run commands
execute 'Run a test command' do
  command "#{node[:was][:install_home]}/bin/versionInfo.sh"
  user node[:was][:run_user]
end

execute 'create Dmgr profile' do
  command "#{node[:was][:install_home]}/bin/manageprofiles.sh -create -templatePath #{node[:was][:install_home]}/profileTemplates/cell/dmgr -nodeProfilePath #{node[:was][:install_home]}/profiles/#{node[:was][:appsrv_profilename]} -profileName #{node[:was][:dmgr_profile_name]} -cellName #{node[:was][:cell_name]} -nodeName #{node[:was][:dmgr_node_name]} -appServerNodeName #{node[:was][:node_name]}"
  #command "#{node[:was][:install_home]}/bin/manageprofiles.sh -create -templatePath #{node[:was][:install_home]}/profileTemplates/cell/dmgr -nodeProfilePath #{node[:was][:install_home]}/profiles/#{node[:was][:appsrv_profilename]} -profileName #{node[:was][:profile_name]} -cellName #{node[:was][:cell_name]} -nodeName #{node[:was][:dmgr_node_name]} -appServerNodeName #{node[:was][:node_name]}"
  user node[:was][:run_user]
  not_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}" ) }
end

# execute 'create Application Server profile' do
#   command "#{node[:was][:install_home]}/bin/manageprofiles.sh -create -templatePath #{node[:was][:install_home]}/profileTemplates/cell/default -dmgrProfilePath #{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]} -portsFile #{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}/properties/portdef.props -nodePortsFile #{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}/properties/nodeportdef.props -profileName #{node[:was][:appsrv_profilename]} -cellName #{node[:was][:cell_name]} -nodeName #{node[:was][:dmgr_node_name]} -appServerNodeName #{node[:was][:appsrv_node_name]}"
#   user node[:was][:run_user]
#   not_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}" ) }
# end

# Create Cluster
# Add member to cluster


# Start servers
execute 'Start Dmgr' do
  command "#{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}/bin/startManager.sh"
  user node[:was][:run_user]
  # TODO: Add guard here to avoid error with started running services
  not_if "#{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}/bin/serverStatus.sh dmgr|grep STARTED"
end

# Start servers
# execute 'Start AppServer' do
#   command "#{node[:was][:install_home]}/profiles/#{node[:was][:appsrv_profilename]}/bin/startNode.sh"
#   user node[:was][:run_user]
#   # TODO: Add guard here to avoid error with started running services
#   not_if "#{node[:was][:install_home]}/profiles/#{node[:was][:appsrv_profilename]}/bin/serverStatus.sh nodeagent| grep STARTED"
# end
