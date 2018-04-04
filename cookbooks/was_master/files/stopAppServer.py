#*************************************************************************
# Script: stopAppServer.py - Stop Application Server
#
# Description:   Simple script to stop applications server on given node. 
#
# Parameters:
#		Script takes three parameters.
#		1) Node name
#		2) Server name
#		3) Debug "YES" or "NO" for printing debug statements for script 
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
#		wsadmin.sh ( or .bat ) -profileName Dmgr -lang jython 
#			/ -f stopAppServer.py "mnNode" "myServer" "YES"
# Author:
#	Bruce Ryba
# Date: 02/07/2018
#
#################################################################################


if __name__ == '__main__':
    if len(sys.argv) < 3:
    	print 'Need three parameters, first is the  node name,server name, debug.'
        sys.exit(1)
        
debug=sys.argv[2]
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 
    
try:
	# execute the stopSingleServer function from the AdminApplication library
	rtn=AdminServerManagement.stopSingleServer(sys.argv[0],sys.argv[1])
	if debug == "YES":
		print "back from call and the return code is " + str(rtn)
	#endIF
except:
	# error processing, print out the cause of the error.
	typ,val,tb = sys.exc_info()
	print "Error with executing start of web application because:"
	print val
	sys.exit(2)
print "Applicaiton Server stopped."  
sys.exit(0)















