

clusterName = sys.argv[0]
debug = sys.argv[1]
	
if debug == "YES":
	print "First check and see if we have a valid cluster."
#EndIf
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist.  Please specify valid cluster name."
	sys.exit(1)
			

if debug == "YES":
		print "Cluster exists."
		print "Done with cluster check."
	#endIF
sys.exit(0)