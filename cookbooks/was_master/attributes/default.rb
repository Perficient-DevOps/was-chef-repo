

#was855 values
default['was']['install_home']  = '/opt/IBM/WebSphere/AppServer/'
default['was']['dmgr_profile_name'] = 'Dmgr01'
default['was']['dmgr_node_name'] = 'DmgrNode'
default['was']['soap_port']     = '10003'
default['was']['profile_name']  = 'DevDmgr'
default['was']['node_name']     = 'STLSCVMG95218Node02'

#was9 values
# default['was']['install_home']  = '/opt/IBM/WAS9/WebSphere/Appserver/'
# default['was']['dmgr_profile_name'] = 'Dev9Dev'
# default['was']['dmgr_node_name'] = 'Dev9Node1'
# default['was']['soap_port']     = '13003'
# default['was']['profile_name']  = 'Dev9Node1'
# default['was']['node_name']     = 'STLSCVMG95219Node03'

default['was']['run_user']      = 'wasadmin'
default['was']['run_group']     = 'wasadmin'
default['was']['run_user_passwd'] = '$ecret!'

#cluster and cell names for standalone server operations
default['was']['cell_name']     = 'STLSCVMG95219Cell01'
default['was']['cluster'] = 'DevCluster'

# App Server

default['was']['server_name']   = 'rory' #Server to be created
default['was']['was_user']      = 'wasadmin'
default['was']['was_pass']      = 'adminwas'
default['was']['host']          = 'STLSCVMG95219'#DMgr Hostname for SOAP Commands

# FIXME: This should not exist
default['was']['jython_path']   = "#{ Chef::Config[:file_cache_path] }/jythonScripts"

# which server is this for
default['was']['server_min_heap']     = '64'
default['was']['server_max_heap']     = '128'

default['was']['jvm_properties']  = '[-Dsun.net.http.allowRestrictedHeaders=true -Dlog4j.configuration=file:/opt/IBM/BPM/rybalog4j.xml]'

#Set Virtual Host
default['was']['virtual_host_name'] = 'default_host'
default['was']['virtual_host_port'] = '2323'
default['was']['host_name'] = 'MyHost'

#Change Server ports
default['was']['change_port_server_name'] = 'rory'
default['was']['change_port_node_name'] = 'STLSCVMG95218Node02'
default['was']['start_port']  = '15001'

default['was']['jdk_version'] = '1.7.1_64'

default['was']['profile_path']  = File.join( node['was']['install_home'], 'profiles', node['was']['profile_name'] )
