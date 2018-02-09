default['was']['profile_name']  = 'DevDmgr'
default['was']['install_home']  = '/opt/IBM/WebSphere/AppServer/'

default['was']['cell_name']     = 'STLSCVMG95219Cell01'
default['was']['node_name']     = 'STLSCVMG95218Node02'
default['was']['server_name']   = 'rory'
default['was']['was_user']	= 'wasadmin'
default['was']['was_pass']	 = 'adminwas'
default['was']['soap_port']     = '10003'
default['was']['host']          = 'STLSCVMG95219'
default['was']['jython_path']   = '/WorkingData/chef-repo/was-chef-repo/jythonScripts/'
default['was']['server_min_heap']     = '64'
default['was']['server_max_heap']     = '128'

default['was']['profile_path']  = File.join( node['was']['install_home'], 'profiles', node['was']['profile_name'] )
