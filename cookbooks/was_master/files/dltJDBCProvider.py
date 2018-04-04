# Script: dltJDBCProvider.py - Set JVM generic arguments
#
# Description:   Script to create JDBC provider at the cluster or cell level
#
# Parameters:
#		Script takes three parameters.
#		1) Provider name
#		10) Debug "YES" or "NO" for printing debug statements for script
#
# Return Codes:
#		0 = Completed without errors
#		1 = Error with one of the parameters
#			*NOTE:  Error processing will validate web application name,
#				node name and server name for valid objects.   If
#				there is an error, a corresponding error message will be printed
#				indicating the incorrect parameter.
#
# Invocation Example:
#		./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -user wasadmin -password adminwas
#		\ -f /WorkingData/jythonScripts/dltJDBCProvider.py "Bruce Provider"  "YES"

#
# Author:
#	Bruce Ryba
# Date: 02/10/2018
#
#################################################################################



# main logic

if __name__ == '__main__':
    if len(sys.argv) < 2:
    	print 'Need provider name, and debug'
        sys.exit(1)

debug=sys.argv[1]
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF

print "args is :"
for arg in sys.argv:
    print arg



jdbcProviderName = sys.argv[0]



# perform the getID on the provider object
try:
	if debug == "YES":
		print "Before the getID for the JDBC Provider."
	#endIF
	providerID = AdminConfig.getid("/JDBCProvider:" + jdbcProviderName + "/")
#endTry
except:
	if debug == "YES":
		print "Error with the AdminConfig.getID for JDBC Provider."
	#endIf
	sys.exit(1)
#endExcept


# check and see if we have a provider first
if (len(providerID) == 0):
	# provider does not exist
        if debug == "YES":
           	print "Provider = ", jdbcProviderName, " was not found."
        sys.exit(0)
#endIf

# otherwise we have a provideer and need to delete it
if debug == "YES":
	print "JDBC provider ready for delete."
#endIF

try:
	if debug == "YES":
		print "before AdminTask.createJDBCProvider call."
	#endIF
	# Call AdminTask to create the JDBC provider
	AdminTask.deleteJDBCProvider(providerID)
#endTry
except:
	print "Exception with AdminTask.createJDBCProvider call."
	sys.exit(1)
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
	sys.exit(1)
#endExcept

if debug == "YES":
	print " We have a successfull save of the configuration."
#endIF
sys.exit(0)
