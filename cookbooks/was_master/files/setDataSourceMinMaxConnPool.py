

def modifyDSPoolMinMax(dataSName, minValue, maxValue, debug):
		     
	if debug == "YES":
		print "Inside modify connection pool min max with "
		print " min = ",minValue," and max = ",maxValue
	#endIf
	
	# first strip off the outer quotes on the data source name 
	ddsname = dataSName.replace("'","")
	# get ID to the datasource so that we can look at the connection pool attributes
	dsID = AdminConfig.getid('/DataSource:'+ ddsname + '/')
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
		["minConnections",minValue]]]])
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
    if len(sys.argv) < 4:
    	print 'Need datasource  name, min value, maximum value  and debug'
        sys.exit(1)
        
debug=sys.argv[3]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 


# Get trade datasource properties
DsName = sys.argv[0]
DsMin = sys.argv[1]
DsMax = sys.argv[2]


if debug == "YES":
 	print "Before call to function for min and max datasource connection pool update."
#EndIf
rtn = modifyDSPoolMinMax(DsName, DsMin, DsMax, debug)
if debug == "YES":
 	print "Back from min and max datasource connection pool update and the return value is = ",rtn
#EndIf
sys.exit(rtn)