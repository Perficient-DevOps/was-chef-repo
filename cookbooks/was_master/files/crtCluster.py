clusterName = sys.argv[0]
debug = sys.argv[1]
preferLocal="true"
createReplicationDomain="true"

# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") != "":
	print "Cluster ", clusterName, " already exists."
	sys.exit(1)

print "Creating cluster"

#Build options list for -clusterConfig step.
clusterConfigOptions = [clusterName, preferLocal]

#Build options list for -replicationDomain step.
replicationDomainOptions = []


if debug == "YES":
		print "ready to create the cluster "
	#endIF

try:
	if debug == "YES":
		print "before AdminTask.createCluster call."
	#endIF
	# Call AdminTask to create the cluster.
	AdminTask.createCluster(["-clusterConfig",[clusterConfigOptions]])
#endTry
except:
	print "Exception with AdminTask.createCluster call."
	sys.exit(1)
#endExcept

# Save the configuration change.
#
if debug == "YES":
		print "Created the cluster and ready to save."
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
		print "Done with cluster create."
	#endIF
