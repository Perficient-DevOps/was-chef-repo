#************************************************************************
# Function: qryAppServer.py  -	Query application server for existance.
#
# Description:	This script has three  parameters.
#
# Parameters:
#		nodeName	-	Name of the node where server resides
#		serverName	-	Name of the server to be changed 
#		debug		-	debug value ( YES or NO ).
#
# Return Code:
#		0		-	Server exists.
#		1		-	Server does not exist in the cell
#
# Invocation:
#	./wsadmin.sh -conntype SOAP -host myHost -port myPort -lang jython
#		-f qryAppServer.py "myNode" "myServer" "Debug"
#
# Author:	Bruce J. Ryba  02/06/18
#
#**************************************************************************
global AdminConfig
global AdminTask



if __name__ == '__main__':
    if len(sys.argv) < 3:
    	print 'need node name, server name,and debug'
        sys.exit(1)
        
debug=sys.argv[2]
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

if debug == "YES":
		print "server name =",sys.argv[1]
		print "node name =",sys.argv[0]
#endIF
# we need to check and see if node and server exists first
# Check if server exists
server = AdminConfig.getid("/Node:" +sys.argv[0]+"/Server:"+sys.argv[1]+"/")
if (len(server) == 0):
	# server does not exist
	if debug == "YES":
           	print "Server = ", sys.argv[1], " was not found."
        #endIf
        sys.exit(1)
#endIf 
if debug == "YES":
	print 'done with the script and return code is 0.'
#endIf
sys.exit(0)