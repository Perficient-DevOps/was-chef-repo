
# parameters: cluster name, node name , server name 
clusterName = sys.argv[0]
serverName = sys.argv[1]
nodeName = sys.argv[2]
debug = sys.argv[3]
preferLocal="true"
createReplicationDomain="true"
	
# first check and see if the cluster already exists
if debug == "YES":
	print "Check and see if the cluster exists for new cluster member."
#EndIf
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist - please create first before calling this script."
	sys.exit(1)
		
	
if debug == "YES":
		print "Ready to create first cluster member. "
	#endIF
	
try:
	if debug == "YES":
		print "before AdminClusterManagement.createFirstClusterMemberWithTemplate call."
	#endIF
	# Call AdminTask to create the cluster.
	AdminClusterManagement.createFirstClusterMemberWithTemplate(clusterName, nodeName, serverName, "default")
	if debug == "YES":
		print "After the AdminClusterManagement.createFirstClusterMemberWithTempate call and successful."
	#EndIf
#endTry
except:
	print "Exception with AdminClusterManagement.createFirstClusterMemberWithTemplate call. Cluster member not created."
	sys.exit(1)
#endExcept	

# Save the configuration change.
#
if debug == "YES":
		print "Created the first member.. ready to save to repository."
	#endIF
try:
	if debug == "YES":
		print "Before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
	if debug == "YES":
		print "After the successful save of the first cluster member."
	#EndIf
#endTry
except:
	print "Exception with AdminConfig.save call.  Changes not saved. No cluster member created."
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with first cluster member create."
	#endIF
sys.exit(0)