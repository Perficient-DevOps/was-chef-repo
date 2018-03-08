

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

#cluster operations
default['was']['create_cluster_name'] = 'TestCluster2'

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

default['was']['jvm_arguments']  = '[-Dsun.net.http.allowRestrictedHeaders=true -Dlog4j.configuration=file:/opt/IBM/BPM/rybalog4j.xml]'

default['was']['jvm_gc']  = '-Xgcpolicy:gencon'
default['was']['jvm_rm_gc'] = ''

default['was']['jvm_property'] = 'jvmPropertyName'
default['was']['jvm_property_value'] = 'jvmPropertyValue'

default['was']['jaas_alias_name'] = 'myAlias'
default['was']['jaas_object_username'] = 'JaasUserName'
default['was']['jaas_object_password'] = 'JaasPassword'
default['was']['jaas_description']  = 'JaasDescription'

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

default['was']['cluster_or_server_name'] = 'MyServer'
default['was']['db_type'] = 'Oracle'
default['was']['jdbc_provider'] = 'Oracle JDBC Driver'
default['was']['data_source_implementation_type'] = 'Connection pool data source'
default['was']['provider_name'] = 'Rory Oracle Provider'
default['was']['provider_jar_path'] = '/home/wasadmin/ojdbc6.jar'
default['was']['provider_description'] = 'Cell Oracle Provider'
default['was']['provider_description_text'] = 'Oracle provider description text'
default['was']['implementation_class_name'] = 'oracle.jdbc.pool.OracleConnectionPoolDataSource'
default['was']['data_source_namespace'] = 'org.apache.derby.jdbc.EmbeddedXADataSource'
default['was']['scope_level'] = 'Cell'
default['was']['data_source_scope'] = 'Cell'
default['was']['jdbc_provider_scope'] = 'Cell'

default['was']['data_source_name']  = 'RoryOracleDataSource'
default['was']['data_source_jndi']  = 'jndi/RoryOracleDataSource'
default['was']['data_source_description']  = 'DataSource Description'
default['was']['database_path']  = '/WorkingData/webapps/Database/PLANTSDB'
default['was']['db_adapter'] = 'com.ibm.websphere.rsadapter.DerbyDataStoreHelper'

default['was']['data_source_min'] = '10' #Datasouce connection pool minimum
default['was']['data_source_max'] = '20' #Datasouce connection pool maximum

default['was']['database_url']  = 'jdbc:oracle:thin:@TXAIXEBNDBD02:1536:ECPD2X'
default['was']['data_source_helper_class'] = 'com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper'
default['was']['component_managed_persistence'] = 'true'
default['was']['container_managed_persistence'] = 'true'
default['was']['data_source_cluster_or_server'] = 'ClusterName'
