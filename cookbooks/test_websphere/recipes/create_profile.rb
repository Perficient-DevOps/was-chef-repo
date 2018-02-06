

execute 'create Dmgr profile' do
  command "#{node[:test_websphere][:install_path]}/bin/manageprofiles.sh -create -templatePath #{node[:test_websphere][:install_path]}/profileTemplates/cell/dmgr -nodeProfilePath #{node[:test_websphere][:install_path]}/profiles/#{node[:test_websphere][:appsrv_profilename]} -profileName #{node[:test_websphere][:dmgr_profilename]} -cellName #{node[:test_websphere][:cell_name]} -nodeName #{node[:test_websphere][:dmgr_node_name]} -appServerNodeName #{node[:test_websphere][:appsrv_node_name]}"
  user node[:test_websphere][:run_user]
  not_if { ::File.exist?( "#{node[:test_websphere][:install_path]}/profiles/#{node[:test_websphere][:dmgr_profilename]}" ) }
end

execute 'create Application Server profile' do
  command "#{node[:test_websphere][:install_path]}/bin/manageprofiles.sh -create -templatePath #{node[:test_websphere][:install_path]}/profileTemplates/cell/default -dmgrProfilePath #{node[:test_websphere][:install_path]}/profiles/#{node[:test_websphere][:dmgr_profilename]} -portsFile #{node[:test_websphere][:install_path]}/profiles/#{node[:test_websphere][:dmgr_profilename]}/properties/portdef.props -nodePortsFile #{node[:test_websphere][:install_path]}/profiles/#{node[:test_websphere][:dmgr_profilename]}/properties/nodeportdef.props -profileName #{node[:test_websphere][:appsrv_profilename]} -cellName #{node[:test_websphere][:cell_name]} -nodeName #{node[:test_websphere][:dmgr_node_name]} -appServerNodeName #{node[:test_websphere][:appsrv_node_name]}"
  user node[:test_websphere][:run_user]
  not_if { ::File.exist?( "#{node[:test_websphere][:install_path]}/profiles/#{node[:test_websphere][:appsrv_profilename]}" ) }
end
