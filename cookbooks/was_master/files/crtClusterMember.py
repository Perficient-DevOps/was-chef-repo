
# parameters: cluster name, node name , server name 
clusterName = sys.argv[0]
serverName = sys.argv[1]
nodeName = sys.argv[2]
debug = sys.argv[3]

	
# first check and see if the cluster already exists
if debug == "YES":
	print "First check and see if cluster exists."
#EndIf
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist - please create first, and create first cluster member before this script."
	sys.exit(1)
		
	
if debug == "YES":
		print "Ready to create additional  cluster member."
	#endIF
	
try:
	if debug == "YES":
		print "Before AdminClusterManagement.createClusterMember call."
	#endIF
	# Call AdminTask to create the cluster.
	AdminClusterManagement.createClusterMember(clusterName, nodeName, serverName)
	if debug == "YES":
		print "After AdminClusterManagement.createClusterMember call and successful."
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.createClusterMember call.  Additional cluster member not created."
	sys.exit(1)
#endExcept	

# Save the configuration change.
#
if debug == "YES":
		print "Created additional  member succeeded.  Now ready to save repository."
	#endIF
try:
	if debug == "YES":
		print "Before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
	if debug == "YES":
		print "After AdminConfig.save - successful repository save. "
	#endIF
#endTry
except:
	print "Exception with AdminConfig.save call - additional cluster member not created."
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with additional clusterMember create - successful."
	#endIF
sys.exit(0)