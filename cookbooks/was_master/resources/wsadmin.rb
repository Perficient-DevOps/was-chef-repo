#
# Helper to wrap the common pattern of wsadmin usage with a scripts and options
#

resource_name :wsadmin

property :conntype, String, default: 'SOAP'
property :script_lang, String, default: 'jython'

property :script_path, String, default: ''
property :script_options, String, default: ''

action :create do
  # base command
  wsadmin_cmd  = ::File.join( node['was']['install_home'], 'bin', 'wsadmin.sh')
  # wsadmin options
  node[:was][:java_options].each do |cur_opt|
    wsadmin_cmd += " -javaoption '#{cur_opt}'"
  end

  # connection information
  wsadmin_cmd += " -conntype #{conntype} -host #{ node['was']['dmgr_host'] } -port #{ node['was']['dmgr_soap_port'] }"
  wsadmin_cmd += node[:was][:was_user] ? " -user #{node['was']['was_user']} -password '#{node['was']['was_pass']}'" : ""
  # script information
  wsadmin_cmd += " -lang #{script_lang} -f #{script_path} #{script_options}"

  execute "Run wsadmin command" do
    command wsadmin_cmd
    live_stream true
  end

end
