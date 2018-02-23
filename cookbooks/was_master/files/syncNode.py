#*************************************************************************
# Script: syncNode.py - Perform sychronization on a node
#
# Description:   Script to sync a given node.
#
# Parameters:
#		Script takes two parameters.
#		1) Node name
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
#		./wsadmin.sh -conntype SOAP -host STLSCVMG95219 -port 10003 -lang jython -user wasadmin -password adminwas
#                \ -f /WorkingData/jythonScripts/syncNodes.py "STLSCVMG95219Node01" "YES"
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
    if len(sys.argv) < 1:
    	print 'need node name, and debug'
        sys.exit(1)

debug=sys.argv[1]
print "debug value is = ",sys.argv[1]
print "before check for debug"
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF

# we need to check and see if node and server exists first
# Check if server exists
print "before check if node is ok"
node_id = AdminConfig.getid("/Node:" +sys.argv[0]+"/")
if (len(node_id) == 0):
	# server does not exist
        if debug == "YES":
        	print "Node = ", sys.argv[0], " was not found."
        sys.exit(1)
#endIf
print "after check is node is OK"
if debug == "YES":
	print "After the node_id and "
	print node_id
#endIf

# Find JVM
if debug == "YES":
	print "before the synch node for node, ", node_id
#endIf

Sync1 = AdminControl.completeObjectName('type=NodeSync,node='+sys.argv[0]+',*')
if debug == "YES":
	print "after complete objectname and object is =",Sync1
#endIf
rtn = AdminControl.invoke(Sync1, 'sync')
if debug == "YES":
	print "After sync and returnvalue is =",rtn
#endIf

# now lets test returncode from sync to be sure it worked
if rtn == "true":
	# we have a valid sychronization of the node
	sys.exit(0)
else:
	# we do not have a valid sync.
	sys.exit(1)

sys.exit(1)
