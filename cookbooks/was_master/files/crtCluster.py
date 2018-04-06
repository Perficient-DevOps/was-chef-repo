

clusterName = sys.argv[0]
debug = sys.argv[1]
preferLocal="true"
createReplicationDomain="true"
	
# first check and see if the cluster already exists
if debug == "YES":
	print "First check and see if cluster exists."
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") != "":
	print "Cluster ", clusterName, " already exists."
	sys.exit(1)
		
	
#Build options list for -clusterConfig step.
clusterConfigOptions = [clusterName, preferLocal]
	
#Build options list for -replicationDomain step.
replicationDomainOptions = []	


if debug == "YES":
		print "Ready to create the cluster "
	#endIF
	
try:
	if debug == "YES":
		print "before AdminClusterManagement.createClusterWithoutMember call."
	#endIF
	# Call AdminTask to create the cluster.
	#AdminTask.createCluster(["-clusterConfig",[clusterConfigOptions]])
	AdminClusterManagement.createClusterWithoutMember(clusterName)
	if debug == "YES":
		print "After call to AdminClusterManagement.createClusterWithoutMember call and OK."
	#EndIf
#endTry
except:
	print "Exception with AdminClusterManagement.createClusterWithoutMember call. Do not save configuration."
	sys.exit(1)
#endExcept	

if debug == "YES":
	print "Cluster created, now going to save the configuration."
#EndIf
# Save the configuration change.
#
try:
	if debug == "YES":
		print "Before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
	if debug == "YES":
		print "After the save of the configuration."
#endTry
except:
	print "Exception with AdminConfig.save call. Do not save the configuration."
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with cluster create and save."
	#endIF
sys.exit(0)