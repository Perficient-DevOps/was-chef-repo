
def createDatasource(clusterName, jdbcProviderName, \
		     dbAlias, dsName, dsJNDIName, dsDescription, dsHelperClass,dsMangPer,dbName,dsScope, \
		     providerScope,dbCMgrPers, nodeNameDS, debug):
	
	if debug == "YES":
		print "Creating datasource:", dsName
	#endIf
	# check and see what type of scope is on the provider so that we can do a getId against it.  
	## need to build out the containment path
	cell = AdminControl.getCell()
	if providerScope == "Cell":
		print "cell scope for provider"
		#cell = AdminControl.getCell()
		proScopeValue = "/Cell:" + cell
		if debug == "YES":
			print "We have a provider at the Cell level = ", proScopeValue
		#endIf
	#endIF
	elif  providerScope == "Cluster":
		proScopeValue = "/Cell:" + cell + "/ServerCluster:" + clusterName
		if debug == "YES":
			print "We have a provider at the Cluster level = ", proScopeValue
		#endIf
	elif  providerScope == "Node":
		proScopeValue = "/Cell:" + cell + "/Node:" + nodeNameDS
		if debug == "YES":
			print "We have a provider at the Node level = ", proScopeValue
		#endIf
	elif  providerScope == "Server":
		proScopeValue = "/Cell:" + cell + "/Node:" + nodeNameDS + "/Server:" + clusterName
		if debug == "YES":
			print "We have a provider at the Server level = ", proScopeValue
		#endIf
	else:
		print "undefined scope for the provider"
	#endIfElse
	
	
	# Compose datasource atributes variable
	dsAttrs = " -name " + "\"" + dsName + "\"" +  " -description " + "\"" +dsDescription + "\"" 
	if debug == "YES":
		print "dsAttrs values are ==",dsAttrs
	#EndIf
	
	# Create JNDI Name parameter
	jndiAttrs = " -jndiName " + dsJNDIName
	if debug == "YES":
		print "jndsAttrs values are==",jndiAttrs
	#EndIf
	
	# Create datasource helper class name parmeter
	dbHelperClass = " -dataStoreHelperClassName " + dsHelperClass
	if debug == "YES":
		print "dbHelperClass values are==", dbHelperClass
	#EndIf
	
	# Create authorization alias parameter
	dbAuthAlias = " -componentManagedAuthenticationAlias " + dbAlias
	if debug == "YES":
		print "component managedauthenticationalias = ",dbAuthAlias
	#EndIf
	
	dbContMgrPersist =" -containerManagedPersistence " + dbCMgrPers
	if debug == "YES":
		print "container managed persistence = ", dbContMgrPersist
	#EndIf
	
	#Create XA recovery alias parameter
	#dbXARecAlias = " -xaRecoveryAuthAlias " + dbAlias
	
	# Create parameter to further configure the resources properties 
	#dbResProps = " -configureResourceProperties [[databaseName java.lang.String " + dsName + "] [serverName java.lang.String " + dbserver + "]]"
	#dbResProps = " -configureResourceProperties [[databaseName java.lang.String " + dbName + "]]"
	dbResProps = " -configureResourceProperties [[URL java.lang.String " + dbName + "]]"
	if debug == "YES":
		print "dbResProps values are ==",dbResProps
	#EndIf
	
	# Combine all the above variables into a list to pass to the
	# JDBC provider nameAdminTask.createDatasource() method
	createDsParams = [dsAttrs, jndiAttrs, dbHelperClass,\
			   dbAuthAlias, dbContMgrPersist, dbResProps] 
	if debug == "YES":		   
		print "before the get id and providername is = ", jdbcProviderName
	#endIF
		   
	# prepare the getID string for scope and type and name
	qs = proScopeValue + "/JDBCProvider:" + jdbcProviderName + "/"
	if debug == "YES":
		print "the getID string is:"
		print qs
	#endIF
	
	# Get JDBC provider configuration Id.
	# This is the parent object of the datasource
	#jdbcProviderId = AdminConfig.getid("/ServerCluster:" + clusterName + "/JDBCProvider:" + jdbcProviderName + "/")
	try:
		if debug == "YES":
			print "Before the getID for the JDBC Provider."
		#endIF
		dss = AdminConfig.getid(proScopeValue +"/JDBCProvider:" + jdbcProviderName + "/")
		if debug == "YES":
			print "After the config id get of provider and value is = ", dss
		#endIf
	#endTry
	except:
		print "Error with the AdminConfig.getID for JDBC Provider."
		return 1
	#endExcept
	if debug == "YES":
		print "Before the try for the AdminTask.createDatasource call."
	#endIF
	
	try:
		# Invoke AdminTask to create e datasource  using the parameters above
		AdminTask.createDatasource(dss, createDsParams)
	
		# Save the configuration
		AdminConfig.save()
	
		if debug == "YES":
			print "Created datasource:", dsName
		#endIF
	except:
		AdminConfig.reset()
		print "Failed to create datasource:", dsName
		print "possibly because it already exists."
		print "Pending changes were reset."
		return 2
	
	# otherwise we have a valid completion 
	#*****************************************************************************
	# get id of datasource we just created, first get the containment path
	dsIDname = proScopeValue + "/JDBCProvider:" + jdbcProviderName + "/DataSource:" + dsName.replace("'","") + "/"
	if debug == "YES":
		print "New datasource we created and containment path is  = ",dsIDname
	#EndIF
	
	# retrieve internal id of datasource
	dsId = AdminConfig.getid(dsIDname)
	if debug == "YES":
		print "New datasource id is = ", dsId
	#Endif
	
	# now lets create the mapping module for datasource - step one of three 
	AdminConfig.create("MappingModule",dsId,[ 
		['mappingConfigAlias', 'DefaultPrincipalMapping'],
		['authDataAlias', dbAlias]])
	if debug == "YES":
		print "After the create of the mapping module."
	#EndIf
	
	# next we need to get Connection Factory object that was created
	dsNameCF = dsName.replace("'","") + '_CF'
	print " connection factory name is = ", dsNameCF
	# now lets get configuration id for the connection factory
	cfId = AdminConfig.getid('/CMPConnectorFactory:'+dsNameCF+'/')
	print "the name of the connection factory id is = ",cfId
	
	AdminConfig.modify(cfId,[['name', dsNameCF],['authDataAlias', dbAlias],
		['xaRecoveryAuthAlias', ""]])
	print "after step 2 modify on connection factory"
	
	# now lets complete step three for security updates
	# set mapping module for connection factory
	if debug == "YES":
		print "Before the step 3 mappingmodule for connection factory"
	#EndIf
	
	AdminConfig.create("MappingModule",cfId,[ 
		['mappingConfigAlias', 'DefaultPrincipalMapping'],
		['authDataAlias', dbAlias]])
	if debug == "YES":
		print "After updating the updating Container-managed authentication alias - now save."
	#EndIf
	
	try:
		# Save the configuration
		AdminConfig.save()
	
		if debug == "YES":
			print "Done with updating Container-managed authentication alias."
		#endIF
	except:
		AdminConfig.reset()
		print "Failed to update Container-managed authentication alias."
		
		return 2
	
	return 0


	
# main logic 
if __name__ == '__main__':
    print " the number of arguments is = ",sys.argv
    print "number is == ",len(sys.argv)
    print "args is :"
    for arg in sys.argv:
    	print arg
    print "************************************************"
    if len(sys.argv) < 14:
    	print 'need node name, server name, generic arguments and debug'
        sys.exit(1)
        
debug=sys.argv[13]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

print "args is :"
for arg in sys.argv:
    print arg
    



# Get trade datasource properties
DsName = sys.argv[0]
DsJNDIName = sys.argv[1]
DsDescription = sys.argv[2]
DsScope = sys.argv[3]
providerScope = sys.argv[4]
# Get JDBC provider type property and remove single quotes from the value returned
jdbcProviderName = sys.argv[5]
dsDBName = sys.argv[6]
dsHelperClass = sys.argv[7]
dsMangPersistance = sys.argv[8]
dsClusterName=sys.argv[9]
dsCMP = sys.argv[10]
dbAlias= sys.argv[11]
dsNodeName = sys.argv[12]

# check and see if we have a cluster or cell scoped provider 
print "before the check if cell or cluster and values is = ", sys.argv[8]
if sys.argv[3] == "Cell":
	cell = AdminControl.getCell()
	scope = "Cell=" + cell
	if debug == "YES":
		print "we have a cell scoped creation."
	#endIF
else:
	clusterName = sys.argv[0]
	scope = "Cluster=" + clusterName
	if debug == "YES":
		print "we have a cluster scoped creation."
	#endIf
#endElse

print "before call to create datasource"
rtn = createDatasource(dsClusterName, jdbcProviderName, \
		 dbAlias, DsName, DsJNDIName,\
		 DsDescription, dsHelperClass,dsMangPersistance,dsDBName,DsScope, \
		 providerScope,dsCMP,dsNodeName, "YES")
if debug == "YES":
	if rtn == 0:
		print "Back from creation of the datasource and we are successfull.  Return code = ", rtn
	else:
		print "Back from creation of datasource and we have an error = ", rtn
	#endElse
#endIf
sys.exit(rtn)