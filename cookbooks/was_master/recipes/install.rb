#
# Cookbook:: was_master
# Recipe:: install
#
# Copyright:: 2018, The Authors, All Rights Reserved.

template_source = 'silent-install.xml'
template_file= File.join( Chef::Config[:file_cache_path], template_source )

template template_file do
  source "#{ template_source }.erb"
  variables({
    :shared_location    => node[:was][:shared_location],
    :install_repo       => node[:was][:install_repo],
    :profile_name       => node[:was][:install_profilename],
    :install_location   => node[:was][:install_home],
    :install_arch       => node[:was][:install_arch],
    :profile_id         => node[:was][:profile_id],
    :install_versiontag => node[:was][:install_versiontag]
    })
  end

execute "Perform silent installation of WebSphere" do
# FIXME: This should be a requirement on another cookbook to install IM and provide this variable
  command "/opt/IBM/InstallationManager/eclipse/tools/imcl -acceptLicense -showVerboseProgress input #{template_file}"
  not_if { ::File.exist?( "#{node[:was][:install_location]}" ) }
end

# FIXME: This is not working as expected?
# Ensure that directory ownership is correct
# directory node[:was][:install_location] do
#   action :create
#   recursive true
#   owner node[:test_webspher`e][:run_user]
#   group node[:was][:run_group]
# end

execute "Update #{node[:was][:install_location]} directory ownership" do
  command "chown -R #{node[:was][:run_user]}:#{node[:was][:run_group]} #{node[:was][:install_location]}"
end

# Add .../AppServer/bin directory to run_user's path
# TODO:
