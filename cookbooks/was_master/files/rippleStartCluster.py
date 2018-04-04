

clusterName = sys.argv[0]
debug = sys.argv[1]

if debug == "YES":
	print "First check and see if we have a valid cluster name."
#EndIf
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist.  Please specify valid cluster name. "
	sys.exit(1)
		
if debug == "YES":
		print "Ready to ripple start  the cluster "
	#endIF
	
try:
	if debug == "YES":
		print "Before AdminClusterManagement.rippleStartSingleCluster call."
	#endIF
	# Call AdminClusterManagement.rippleStartSingleCluster to start the cluster.
	AdminClusterManagement.rippleStartSingleCluster(clusterName)
	if debug == "YES":
		print "After AdminClusterManagement.rippleStartSingleCluster call - successful."
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.rippleStartSingleCluster call."
	sys.exit(1)
#endExcept	

	
if debug == "YES":
		print "Done with rippleStartSingleCluster."
	#endIF
sys.exit(0)