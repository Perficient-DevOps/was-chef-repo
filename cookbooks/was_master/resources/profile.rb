#
#
# WebSphere manageprofiles command reference
# https://www.ibm.com/support/knowledgecenter/en/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/rxml_manageprofiles.html

property :profile_name, String, default: '', required: true
property :profile_path, String, default: '', required: false
property :profile_template_path, String, default: '', required: false


action :create do

  template ::File.join( Chef::Config[:file_cache_path], 'manage_profiles_wrapper.sh' ) do
    action :create
    source 'create_profile.sh.erb'
    owner node[:was][:run_user]
    group node[:was][:run_group]
    mode 0755
    variables ({
      :was_home     => node[:was][:install_home],
      :profile_name => profile_name,
      :profile_path => profile_path,
      :profile_template_path => profile_template_path
      })
  end

  execute 'Create WebSphere Profile' do
    command ::File.join( Chef::Config[:file_cache_path], 'manage_profiles_wrapper.sh' )
    user node[:was][:run_user]
    not_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{profile_name}" ) }
  end

end


action :delete do

  template ::File.join( Chef::Config[:file_cache_path], 'manage_profiles_wrapper.sh' ) do
    action :create
    source 'delete_profile.sh.erb'
    owner node[:was][:run_user]
    group node[:was][:run_group]
    mode 0755
    variables ({
      :was_home     => node[:was][:install_home],
      :profile_name => profile_name
      })
  end

  execute 'Delete WebSphere Profile' do
    command ::File.join( Chef::Config[:file_cache_path], 'manage_profiles_wrapper.sh' )
    #user node[:was][:run_user]
    group node[:was][:run_group]
    only_if { ::File.exist?( "#{node[:was][:install_home]}/profiles/#{profile_name}" ) }
  end

  directory "#{node[:was][:install_home]}/profiles/#{profile_name}" do
    action :delete
    recursive true
  end

end
