

clusterName = sys.argv[0]
debug = sys.argv[1]

	
# first check and see if the cluster already exists
if debug == "YES":
	print "First verify that we indeed have a valid cluster name."
#EndIf
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist.  Cannot start cluster that does not exist."
	sys.exit(1)
		
		

if debug == "YES":
		print "Ready to start the cluster "
	#endIF
	
try:
	if debug == "YES":
		print "Before AdminClusterManagement.startSingleCluster call."
	#endIF
	# Call AdminClusterManagement.startSingleCluster to start the cluster.
	AdminClusterManagement.startSingleCluster(clusterName)
	if debug == "YES":
		print "After AdminClusterManagement.startSingleCluster call -successful. "
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.startSingleCluster call.  Cluster not started."
	sys.exit(1)
#endExcept	
	
	
if debug == "YES":
		print "Done with cluster start operation."
	#endIF
sys.exit(0)