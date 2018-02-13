default['was']['run_user']      = 'wasadmin'
default['was']['run_group']     = 'wasadmin'
default['was']['run_user_passwd'] = '$ecret!'

default['was']['dmgr_profile_name'] = 'Dmgr01'
default['was']['profile_name']  = 'DevDmgr'
default['was']['install_home']  = '/opt/IBM/WebSphere/AppServer/'

default['was']['cell_name']     = 'STLSCVMG95219Cell01'
default['was']['dmgr_node_name'] = 'DmgrNode'
default['was']['node_name']     = 'STLSCVMG95218Node02'
default['was']['server_name']   = 'rory'
default['was']['was_user']      = 'wasadmin'
default['was']['was_pass']      = 'adminwas'
default['was']['soap_port']     = '10003'
default['was']['host']          = 'STLSCVMG95219'
default['was']['jython_path']   = '/WorkingData/chef-repo/was-chef-repo/jythonScripts/'
default['was']['server_min_heap']     = '64'
default['was']['server_max_heap']     = '128'

#JDBC Attributes
default['was']['cluster'] = 'DevCluster'
default['was']['db_name'] = 'Derby'
default['was']['jdbc_provider'] = 'Derby JDBC Provider'
default['was']['data_source_implementation_provider'] = 'XA data source'
default['was']['provider_name'] = 'Bruce Provider'
default['was']['provider_jar_path'] = '/opt/IBM/WebSphere/AppServer/derby/lib/derby.jar'
default['was']['provider_description'] = 'description'
default['was']['data_source_namespace'] = 'org.apache.derby.jdbc.EmbeddedXADataSource'
default['was']['scope_level'] = 'Cluster'

default['was']['data_source_name']  = 'PlantsByWebSphereDataSource'
default['was']['data_source_jndi']  = 'jndi/PlantsByWebSphereDataSource'
default['was']['data_source_description']  = 'DataSource Description'
default['was']['database_path']  = '/WorkingData/webapps/Database/PLANTSDB'

default['was']['profile_path']  = File.join( node['was']['install_home'], 'profiles', node['was']['profile_name'] )
