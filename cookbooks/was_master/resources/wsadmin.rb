#
# Helper to wrap the common pattern of wsadmin usage with a scripts and options
#

resource_name :wsadmin

property :conntype, String, default: 'SOAP'
property :script_lang, String, default: 'jython'

property :script_name, String, default: ''
property :script_options, String, default: ''


action :create do
  script_temp_path = ::File.join( Chef::Config[:file_cache_path], 'scripts')
  script_path = ::File.join( script_temp_path, script_name)
  # base command
  wsadmin_cmd  = ::File.join( node['was']['install_home'], 'bin', 'wsadmin.sh')
  # wsadmin options
  wsadmin_cmd += " -javaoption '#{node['was']['java_option_first']}' -javaoption '#{node['was']['java_option_second']}'"
  # connection information
  wsadmin_cmd += " -conntype #{conntype} -host #{ node['was']['host'] } -port #{ node['was']['soap_port'] }"
  wsadmin_cmd += node[:was][:was_user] ? "-user #{node['was']['was_user']} -password '#{node['was']['was_pass']}'" : ""
  # script information
  wsadmin_cmd += " -lang #{script_lang} -f #{script_path} #{script_options}"

  directory script_temp_path do
    owner node[:was][:run_user]
    group node[:was][:run_group]
    mode '0755'
    action :create
    recursive true
  end

  cookbook_file script_path do
    source script_name
    owner node[:was][:run_user]
    group node[:was][:run_group]
    mode '0755'
    action :create
  end

  execute "Run wsadmin command" do
    command wsadmin_cmd
  end

end
