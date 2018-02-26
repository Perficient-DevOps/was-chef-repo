
global AdminConfig
global AdminTask
global AdminControl


# main logic
if __name__ == '__main__':
    if len(sys.argv) < 4:
    	print 'need node name, server name, JDK version, and debug'
        sys.exit(1)
        
debug=sys.argv[3]
print "before check for debug"
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

# we need to check and see if node and server exists first
# Check if server exists
if debug == "YES":
	print "Before the call to verify that we have a valid node and server name."
#EndIf

server_id = AdminConfig.getid("/Node:" +sys.argv[1]+"/Server:"+sys.argv[0]+"/")
if (len(server_id) == 0):
	# server does not exist
        if debug == "YES":
        	print "Server = ", sys.argv[0], " was not found. Please specify valied node and server name."
        sys.exit(1)
#endIf

if debug == "YES":
	print "After the server_id and we have a valid server and node."  
	print "Server id that we are going to update JDK on is = ",server_id
#endIf

try:
	# change the end point here
       	if debug == "YES":
       		print "Before the AdminTask.setServerSDK command."
       	#endIF
        AdminTask.setServerSDK("[-nodeName "+ sys.argv[1] +" -serverName " + sys.argv[0] + " -sdkName "+ sys.argv[2] + "]")
        if debug == "YES":
        	print "After set JDK, now we need to save."
#endTry
except:
	if debug == "YES":
        	print "Error with the AdminTask.setServerSDK."
        #endIf 
	sys.exit(1)
#EndExcept
       

try:
	# change the end point here
       	if debug == "YES":
       		print "Before the AdminConfig.save command.  Need to save changes"
       	#endIF
        AdminConfig.save()
        if debug == "YES":
        	print "After save of configuration - successful."
#endTry
except:
	if debug == "YES":
        	print "Error with the AdminConfig.save() - configuration save error.  Unsuccessful. "
        #endIf 
	sys.exit(1)
#EndExcept

if debug == "YES":
        	print "Finished with JDK change."
        #endIf 
sys.exit(0)
