#*************************************************************************
# Script: setJVMCustProp.py - Set JVM custom property
#
# Description:   Script to set custom property for a given server 
#
# Parameters:
#		Script takes five parameters.
#		1) Node name
#		2) Server name
#		3) property name
#               4) property value
#		5) Debug "YES" or "NO" for printing debug statements for script 
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
#		./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -javaoption #{node['was']['jvm_size']} -user wasadmin -password adminwas 
#                \ -f /WorkingData/jythonScripts/setJVMCustProp.py "STLSCVMG95219Node01" "bruce" "bruce" "Ryba" "YES"
#
# Author:
#	Bruce Ryba
# Date: 02/07/2018
#
#################################################################################
global AdminConfig
global AdminTask
global AdminControl
print 'instide test script '


# main logic
if __name__ == '__main__':
    if len(sys.argv) < 5:
    	print 'need node name, server name, custom name, custom value and debug'
        sys.exit(1)
        
debug=sys.argv[4]
print "before check for debug"
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

# we need to check and see if node and server exists first
# Check if server exists
server_id = AdminConfig.getid("/Node:" +sys.argv[0]+"/Server:"+sys.argv[1]+"/")
if (len(server_id) == 0):
	# server does not exist
        if debug == "YES":
        	print "Server = ", sys.argv[1], " was not found."
        sys.exit(1)
#endIf

if debug == "YES":
	print "After the server_id and "
	print server_id
#endIf

# Find JVM
if debug == "YES":
	print "before the javavirtualmachine serverid get"
#endIf
jvm_id = AdminConfig.list('JavaVirtualMachine', server_id )

# Create and initialize variables used for custom property attributes

valid=["validationExpression", ""]
nname=["name",sys.argv[2]]
vvalue=["value",sys.argv[3]]
descrip=["description","description"]
requiredd=["required","false"]
custAt=[valid,nname,descrip,vvalue,requiredd]

# Add new properties
AdminConfig.create('Property', jvm_id, custAt)

AdminConfig.save()
sys.exit(0)
