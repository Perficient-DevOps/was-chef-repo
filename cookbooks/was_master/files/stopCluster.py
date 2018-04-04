

clusterName = sys.argv[0]
debug = sys.argv[1]

if debug == "YES":
	print "First check and see if we have a valid cluster name."
#EndIf	
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist, please specify a valid cluster name."
	sys.exit(1)
			

if debug == "YES":
		print "Ready to stop the cluster."
	#endIF
	
try:
	if debug == "YES":
		print "Before AdminClusterManagement.stopSingleCluster call."
	#endIF
	# Call AdminClusterManagement.stopSingleCluster to start the cluster.
	AdminClusterManagement.stopSingleCluster(clusterName)
	if debug == "YES":
		print "After AdminClusterManagement.stopSingleCluster call - successful."
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.stopSingleCluster call."
	sys.exit(1)
#endExcept	

	
if debug == "YES":
		print "Done with cluster stop."
	#endIF
sys.exit(0)