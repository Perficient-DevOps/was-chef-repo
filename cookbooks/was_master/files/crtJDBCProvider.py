#*************************************************************************
# Script: crtJDBCProvider.py - Set JVM generic arguments
#
# Description:   Script to create JDBC provider at the cluster or cell level 
#
# Parameters:
#		Script takes three parameters.
#		1) Cluster name/server name
#		2) Database type
#		3) Provider type
#		4) Implementation type
#		5) Provider descriptive name
#		6) Classpath
#		7) Description 
#		8) Implementation class
#		9) Scope: "Cell", "Server" or "Cluster"
#		10) Node name 
#		11) Debug "YES" or "NO" for printing debug statements for script 
#
# Return Codes:
#		0 = Completed without errors
#		2 = Error with one of the parameters
#			*NOTE:  Error processing will validate web application name, 
#				node name and server name for valid objects.   If 
#				there is an error, a corresponding error message will be printed 
#				indicating the incorrect parameter.
#
# Invocation Example:
#		./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -user wasadmin -password adminwas 
#		\ -f /WorkingData/jythonScripts/crtJDBCProvider.py "DevCluster" "Derby" "Derby JDBC Provider" "XA data source" 
#		\ "Bruce Plants Provider" "/opt/IBM/WebSphere/AppServer/derby/lib/derby.jar" "Derby provider for Plants by WebSphere" 
#		\ "org.apache.derby.jdbc.EmbeddedXADataSource" "Cluster" "YES"
#
# Author:
#	Bruce Ryba
# Date: 02/10/2018
#
#################################################################################
def createJDBCProvider(scope, jdbcDBType, jdbcProviderType, jdbcImplementationType,
	jdbcProName,jdbcProClass,jdbcProNative,jdbcProDesc,jdbcImplementationClass,debug):
	
	if debug == "YES":
		print "Creating JDBC provider"
		print "here are the parms:"
		print "scope = ", scope
		print "jdbcDBType = ", jdbcDBType
		print "jdbcProviderType = ", jdbcProviderType
		print "jdbcImplementationType = ", jdbcImplementationType
		print "jdbcProName = ", jdbcProName
		l = len(jdbcProClass)
		print "Number of classes passes in classList is = ",l
		print "JDBCProClass = ", jdbcProClass
		print "jdbcProNative = ", jdbcProNative
		print "jdbcProDesc = ", jdbcProDesc
		print "jdbcImpementationClass = ", jdbcImplementationClass
		print "Done with parameters."
		#return 0
	#endIF
	print "inside ***"
	#Create scope variable
	scope = "-scope " + scope
	if debug == "YES":
		print "the scope value is =", scope
	#endIf
	
	# Create database type variable
	dbType = " -databaseType " + jdbcDBType
	
	# Create jdbc provider type variable
	providerType = " -providerType " + "\"" + jdbcProviderType + "\""
	#providerType = " -providerType " + jdbcProviderType
	print " provider type is: ", providerType
	
	# Create JDBC implementation type variable
	implementationType = " -implementationType " + "\"" +jdbcImplementationType + "\""
	#implementationType = " -implementationType " + jdbcImplementationType
	
	# create JDBC name
	providerName = " -name " + "\"" + jdbcProName + "\""
	#providerName = " -name " + jdbcProName 
	
	# create JDBC description
	providerDesc = " -description " + "\"" + jdbcProDesc + "\"" 
	
	
	
	providerClass = " -classpath " + jdbcProClass
	#print "providerClass value is == ", providerClass
	
	# create native class 
	providerNative = " -nativePath " + "\"" + jdbcProNative + "\""
	
	#implementation class 
	implClass = " -implementationClassName " + jdbcImplementationClass
	
	# Concatenate all attributes
	#jdbcAttrs = scope + dbType + providerType + implementationType + providerName + \
	#	providerDesc + providerClass + providerNative
		
	jdbcAttrs = scope + dbType + providerType + implementationType + providerName  + providerClass 	\
		+ providerDesc + providerNative + implClass
		
	if debug == "YES":
		print "JDBC provider attributes: " + jdbcAttrs
	#endIF
	
	try:
		if debug == "YES":
			print "before AdminTask.createJDBCProvider call."
		#endIF
		# Call AdminTask to create the JDBC provider
		AdminTask.createJDBCProvider(jdbcAttrs)
	#endTry
	except:
		print "Exception with AdminTask.createJDBCProvider call."
		return 1
	#endExcept
	
	try:
		if debug == "YES":
			print "good admintask call now save"
		#endIF
		# Save configuration
		AdminConfig.save()
	#endTry
	except:
		print "exception in AdminConfig.save operation."
		return 2
	#endExcept
	
	if debug == "YES":
		print "Created JDBC provider, and done."
	#endIF
	return 0
	

# main logic

if __name__ == '__main__':
    if len(sys.argv) < 11:
    	print 'need node name, server name, generic arguments and debug'
        sys.exit(1)
        
debug=sys.argv[10]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

print "args is :"
for arg in sys.argv:
    print arg
    
# check and see if we have a cluster or cell scoped provider 
print "before the check if cell, cluster or server  and values is = ", sys.argv[8]
if sys.argv[8] == "Cell":
	cell = AdminControl.getCell()
	scope = "Cell=" + cell
	if debug == "YES":
		print "We have a cell scope provider creation.  Scope is = ", scope 
	#endIF
elif sys.argv[8] == "Cluster":
	clusterName = sys.argv[0]
	scope = "Cluster=" + clusterName
	if debug == "YES":
		print "We have a cluster scoped creation. Scope is = ", scope
	#endIf
elif sys.argv[8] == "Node":
	NodeName = sys.argv[9]
	scope = "Node=" + NodeName
	if debug == "YES":
		print "We have a node scope provider creation.  Scope is = ", scope
	#EndIf
else:
	# we have a server scope 
	serverName = sys.argv[0]
	NodeName = sys.argv[9]
	scope = "Node=" + NodeName + ",Server=" + serverName
	if debug == "YES":
		print "We have a server scope provider creation.  Scope is = ", scope
	#EndIf
#endIfElse

print "before the call to e function"
#Call the createJDBCProvider() method at the cluster scope
rtn = createJDBCProvider(scope, sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4],sys.argv[5],"",sys.argv[6],sys.argv[7],"YES")
if debug == "YES":
	print "back from e function and the return code is = " + str(rtn)
	print "done."
#endIf
sys.exit(rtn)
