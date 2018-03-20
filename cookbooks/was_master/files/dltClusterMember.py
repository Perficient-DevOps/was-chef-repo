
# parameters: cluster name, node name , server name 
clusterName = sys.argv[0]
serverName = sys.argv[1]
nodeName = sys.argv[2]
debug = sys.argv[3]

	
if debug == "YES":
	print "First check and see if we have a valid cluster."
#EndIf
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist - please specify valid cluster name."
	sys.exit(1)
		
	
if debug == "YES":
		print "REeady to delete  cluster member. "
	#endIF
	
try:
	if debug == "YES":
		print "before AdminClusterManagement.deleteClusterMember call."
	#endIF
	# Call AdminTask to delete the cluster.
	AdminClusterManagement.deleteClusterMember(clusterName, nodeName, serverName)
	if debug == "YES":
		print "After AdminClusterManagement.deleteClusterMember call - successful."
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.deleteClusterMember call.  Cluster member not deleted."
	sys.exit(1)
#endExcept	

# Save the configuration change.
#
if debug == "YES":
		print "Deleted cluster  member.. ready to save repository."
	#endIF
try:
	if debug == "YES":
		print "Before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
	if debug == "YES":
		print "After AdminConfig.save - successful. "
	#endIF
#endTry
except:
	print "Exception with AdminConfig.save call - delete of cluster member not saved. "
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with clusterMember delete."
	#endIF
sys.exit(0)