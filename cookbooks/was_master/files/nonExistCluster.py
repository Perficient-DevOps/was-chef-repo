

clusterName = sys.argv[0]
debug = sys.argv[1]
	
if debug == "YES":
	print "First check and see if we do not have a valid cluster."
#EndIf
# first check and see if the cluster already exists
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") != "":
	print "Cluster ", clusterName, " exists."
	sys.exit(1)
			

if debug == "YES":
		print "Cluster does not exist exists."
		print "Done with cluster check."
	#endIF
sys.exit(0)