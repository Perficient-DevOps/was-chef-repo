# parameters: cluster name, node name , server name
clusterName = sys.argv[0]
serverName = sys.argv[1]
nodeName = sys.argv[2]
debug = sys.argv[3]
preferLocal="true"
createReplicationDomain="true"

# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist - please create first."
	sys.exit(1)

print "Creating first cluster member"

if debug == "YES":
		print "ready to create first member "
	#endIF

try:
	if debug == "YES":
		print "before AdminClusterManagement.createFirstClusterMemberWithTemplate call."
	#endIF
	# Call AdminTask to create the cluster.
	AdminClusterManagement.createFirstClusterMemberWithTemplate(clusterName, nodeName, serverName, "default")
#endTry
except:
	print "Exception with AdminClusterManagement.createFirstClusterMemberWithTemplate call."
	sys.exit(1)
#endExcept

# Save the configuration change.
#
if debug == "YES":
		print "Created the first member.. ready to save."
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
sys.exit(0)
