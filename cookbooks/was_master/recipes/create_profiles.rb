#
# Cookbook:: test_websphere
# Recipe:: create_profiles
#
# Copyright:: 2018, The Authors, All Rights Reserved.


was_master_profile 'Create Dmgr profile' do
  action :create
  profile_name node[:was][:dmgr_profilename]
  profile_template_path "#{node[:was][:install_home]}/profileTemplates/cell/dmgr"
end

# Create
was_master_profile 'Create test profile' do
  action :create
  profile_name node[:was][:appsrv_profilename]
end


was_master_profile 'Delete test profile' do
  action :delete
  profile_name node[:was][:appsrv_profilename]
end

was_master_profile 'Delete Dmgr profile' do
  action :delete
  profile_name node[:was][:dmgr_profilename]
end


# Create Cluster
# Add member to cluster

# Start servers
# execute 'Start Dmgr' do
#   command "#{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}/bin/startManager.sh"
#   user node[:was][:run_user]
#   # TODO: Add guard here to avoid error with started running services
#   not_if "#{node[:was][:install_home]}/profiles/#{node[:was][:profile_name]}/bin/serverStatus.sh dmgr|grep STARTED"
# end
#
# Start servers
# execute 'Start AppServer' do
#   command "#{node[:was][:install_home]}/profiles/#{node[:was][:appsrv_profilename]}/bin/startNode.sh"
#   user node[:was][:run_user]
#   # TODO: Add guard here to avoid error with started running services
#   not_if "#{node[:was][:install_home]}/profiles/#{node[:was][:appsrv_profilename]}/bin/serverStatus.sh nodeagent| grep STARTED"
# end
