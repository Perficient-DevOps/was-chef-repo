
if __name__ == '__main__':
    print "amount of args passed in is ", sys.argv
    if len(sys.argv) < 9:
    	print 'Need node name, server/cluster, binding name, name in space, string to bind and debug'
        sys.exit(1)
        
debug=sys.argv[8]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 


nodeV=sys.argv[0]
webserverV=sys.argv[1]
portV=sys.argv[2]
plgInsRootV=sys.argv[3]
webInstallRootV=sys.argv[4]
adminUserV=sys.argv[5]
adminPsswdV=sys.argv[6]
webServerTypeV=sys.argv[7]

# check and see if the node exists before trying to create the web server
nodeId = AdminConfig.getid("/Node:" +nodeV)
print "after the get of the node and server and values is = ", nodeId
if (len(nodeId) == 0):
	# node exists 
        if debug == "YES":
           	print "Node   = ", nodeV, " does not exist.   Please create node first."
        sys.exit(1)
#endIf

# we need to check and see if node and server exists first
# Check if server exists
# we need to check and see if node and server exists first
  	# Check if server exists
print "before the getid of the node and server"
nodeId = AdminConfig.getid("/Node:" +nodeName+"/Server:" + webserverV)
print "after the get of the node and server and values is = ", nodeId
if (len(nodeId) != 0):
	# server already exists
        if debug == "YES":
           	print "Web Server  = ", webserverV, " already exists."
        sys.exit(1)
#endIf
print "after the check for the server "

if debug == "YES":
		print "ready to create the web server. "
#endIF

if webServerTypeV == "SUN":
	webServerType = "SUNJAVASYSTEM"
elif webServerTypeV == "IHS":
		webServerType = "IHS"
#EndIfElse
else:
	# we have an invalid type of web server
	if debug == "YES":
		print "Invalid type of web server. Please specify either IHS or SUN."
	#endIF
	sys.exit(1)
#EndElse
if debug == "YES":
	print "We have a type ",webServerType," web server creation request."
#EndIf 
	
#call the AdminTask to create the web server 
try:
	if debug == "YES":
		print "Before AdminTask call to create the web server."
	#endIF
	
	AdminTask.createWebServer(nodeV,'[-name ' + webserverV + ' -templateName ' + webServerType \
		+ ' -serverConfig [-webPort ' + portV + ' -serviceName -webInstallRoot ' + webInstallRootV \
		+ ' -webProtocol HTTP' \
		+ ' -configurationFile -errorLogfile -accessLogfile -pluginInstallRoot ' + plgInsRootV \
		+ ' -webAppMapping ALL] ' \
		+ ' -remoteServerConfig [-adminPort 8008 -adminUserID ' + adminUserV \
		+ ' -adminPasswd ' +  adminPsswdV + ' -adminProtocol HTTP]]')
	if debug == "YES":
		print "After AdminTask call to create the web server."
	#endIF
#endTry
except:
	print "Exception with AdminTask call to create web server."
	sys.exit(1)
#endExcept	
	
# Save the configuration change.
if debug == "YES":
		print "Created the web server and now ready to save."
	#endIF
try:
	if debug == "YES":
		print "before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
#endTry
except:
	print "Exception with AdminConfig.save call."
	AdminConfig.reset()
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with web server  create."
	#endIF
sys.exit(0)