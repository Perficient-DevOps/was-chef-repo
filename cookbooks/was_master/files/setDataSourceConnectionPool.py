

def modifyDSPoolMinMax(dataSName, minValue, maxValue,connTimeOut,unusedTimeout, agedTimeout, reepTime, \
			purgeP,dsScope, dsClusterServerName, dsNodeName,dsProviderName, debug):
		     
	if debug == "YES":
		print "Inside modify connection pool min max with "
		print " min = ",minValue," and max = ",maxValue
	#endIf
	
	# first strip off the outer quotes on the data source name 
	ddsname = dataSName.replace("'","")
	# get ID to the datasource so that we can look at the connection pool attributes
	## need to set correct containment type.  Might have more than one ds with same name
	## on different scopes - problem.  Need to know scope.
	cell = AdminControl.getCell()
	if dsScope == "Cell":
		print "cell scope for datasource"
		#cell = AdminControl.getCell()
		proScopeValue = "/Cell:" + cell
		if debug == "YES":
			print "We have a datasource at the Cell level = ", proScopeValue
		#endIf
	#endIF
	elif  dsScope == "Cluster":
		proScopeValue = "/Cell:" + cell + "/ServerCluster:" + dsClusterServerName
		if debug == "YES":
			print "We have a datasource at the Cluster level = ", proScopeValue
		#endIf
	elif  dsScope == "Node":
		proScopeValue = "/Cell:" + cell + "/Node:" + dsNodeName
		if debug == "YES":
			print "We have a datasource at the Node level = ", proScopeValue
		#endIf
	elif  dsScope == "Server":
		proScopeValue = "/Cell:" + cell + "/Node:" + dsNodeName + "/Server:" + dsClusterServerName
		if debug == "YES":
			print "We have a datasource  at the Server level = ", proScopeValue
		#endIf
	else:
		print "undefined scope for the datasource"
	#endIfElse
	
	# now lets use our containment path to find datasource at the right scope
	dataSpath = proScopeValue + '/JDBCProvider:' + dsProviderName + '/DataSource:'+ ddsname + '/'
	if debug == "YES":
		print "Before the get of the datasource id with containment path = ", dataSpath
	#EndIf
	dsID = AdminConfig.getid(dataSpath)
	if (len(dsID) == 0):
		# server does not exist
       		 if debug == "YES":
        		print "DataSource = ", ddsname, " was not found."
        	 sys.exit(1)
	#endIf
	if debug == "YES":
		print "the getid of the datasource is = ", dsID
	#endIf
	else:
		if debug == "YES":
			print "We do not have a valid datasource name.  Please specify correct name please."
		#EndIf
		return 1
	#endElse
	
	# know lets modify the attributes for min and max on data source attribute connectionpool
	try:
		if debug == "YES":
			print "Before the modify of connection pool via AdminConfig.modify."
		#endIf
		AdminConfig.modify(dsID,[["connectionPool",[["maxConnections", maxValue], \
		["minConnections",minValue], ["unusedTimeout", unusedTimeout],["agedTimeout",agedTimeout], \
		["purgePolicy", purgeP],["reapTime",reepTime],["connectionTimeout",connTimeOut]]]])
	#endTry
	except:
		print "Problem with AdminConfig.modify to change min and max on connection pool."
		# reset the configuration changes due to errors.
		AdminConfig.reset()
		return 1
	#endExcept
	if debug == "YES":
		print "After the modify and getting ready to save configuration."
	#endIF 
	try:
		AdminConfig.save()
	#endTry
	except:
		print "error with the AdminConfig.save operation."
		AdminConfig.reset()
		return 2
	#endIf
	# otherwise we have had a successful change
	if debug == "YES":
		print "successful change of the min and the max values."
	#endIf
	
	return 0
	
	
# main logic 
if __name__ == '__main__':
    print "amount of args passed in is ", sys.argv
    if len(sys.argv) < 13:
    	print 'Need datasource  name, min value, maximum value  and debug'
        sys.exit(1)
        
debug=sys.argv[12]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 


# Get trade datasource properties
DsName = sys.argv[0]
DsMin = sys.argv[1]
DsMax = sys.argv[2]
DsCTout = sys.argv[3]
DsUTout = sys.argv[4]
DsATout = sys.argv[5]
DsRT = sys.argv[6]
DsPP = sys.argv[7]
DsScope = sys.argv[8]
DsClSrv = sys.argv[9]
DsNode = sys.argv[10]
DsProVName = sys.argv[11]



if debug == "YES":
 	print "Before call to function for min and max datasource connection pool update."
#EndIf
rtn = modifyDSPoolMinMax(DsName, DsMin, DsMax,DsCTout, DsUTout, DsATout, DsRT, DsPP,DsScope, \
	DsClSrv, DsNode, DsProVName,debug)
if debug == "YES":
 	print "Back from min and max datasource connection pool update and the return value is = ",rtn
#EndIf
sys.exit(rtn)