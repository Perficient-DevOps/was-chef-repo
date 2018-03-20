

clusterName = sys.argv[0]
debug = sys.argv[1]
	
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	if debug == "YES":
		print "Cluster ", clusterName, " does not exist."
	#EndIf
	sys.exit(1)
			
if debug == "YES":
		print "Checked and cluster exists, now we need to delete."
	#endIF
	
#Build options list for -cluster step.
clusterConfigOptions = [clusterName]
	
try:
	if debug == "YES":
		print "before AdminTask.deleteCluster call."
	#endIF
	# Call AdminTask to create the cluster.
	AdminTask.deleteCluster(["-clusterName " + clusterName])
	if debug == "YES":
		print "After the AdminTask.deleteCluster call and cluster was deleted."
#endTry
except:
	print "Exception with AdminTask.deleteCluster call.  Cluster not deleted."
	sys.exit(1)
#endExcept	

# Save the configuration change.
#
if debug == "YES":
		print "Deleted cluster and am now ready to save configuration."
try:
	if debug == "YES":
		print "before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
	if debug == "YES":
		print "Configuration saved."
#endTry
except:
	print "Exception with AdminConfig.save call."
	sys.exit(1)
#endExcept	
	
if debug == "YES":
		print "Done with cluster delete operation."
	#endIF
sys.exit(0)