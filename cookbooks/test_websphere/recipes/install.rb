#
# Cookbook:: test_websphere
# Recipe:: install
#
# Copyright:: 2018, The Authors, All Rights Reserved.

template_source = 'silent-install.xml'
template_file= File.join( Chef::Config[:file_cache_path], template_source )

template template_file do
  source "#{ template_source }.erb"
  variables({
    :shared_location    => node[:test_websphere][:shared_location],
    :install_repo       => node[:test_websphere][:install_repo],
    :profile_name       => node[:test_websphere][:install_profilename],
    :install_location   => node[:test_websphere][:install_location],
    :install_arch       => node[:test_websphere][:install_arch],
    :profile_id         => node[:test_websphere][:profile_id],
    :install_versiontag => node[:test_websphere][:install_versiontag]
    })
  end

execute "Perform silent installation of WebSphere" do
# FIXME: This should be a requirement on another cookbook to install IM and provide this variable
  command "/opt/IBM/InstallationManager/eclipse/tools/imcl -acceptLicense -showVerboseProgress input #{template_file}"
  not_if { ::File.exist?( "#{node[:test_websphere][:install_location]}" ) }
end

# FIXME: This is not working as expected?
# Ensure that directory ownership is correct
# directory node[:test_websphere][:install_location] do
#   action :create
#   recursive true
#   owner node[:test_webspher`e][:run_user]
#   group node[:test_websphere][:run_group]
# end

execute "Update #{node[:test_websphere][:install_location]} directory ownership" do
  command "chown -R #{node[:test_websphere][:run_user]}:#{node[:test_websphere][:run_group]} #{node[:test_websphere][:install_location]}"
end

# Add .../AppServer/bin directory to run_user's path
# TODO:
