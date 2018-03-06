default['was']['db_name'] = 'Derby'
default['was']['jdbc_provider'] = 'Derby JDBC Provider'
default['was']['data_source_implementation_provider'] = 'XA data source'
default['was']['provider_name'] = 'Bruce Plants Provider'
default['was']['provider_jar_path'] = '/opt/IBM/WebSphere/AppServer/derby/lib/derby.jar'
default['was']['provider_description'] = 'description'
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
