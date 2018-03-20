
# parameters: cluster name, node name , server name 
clusterName = sys.argv[0]
serverName = sys.argv[1]
debug = sys.argv[2]

	
if debug == "YES":
	print "First check and see if cluster exists."
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist.  Please specify correct cluster name. "
	sys.exit(1)
		
	
if debug == "YES":
		print "eady to check if cluster member exists."
	#endIF
	
try:
	if debug == "YES":
		print "Before AdminClusterManagement.checkIfClusterMemberExists call."
	#endIF
	# Call AdminTask to create the cluster.
	rtn=AdminClusterManagement.checkIfClusterMemberExists(clusterName,serverName)
	if debug == "YES":
		print "After AdminClusterManagement.checkIfClusterMemberExists call with return value of ",rtn
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.checkIfClusterMemberExists call."
	sys.exit(1)
#endExcept	
#check and see if the cluster member is indeed in the cluster
if rtn == "false":
	if debug == "YES":
		print "We do not have a cluster member by the name of ", serverName," in the cluster ",clusterName
	#EndIf
	sys.exit(1)
#EndIf
if debug == "YES":
	print "Cluster member ", serverName, " exists in cluster ", clusterName, "."
	#endIF
if debug == "YES":
		print "Done with clusterMember exists."
	#endIF
sys.exit(0)