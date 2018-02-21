
clusterName = sys.argv[0]
debug = sys.argv[1]


# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist."
	sys.exit(1)

print "Starting cluster"


if debug == "YES":
		print "ready to start the cluster "
	#endIF

try:
	if debug == "YES":
		print "before AdminClusterManagement.startSingleCluster call."
	#endIF
	# Call AdminClusterManagement.startSingleCluster to start the cluster.
	AdminClusterManagement.startSingleCluster(clusterName)
#endTry
except:
	print "Exception with AdminClusterManagement.startSingleCluster call."
	sys.exit(1)
#endExcept

# Save the configuration change.
#
if debug == "YES":
		print "Started the cluster and ready to save."
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
		print "Done with cluster start."
	#endIF
sys.exit(0)
