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
#print "debug value is = ",sys.argv[1]
#print "before check for debug"
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 
nodeName = sys.argv[0]
if debug == "YES":
	print "node name is =",nodeName
#endIf

#check to see if the node exists
nodeRtn = AdminNodeManagement.doesNodeExist(nodeName)
print "return value from does node exist is =",nodeRtn
if nodeRtn == "true":
	# we have a valid node name, next check and see if it is running
	nodeActive = AdminNodeManagement.isNodeRunning(nodeName)
	print "return value from is active is =",nodeActive
	if nodeActive == 1: 
		print " we have a valid and active node that can be sychronized."
		# Find JVM
		

		Sync1 = AdminControl.completeObjectName('type=NodeSync,node='+nodeName+',*')
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
			if debug == "YES":
				print "We have a valid sychronization!"
			#endIf
			sys.exit(0)
		else:
			# we do not have a valid sync.
			if debug == "YES":
				print "We have an invalid sychronization!"
			#endIf
			sys.exit(1)
	#EndIf
	else:
		print "We have a valid node agent but it is not active.  No Sync. "
		sys.exit(0)
	#EndElse
#EndIf
else:
	if debug == "YES":
		print "Invalid node name.  Please specify a correct node name."
	#EndIf
	sys.exit(1)
#EndElse
	
if debug == "YES":
	print "Done with sync node script."
#EndIf


