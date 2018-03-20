
if __name__ == '__main__':
    print "amount of args passed in is ", sys.argv
    if len(sys.argv) < 9:
    	print 'Need scope, node name,server/cluster name, library, class, desc, native, isolation and debug'
        sys.exit(1)
        
debug=sys.argv[8]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

scopeV=sys.argv[0]
nodeV=sys.argv[1]
serverClusterName = sys.argv[2]
libV=sys.argv[3]
classV=sys.argv[4]
descV=sys.argv[5]
nativeP=sys.argv[6]
isolateCL=sys.argv[7]

if nativeP == "none":
	nativeP = ""

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
		print "ready to create the shared library "
	#endIF

try:
	if debug == "YES":
		print "before create of shared library"
	#endIF
	# Call AdminTask to create the cluster.
	AdminConfig.create('Library', scopeID, [['name', libV], \
	['classPath',classV],['description',descV],['isolatedClassLoader', isolateCL], \
	['nativePath',nativeP]])
	#AdminResources.createSharedLibraryAtScope(scope,libV,classV)
#endTry
except:
	print "Exception with create shared lib  call."
	sys.exit(1)
#endExcept	

# Save the configuration change.
#
if debug == "YES":
		print "Created the shared library and now ready to save."
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
		print "Done with shared lib  create."
	#endIF
sys.exit(0)