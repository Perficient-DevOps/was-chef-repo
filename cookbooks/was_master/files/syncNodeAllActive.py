#*************************************************************************
# Script: syncNodeAllActive.py - Perform sychronization on a node
#
# Description:   Script to sync a given node. 
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
        
debug=sys.argv[0]
print "debug value is = ",sys.argv[0]
print "before check for debug"
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

# we need to check and see if node and server exists first
# Check if server exists

# Find JVM
if debug == "YES":
	print "before the synch node for all active nodes in cell."
#endIf

try:
	if debug == "YES":
		print "Before AdminNodeManagement ."
	#endIF
	Sync=AdminNodeManagement.syncActiveNodes()
	if debug == "YES":
		print "After AdminNodeManagement sync call to sync active nodes."
	#endIF
#endTry
except:
	print "Exception with AdminNodeManagement sync all active nodes."
	sys.exit(1)
#endExcept

if debug == "YES":
	print "After sync and returnvalue is =", Sync
#endIf

# now lets test returncode from sync to be sure it worked
if Sync == 1:
	# we have a valid sychronization of the node
	if debug == "YES":
		print "We have a valid sychronization of all of the active nodes."
	#Endif
	sys.exit(0)
else:
	# we do not have a valid sync.
	if debug == "YES":
		print "We do not have a valid sychronization of all of the active nodes."
	#Endif
	sys.exit(1)

sys.exit(1)
