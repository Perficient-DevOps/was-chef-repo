clusterName = sys.argv[0]
debug = sys.argv[1]

# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist."
	sys.exit(1)

if debug == "YES":
		print "ready to delete  the cluster "
	#endIF

#Build options list for -cluster step.
clusterConfigOptions = [clusterName]

try:
	if debug == "YES":
		print "before AdminTask.deleteCluster call."
	#endIF
	# Call AdminTask to create the cluster.
	AdminTask.deleteCluster(["-clusterName " + clusterName])
#endTry
except:
	print "Exception with AdminTask.deleteCluster call."
	sys.exit(1)
#endExcept

# Save the configuration change.
#
if debug == "YES":
		print "Deleted cluster and am now ready to save."
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
		print "Done with cluster delete."
	#endIF
sys.exit(0)
