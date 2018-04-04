
if __name__ == '__main__':
    print "amount of args passed in is ", sys.argv
    if len(sys.argv) < 7:
    	print 'Need scope, node name, server/cluster, binding name, name in space, string to bind and debug'
        sys.exit(1)
        
debug=sys.argv[6]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

scopeV=sys.argv[0]
nodeV=sys.argv[1]
serverClusterName = sys.argv[2]
nameV=sys.argv[3]
nameInSpV=sys.argv[4]
stringToBindV=sys.argv[5]



# check out what type of scope we should use
# check and see if we have a cluster or cell scoped provider 
cell = AdminControl.getCell()
if scopeV == "Cell":
	print "cell scope for sharedlib"
	proScopeValue = "/Cell:" + cell
	if debug == "YES":
		print "We have a datasource at the Cell level = ", proScopeValue
	#endIf
#endIF
elif  scopeV == "Cluster":
	proScopeValue = "/Cell:" + cell + "/ServerCluster:" + serverClusterName
	if debug == "YES":
		print "We have a datasource at the Cluster level = ", proScopeValue
	#endIf
elif  scopeV == "Node":
	proScopeValue = "/Cell:" + cell + "/Node:" + nodeV
	if debug == "YES":
		print "We have a datasource at the Node level = ", proScopeValue
	#endIf
elif  scopeV == "Server":
	proScopeValue = "/Cell:" + cell + "/Node:" + nodeV + "/Server:" + serverClusterName
	if debug == "YES":
		print "We have a datasource  at the Server level = ", proScopeValue
	#endIf
else:
	print "undefined scope for the datasource"
#endIfElse
	

if debug == "YES":
		print "Before the check of the scope."
	#EndIf	
# first check and see if the cluster already exists
scopeID=AdminConfig.getid(proScopeValue)
print "after the getid"
if scopeID == "":
	print "Scope value does not exist."
	sys.exit(1)
	

if debug == "YES":
		print "ready to create the name space binding. "
	#endIF

try:
	if debug == "YES":
		print "before create of name space binding"
	#endIF
	# Call AdminTask to create the cluster.
	AdminConfig.create('StringNameSpaceBinding', scopeID, [['name', nameV], \
	['nameInNameSpace',nameInSpV],['stringToBind',stringToBindV]])
	
#endTry
except:
	print "Exception with create shared lib  call."
	sys.exit(1)
#endExcept	

# Save the configuration change.
#
if debug == "YES":
		print "Created the name space binding  and now ready to save."
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
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with name space binding create."
	#endIF
sys.exit(0)