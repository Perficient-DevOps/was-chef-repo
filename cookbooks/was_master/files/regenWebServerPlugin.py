
if __name__ == '__main__':
    print "amount of args passed in is ", sys.argv
    if len(sys.argv) < 3:
    	print 'Need node name, web server name, and debug'
        sys.exit(1)
        
debug=sys.argv[2]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

# input parameters
nodeV=sys.argv[0]
webserverV=sys.argv[1]


# check and see if the node exists before trying to create the web server
nodeId = AdminConfig.getid("/Node:" +nodeV)
print "after the get of the node and server and values is = ", nodeId
if (len(nodeId) == 0):
	# node exists 
        if debug == "YES":
           	print "Node   = ", nodeV, " does not exist. Please specify valid node name for web server."
        sys.exit(1)
#endIf

# we need to check and see if node and web server exists first
nodeId = AdminConfig.getid("/Node:" +nodeName+"/Server:" + webserverV)
if debug == "YES":
	print "after the get of the node and web server and values is = ", nodeId
#EndIf
if (len(nodeId) == 0):
	# server already exists
        if debug == "YES":
           	print "Web Server  = ", webserverV, " does not  exist."
        sys.exit(1)
#endIf

if debug == "YES":
		print "Need to get name of deployment manager and node. "
#endIF

#need to get node name from the deployment manager process

cell = AdminConfig.list("Cell")
nodes = AdminConfig.list('Node', cell).splitlines()
for node in nodes:
	nodeName = AdminConfig.showAttribute(node, 'name')
	servers = AdminConfig.list('Server', node).splitlines()
	for server in servers:
		serverName = AdminConfig.showAttribute(server, 'name')
		serverType = AdminConfig.showAttribute(server, 'serverType')
		if serverType == 'DEPLOYMENT_MANAGER':
			if debug == "YES":
				print "***** We have Deployment Manager on node = ",nodeName
			#EndIf
			dmgrNodeName=nodeName
		#EndIf
	#EndFor
#EndFor
if debug == "YES":
	print " Done with finding node name for dmgr = ",dmgrNodeName
#EndIf
	   
#now lets get the environment variables from cell/dmgr node and look for user install root
cell = AdminControl.getCell()
cellId= AdminConfig.getid("/Cell:" + cell)
varMap = AdminConfig.getid("/Cell:" + cell +"/Node:" + dmgrNodeName + "/VariableMap:/")
entries = AdminConfig.list("VariableSubstitutionEntry", varMap)
eList = entries.splitlines()
for entry in eList:
	name =  AdminConfig.showAttribute(entry, "symbolicName")
	if name == "USER_INSTALL_ROOT":
		if debug == "YES":
			print "We have found the USER_INSTALL_ROOT variable."
		#EndIf
        	value = AdminConfig.showAttribute(entry, "value")
        	if debug == "YES":
        		print "The USER_INSTALL_ROOT is = ",value
        	#EndIf
        #EndIf
#EndFor
if debug == "YES":
	print "After the get of the environment variable USER_INSTALL_ROOT"
#EndIf

# now lets regen the plugin for our web server       
generator = AdminControl.completeObjectName('type=PluginCfgGenerator,*')
webStr = value + "/config " + cell + " " + nodeV + " " + webserverV + " false"
if debug == "YES":
	print "Before the call to the regen and value is = ",webStr
#EndIf
try:
	if debug == "YES":
		print "Before AdminTask call to regen the web server ."
	#endIF
	AdminControl.invoke(generator,'generate',webStr)
	if debug == "YES":
		print "After AdminTask call to regen the web server."
	#endIF
#endTry
except:
	print "Exception with AdminControl.invoke  call to regen the  web server."
	sys.exit(1)
#endExcept

if debug == "YES":                                
	print "After the web server regeneration and it was successfull. "
#EndIf
 
sys.exit(0)