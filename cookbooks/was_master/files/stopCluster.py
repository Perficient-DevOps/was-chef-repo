clusterName = sys.argv[0]
debug = sys.argv[1]


# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist."
	sys.exit(1)

print "Stopping cluster"


if debug == "YES":
		print "ready to stop the cluster "
	#endIF

try:
	if debug == "YES":
		print "before AdminClusterManagement.stopSingleCluster call."
	#endIF
	# Call AdminClusterManagement.stopSingleCluster to start the cluster.
	AdminClusterManagement.stopSingleCluster(clusterName)
#endTry
except:
	print "Exception with AdminClusterManagement.stopSingleCluster call."
	sys.exit(1)
#endExcept

# Save the configuration change.
#
if debug == "YES":
		print "Stopped the cluster and ready to save."
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
		print "Done with cluster stop."
	#endIF
sys.exit(0)
