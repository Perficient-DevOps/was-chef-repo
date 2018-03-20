#These values are test values and only appy to the Perficient internal environment
#All of these values should be overridden by the JSON passed into UCD

#was855 base values used across multiple recipes
default['was']['install_home']  = '/opt/IBM/WebSphere/AppServer/'
default['was']['dmgr_profile_name'] = 'Dmgr01'
default['was']['dmgr_node_name'] = 'DmgrNode'
default['was']['soap_port']     = '10003'
default['was']['profile_name']  = 'DevDmgr'
default['was']['node_name']     = 'STLSCVMG95218Node02'
default['was']['was_user']      = 'wasadmin'
default['was']['was_pass']      = 'adminwas'

#was9 values
# default['was']['install_home']  = '/opt/IBM/WAS9/WebSphere/Appserver/'
# default['was']['dmgr_profile_name'] = 'Dev9Dev'
# default['was']['dmgr_node_name'] = 'Dev9Node1'
# default['was']['soap_port']     = '13003'
# default['was']['profile_name']  = 'Dev9Node1'
# default['was']['node_name']     = 'STLSCVMG95219Node03'

#Run user and run gtoup to create temporary wasadmin scripts on the file system
default['was']['run_user']      = 'wasadmin'
default['was']['run_group']     = 'wasadmin'
default['was']['run_user_passwd'] = '$ecret!'

#cluster operations
#cluster names for specific cluster operations
default['was']['create_cluster_name'] = 'TestCluster2'
default['was']['cluster_first_node_name'] = 'STLSCVMG95219Node01'
default['was']['cluster_first_member_name'] = 'ClusterServerEin'
default['was']['cluster_subsequent_node_name'] = 'STLSCVMG95218Node02'
default['was']['cluster_subsequent_member_name'] = 'ClusterServerZwei'

# Create generic App Server
#create_was_server recipe
default['was']['server_name']   = 'rory' #Server to be created
#cluster and cell names for standalone server operations
default['was']['cell_name']     = 'STLSCVMG95219Cell01'
default['was']['cluster'] = 'DevCluster'

default['was']['host']          = 'STLSCVMG95219'#DMgr Hostname for SOAP Commands

# This path need not change per environment, it should remain the same
default['was']['jython_path']   = "#{ Chef::Config[:file_cache_path] }/jythonScripts"
#Profile path is used by the generic create server recipe
default['was']['profile_path']  = File.join( node['was']['install_home'], 'profiles', node['was']['profile_name'] )

#set_jvm_heap recipe
default['was']['server_min_heap']     = '64'
default['was']['server_max_heap']     = '128'

#set_basic_jvm_args recipe
default['was']['jvm_arguments']  = '[-Dsun.net.http.allowRestrictedHeaders=true -Dlog4j.configuration=file:/opt/IBM/BPM/rybalog4j.xml]'

#set_jvm_garbage_collection recipe
default['was']['jvm_gc']  = '-Xgcpolicy:gencon' #Set garbage collection
default['was']['jvm_rm_gc'] = '' #remove garbage collection

#set_jvm_custom_props recipe
default['was']['jvm_property'] = 'jvmPropertyName'
default['was']['jvm_property_value'] = 'jvmPropertyValue'

#set_jvm_log_size recipe
default['was']['log_name'] = 'outputStreamRedirect' #This is for stdOut, stdErr value should be errorStreamRedirect
default['was']['log_size'] = '5'
default['was']['max_logs_to_keep'] = '5'

#create_jaas_alias recipe
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

#set_server_jdk recipe
default['was']['jdk_version'] = '1.7.1_64'

#Below attributes apply to datasouce and provider recipes
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


default['was']['database_url']  = 'jdbc:oracle:thin:@TXAIXEBNDBD02:1536:ECPD2X'
default['was']['data_source_helper_class'] = 'com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper'
default['was']['component_managed_persistence'] = 'true'
default['was']['container_managed_persistence'] = 'true'
default['was']['data_source_cluster_or_server'] = 'ClusterName'

#Below attributes apply to datasource connection pool recipe
default['was']['data_source_min'] = '10' #Datasouce connection pool minimum
default['was']['data_source_max'] = '20' #Datasouce connection pool maximum
default['was']['reap_time'] = '60'
default['was']['unused_timeout']  = '60'
default['was']['aged_timeout']  = '60'
default['was']['purge_policy']  = 'FailingConnectionOnly'

#create shared library recipes
default['was']['library_scope'] = 'Cell'
default['was']['server_or_cluster_name'] = 'STLSCVMG95219Node01' #NOTE: If you specify Cell level scope, then use ‘none’ for node and server/cluster parmaters.
#NOTE: If you specify Node level scope, then use ‘none’ value for server/cluster parameter.
#NOTE: If you specify Cluster scope, then use ‘none’ values for node name and server/cluster parameters.
default['was']['shared_library_name'] = 'somelibraryname'
default['was']['shared_library_classpath'] = 'somelib.zip'
default['was']['shared_library_description'] = 'My Shared Library Description'
default['was']['native_library_path'] = 'none' #if specified otherwise none.
default['was']['isolated_class_loader'] = 'true' #or false

#create_jndi_namespace_binding
default['was']['jndi_scope'] = 'Cell'
default['was']['binding_identifier'] = ''
default['was']['name_in_space'] = 'spaceBind'
default['was']['string_value'] = 'false'

#backup_config
default['was']['backup_path'] = '/WorkingData/backupConfig/DevDmgr'

#wasadmin JVM Size for all recipes using wasadmin
default['was']['jvm_size'] = '-javaoption –Xms512m –Xmx1024m'
