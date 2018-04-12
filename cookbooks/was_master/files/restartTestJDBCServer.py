import time

serverName = sys.argv[0]
nodeNameV = sys.argv[1]
dataSourceName = sys.argv[2]
debug = sys.argv[3]

	
# first check and see if the cluster already exists
if debug == "YES":
	print "First verify that we indeed have a valid server  name."
#EndIf
mycell = AdminControl.getCell()
proScopeValue = "/Cell:" + mycell + "/Node:" + nodeNameV + "/Server:" + serverName
if debug == "YES":
	print "Before the get id of the server and using containment path: ",proScopeValue
serverID=AdminConfig.getid(proScopeValue + "/")
if serverID == "":
	print "Server ", serverName, " does not exist.  Cannot restart server that does not exist."
	sys.exit(1)
		
if debug == "YES":
		print "***** Ready to stop  the server."
	#endIF
	
# check to see if the server is up, if server is down then complete object name is blank
serverCON = AdminControl.completeObjectName('cell='+mycell+',node='+nodeNameV+',name='+serverName+',type=Server,*')
print "after complete object name get and value is = ",serverCON
# query the state of the server
if serverCON == "":
	print " Server is already in a stopped state."
#EndIf 
else:
	#we need to stop the server first 
	serverState = AdminControl.getAttribute(serverCON, 'state')

	if debug == "YES":
		print "		Server state is =",serverState
	#EndIf
	
	try:
		if debug == "YES":
			print "		Before AdminClusterManagement.stopSingleServer call."
		#endIF
		# Call AdminClusterManagement.stopSingleCluster to start the server.
		AdminServerManagement.stopSingleServer(nodeNameV,serverName)
		if debug == "YES":
			print "		After AdminServerManagement.stopSingleServer call -successful. "
		#endIF
	#endTry
	except:
		print "		Exception with AdminServerManagement.stopSingleServer call.  Server not stopped."
		sys.exit(1)
	#endExcept	

time.sleep(60)

try:
	if debug == "YES":
		print "Before AdminServerManagement.startSingleServer call."
	#endIF
	# Call AdminServerManagement.stopSingleServer to start the server.
	AdminServerManagement.startSingleServer(nodeNameV,serverName)
	if debug == "YES":
		print "After AdminServerManagement.startSingleServer call -successful. "
	#endIF
#endTry
except:
	print "Exception with AdminServerManagement.startSingleServer call.  Server not started."
	#sys.exit(1)
#endExcept	

#sleep for about 60 seconds for cluster members to start 
time.sleep(60)

#Now we need to test the datasource connections on the server
# get a list of data sources defined for cluster scope and find the one that is ours
if debug == "YES":
	print "Data source list at server scope  is: ======",AdminConfig.list("DataSource",serverID)
#EndIf

#place list in a list object - there might be more data sources defined at scope level cluster
dsList = AdminConfig.list("DataSource", serverID).splitlines()
if debug == "YES":
	print "The list of data sources for server are: ", dsList
#EndIf

#now loop through the list of data sources at cluster level and find our datasource
foundDs = "False"

if debug == "YES":
	print "The length of the ds list is =",len(dsList)
#EndIf 

#loop through list and get name of datasource, provider name
for dsItem in dsList:
	if debug == "YES":
		print "Inside the datasource list looking for our datasource match."
		print "Working with datasource item = ",dsItem
	#EndIf
	
	#check and see if this is the datasource that we are after
	#pull name from datasource id and see if it matches our datasource
	dsMember_name=AdminConfig.showAttribute(dsItem, "name")
	dsProvider = AdminConfig.showAttribute(dsItem,"provider")
	dsProviderName = AdminConfig.showAttribute(dsProvider,"name")
	
	if debug == "YES":
		print "After the show attribute on the datasource."
		print "The datasource name for ",dsItem," is = ",dsMember_name,"."
		print "The provider for the datasource is =", dsProvider
		print "The provider name is = ",dsProviderName
	#EndIf
	
	#check and see if we have indeed a match with our datasource and item from list
	if dsMember_name == dataSourceName:
		if debug == "YES":
			print "We have a match on the datasource name."
			print "Before the test connection on the server scoped datasource ",dsMember_name
		#EndIf 
		
		#Build out containment path for the datasource so we can get the id for it
		#proScopeValue = "/Cell:" + mycell + "/ServerCluster:" + clusterName
		dsIDname = proScopeValue + "/JDBCProvider:" + dsProviderName + "/DataSource:" + dsMember_name + "/"
		if debug == "YES":
			print "Datasource containment path is  = ",dsIDname
		#EndIF
	
		# retrieve internal id of datasource
		dsId = AdminConfig.getid(dsIDname)
		if debug == "YES":
			print "Datasource id is = ", dsId
		#Endif
		
		try:
			#now test the connection
			
			AdminControl.testConnection(dsId)
			if debug == "YES":
				print "After the test connection."
			foundDs = "True"
		#Endtry
		except:
			if debug == "YES":
				print "Error with testing data source connection ",dsMember_name
				print "Make sure that the datasource works correctly."
			#EndIf 
			sys.exit(1)
		#EndExcept
	else:
		if debug == "YES":
			print "Not a match for the item in datasource list and our datasource."
		#EndIf 
		
if foundDs == "False":
	if debug == "YES":
		print "We did not find a datasource ", dataSourceName," at the server  scope."
		print "Could not test the data source on the server level. "
		sys.exit(1)
	#EndIf 
#EndIf
else:
	if debug == "YES":
		print "Successfully tested server level datasource."
	#EndIf
	
if debug == "YES":
		print "Done with server restart and testing of datasource. Please review test info in logs."
	#endIF
sys.exit(0)