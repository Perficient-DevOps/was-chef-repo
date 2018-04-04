#************************************************************************
# Function: ChgServerPorts  	- Change ports for a given server.
#
# Description:	Change endPoints for a given server in a cell.  Script 
#		checks to see if server is a nodeagent.  If so, different
#		endpoints are modified ( subset ).
#
# Parameters:
#		nodeName	-	Name of the node where server resides
#		serverName	-	Name of the server to be changed. 
#		transportStartPort 	portBlock starting point 
#		debug		-	debug value ( YES or NO ).
#
# Return Code:
#		0		-	Endpoints changed OK.
#		1		-	Server does not exist in the cell.
#		2		-	AdminTask operation failed.
#		3		-	Invalid starting port value
#		4		-	Failure on AdminConfig.save operation
#
# *NOTE:  
#
# Author:	Bruce J. Ryba  01/18/11
#
#**************************************************************************
def modifyPorts ( serverName, nodeName, transportStartPort,debug):

        #--------------------------------------------------------------
        # set up globals
        #--------------------------------------------------------------
        global AdminConfig
        global AdminControl
        global AdminApp
        
        nodeAgentEndPoints = [ "BOOTSTRAP_ADDRESS","CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS",
        			"CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS","DCS_UNICAST_ADDRESS",
        			"NODE_DISCOVERY_ADDRESS","NODE_IPV6_MULTICAST_DISCOVERY_ADDRESS",
        			"NODE_MULTICAST_DISCOVERY_ADDRESS","ORB_LISTENER_ADDRESS",
        			"SAS_SSL_SERVERAUTH_LISTENER_ADDRESS","SOAP_CONNECTOR_ADDRESS",
        			"IPC_CONNECTOR_ADDRESS","XDAGENT_PORT","OVERLAY_TCP_LISTENER_ADDRESS",
        			"OVERLAY_UDP_LISTENER_ADDRESS"]
        appServerEndPoints = [ "WC_defaulthost","WC_defaulthost_secure","WC_adminhost",
        			"WC_adminhost_secure","BOOTSTRAP_ADDRESS","SOAP_CONNECTOR_ADDRESS",
        			"IPC_CONNECTOR_ADDRESS","SAS_SSL_SERVERAUTH_LISTENER_ADDRESS",
        			"CSIV2_SSL_SERVERAUTH_LISTENER_ADDRESS","CSIV2_SSL_MUTUALAUTH_LISTENER_ADDRESS",
        			"ORB_LISTENER_ADDRESS","DCS_UNICAST_ADDRESS","SIB_ENDPOINT_ADDRESS",
        			"SIB_ENDPOINT_SECURE_ADDRESS","SIB_MQ_ENDPOINT_ADDRESS",
        			"SIB_MQ_ENDPOINT_SECURE_ADDRESS","SIP_DEFAULTHOST","SIP_DEFAULTHOST_SECURE",
        			"OVERLAY_UDP_LISTENER_ADDRESS","OVERLAY_TCP_LISTENER_ADDRESS"]
  
  	print "before the check of server type"
  	# first check and see if we are changing a nodeagent or application server
  	if serverName == "nodeagent":
  		# then we need to use endpoints for node agents only
  		print "we have a node agent to process"
  		endPointsChg = nodeAgentEndPoints
  	#endIf
  	else:
  		print "we have an application server to process"
  		endPointsChg = appServerEndPoints
  	#endElse
  	
  	# we need to check and see if node and server exists first
  	# Check if server exists
        server = AdminConfig.getid("/Node:" +nodeName+"/Server:"+serverName+"/")
        if (len(server) == 0):
           # server does not exist
           if debug == "YES":
           	print "Server = ", serverName, " was not found."
           return 1
        #endIf
  	
  	print "before the change to the ports"
  	# set initial starting portblock
        myPort = int(transportStartPort)
        if ( transportStartPort > 0 ):
        	# loop through the endpoints in list and assign port block value and increment
        	for sEPoint in endPointsChg:
                	sAttrs = '[-nodeName ' + nodeName + ' -endPointName ' + sEPoint + ' -port ' \
                		 + str(myPort) + ' -modifyShared true' + ']'
                        try:
                        	# change the end point here
       				if debug == "YES":
       					print "--## Changing "+sEPoint+" for "+ serverName + " to: " + str(myPort)+" ##--"
       				#endIF
           			AdminTask.modifyServerPort( serverName, sAttrs )
        		#endTry
       			except:
        			if debug == "YES":
        				print "Error with the Admin Task and save."
        			#endIf 
        			#AdminConfig.reset()
        			return 2
       			#endExcept
                        myPort = myPort+1
        	#endFor
        #endif
        else:
        	if debug == "YES":
        		print " we have a invalid starting port value"
        		return 3
        	#endIF
        #endElse
        
	# we have had a successful adminTask set and now lets save the env. 		
	# Save the changes
	try:
		if debug == "YES":
			print "before the save of the configuration"
		#endIf 
		AdminConfig.save()
		if debug == "YES":
			print "after the AdminConfig.save()"
		#endIf
		return 0
	#endTry
	except:
		if debug == "YES":
			print " we have an exception with the AdminConfig.save operation."
		#endIf
		return 4
	#endExcept

        
#endDef 
print "Before the call to change ports"
if len(sys.argv) != 4:
   print "ex2: this script requires 4 parameters: serverName, nodeName, and debuy yes or no"
   print "e.g.:     chgwasports.py myServer myNode 20000 YES" 
   print " here are the parameters that you passed in: "
   print sys.argv[0]
   print sys.argv[1]
   print sys.argv[2]
   print sys.argv[3]
   print "total amount of parameters is: " + len(sys.argv)
   #print len(sys.argv)
else:
   #print sys.argv[0]
   #print sys.argv[1]
   #print sys.argv[2]
   #print sys.argv[3]
   #print len(sys.argv)
   rtn = modifyPorts(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
   print "back from modifyPorts call and return value is = " + str(rtn)
   print "done."
