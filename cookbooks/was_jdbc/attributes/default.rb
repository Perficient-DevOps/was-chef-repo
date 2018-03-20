default['was']['db_type'] = 'Oracle'
default['was']['jdbc_provider'] = 'Oracle JDBC Driver'
default['was']['data_source_implementation_type'] = 'Connection pool data source'
default['was']['provider_name'] = 'Bruce Plants Provider'
default['was']['provider_jar_path'] = '/home/wasadmin/ojdbc6.jar'
default['was']['provider_description'] = 'Cell Oracle Provider'
default['was']['provider_description_text'] = 'Oracle provider description text'
default['was']['implementation_class_name'] = 'oracle.jdbc.pool.OracleConnectionPoolDataSource'
default['was']['data_source_namespace'] = 'org.apache.derby.jdbc.EmbeddedXADataSource'
default['was']['scope_level'] = 'Cell'
default['was']['data_source_scope'] = 'Cell'
default['was']['jdbc_provider_scope'] = 'Cell'

default['was']['data_source_name']  = 'PlantsByWebSphereDataSource'
default['was']['data_source_jndi']  = 'jndi/PlantsByWebSphereDataSource'
default['was']['data_source_description']  = 'DataSource Description'
default['was']['database_path']  = '/WorkingData/webapps/Database/PLANTSDB'
default['was']['db_adapter'] = 'com.ibm.websphere.rsadapter.DerbyDataStoreHelper'

default['was']['data_source_min'] = '10' #Datasouce connection pool minimum
default['was']['data_source_max'] = '20' #Datasouce connection pool maximum

default['was']['database_url']  = 'jdbc:oracle:thin:@TXAIXEBNDBD02:1536:ECPD2X'
default['was']['data_source_helper_class'] = 'com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper'
default['was']['container_managed_persistence'] = 'true'
default['was']['data_source_cluster'] = 'ClusterName'
