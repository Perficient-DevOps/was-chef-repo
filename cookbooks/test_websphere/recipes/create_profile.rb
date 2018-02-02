

execute 'create Dmgr profile' do
  command "#{node[:test_websphere][:install_path]}/bin/manageprofiles.sh -create -templatePath #{node[:test_websphere][:install_path]}/profileTemplates/cell/dmgr -nodeProfilePath #{node[:test_websphere][:install_path]}/profiles/AppSrv01 -profileName Dmgr001 -cellName Default01Cell -nodeName Default01Node -appServerNodeName Default02Node"
end


execute 'create Application Server profile' do
  command "#{node[:test_websphere][:install_path]}/bin/manageprofiles.sh -create -templatePath #{node[:test_websphere][:install_path]}/profileTemplates/cell/default -dmgrProfilePath #{node[:test_websphere][:install_path]}/profiles/Dmgr001 -portsFile #{node[:test_websphere][:install_path]}/profiles/Dmgr001/properties/portdef.props -nodePortsFile #{node[:test_websphere][:install_path]}/profiles/Dmgr001/properties/nodeportdef.props -profileName AppSrv01 -cellName Default01Cell -nodeName Default01Node -appServerNodeName Default02Node"
end
