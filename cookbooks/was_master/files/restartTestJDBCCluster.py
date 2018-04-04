import time

clusterName = sys.argv[0]
dataSourceName = sys.argv[1]
debug = sys.argv[2]

	
# first check and see if the cluster already exists
if debug == "YES":
	print "First verify that we indeed have a valid cluster name."
#EndIf
if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
	print "Cluster ", clusterName, " does not exist.  Cannot restart cluster that does not exist."
	sys.exit(1)
		

if debug == "YES":
		print "***** Ready to stop  the cluster."
	#endIF
	
# check to see if the cluster is up
mycell = AdminControl.getCell()
clusterCON = AdminControl.completeObjectName('cell=' + mycell + ',type=Cluster,name=' + clusterName + ',*')

# query the state of the cluster
clusterState = AdminControl.getAttribute(clusterCON, 'state')

if debug == "YES":
	print "		Cluster state is =",clusterState
#EndIf

#bypass cluster stop if the state of the cluster is already stopped
if clusterState == "websphere.cluster.stopped":
	if debug == "YES":
		print "		Cluster " + clusterName + " is already in a stopped state."
	#EndIF
else:
	#we need to stop the cluster first 
	try:
		if debug == "YES":
			print "		Before AdminClusterManagement.stopSingleCluster call."
		#endIF
		# Call AdminClusterManagement.stopSingleCluster to start the cluster.
		AdminClusterManagement.stopSingleCluster(clusterName)
		if debug == "YES":
			print "		After AdminClusterManagement.stopSingleCluster call -successful. "
		#endIF
	#endTry
	except:
		print "		Exception with AdminClusterManagement.stopSingleCluster call.  Cluster not stopped."
		sys.exit(1)
	#endExcept	

time.sleep(60)

#now that we are done stopping the cluster, lets get a list of the nodes in the cluster

# Get configID of the cluster, we know it exists
cluster_conf_id = AdminConfig.getid("/ServerCluster:"+clusterName )

# Get confids of the cluster members
if debug == "YES":
		print "***** Before AdminConfig call to get list of cluster members"
#EndIf

# get the list of member in the cluster.  Then make a list of the nodes.
member_conf_ids = AdminConfig.showAttribute(cluster_conf_id, "members")
# AdminConfig returns the list in [], get rid of the brackets
member_conf_ids = member_conf_ids[1:-1]
#print "Cluster %s has following members:" % clusterName  
# split by space
nodeListNbr=0
nodeList = []

for member_conf_id in member_conf_ids.split():
    	# Obtain server name and node name
	member_name=AdminConfig.showAttribute(member_conf_id, "memberName")
   	node_name=AdminConfig.showAttribute(member_conf_id, "nodeName")
   	if debug == "YES":
   		print " Member and Node item is = ", node_name+"/"+member_name
   	if len(nodeList) == 0:
   		print "First node item add it to list of nodes for cluster."
   		nodeList.append(node_name)
   	#endIf
   	else:
   		#we have other nodes, make sure it is not there 
   		if debug == "YES":
   			print "Not the first node, another node to add - first check if there."
   		if node_name in nodeList:
   			if debug == "YES":
   				print "Node is already in list of nodes, do not add."
   			#EndIf
   		#EndIf
   		else:
   			#add node to node list=",node_name
   			if debug == "YES":
   				print "Adding another new node to list of nodes in cluster. "
   			#EndIf
   			nodeList.append(node_name)
   		#EndList
   	#EndElse
#EndFor

if debug == "YES":
	print "After the build of node list and value is = ", nodeList
	print "the length of the list is ", len(nodeList)
#EndIf

#now we need to go through the list of nodes and restart the node agents
if debug == "YES":
	print "Now we have to go through the list of nodes and restart the node agents."
#EndIf

#loop through the list of nodes and restart the node agent for the node. 
for node_item in nodeList:
	if debug == "YES":
		print "Node name = ",node_item, " will be restarted now."
	try:
		if debug == "YES":
			print "Before the restart of Node Agen = ",node_item
		#EndIf
		# restart the node agent
		AdminNodeManagement.restartNodeAgent(node_item)
		if debug == "YES":
			print "After call to restart Node agent = ", node_item
		#EndIf
	except:
		if debug == "YES":
			print "Error with restarting the node agent"
		#EndIf 
#EndFor 

#sleep for 60 seconds in order to wait for the node agents to be ready after restart
if debug == "YES":
	print "Wait for 60 seconds for the node agents to be ready after restart."
#EndIf
time.sleep(60)

#now restart the cluster 
clusterState = AdminControl.getAttribute(clusterCON, 'state')
print "Cluster state before the restart is =",clusterState



try:
	if debug == "YES":
		print "Before AdminClusterManagement.startSingleCluster call."
	#endIF
	# Call AdminClusterManagement.stopSingleCluster to start the cluster.
	AdminClusterManagement.startSingleCluster(clusterName)
	if debug == "YES":
		print "After AdminClusterManagement.startSingleCluster call -successful. "
	#endIF
#endTry
except:
	print "Exception with AdminClusterManagement.startSingleCluster call.  Cluster not started."
	#sys.exit(1)
#endExcept	

#sleep for about 60 seconds for cluster members to start 
time.sleep(60)

#Now we need to test the datasource connections on the cluster
# get a list of data sources defined for cluster scope and find the one that is ours
if debug == "YES":
	print "Data source list at cluster scope  is: ======",AdminConfig.list("DataSource",cluster_conf_id)
#EndIf

#place list in a list object - there might be more data sources defined at scope level cluster
dsList = AdminConfig.list("DataSource", cluster_conf_id).splitlines()
if debug == "YES":
	print "The list of data sources for cluster are: ", dsList
#EndIf

#now loop through the list of data sources at cluster level and find our datasource
foundDs = "False"

if debug == "YES":
	print "The length of the ds list is =",len(dsList)
#EndIf 

#loop through list and get name of datasource, provider name
for dsItem in dsList:
	if debug == "YES":
		print "Inside the datasource list looking for our datasource match."
		print "Working with datasource item = ",dsItem
	#EndIf
	
	#check and see if this is the datasource that we are after
	#pull name from datasource id and see if it matches our datasource
	dsMember_name=AdminConfig.showAttribute(dsItem, "name")
	dsProvider = AdminConfig.showAttribute(dsItem,"provider")
	dsProviderName = AdminConfig.showAttribute(dsProvider,"name")
	
	if debug == "YES":
		print "After the show attribute on the datasource."
		print "The datasource name for ",dsItem," is = ",dsMember_name,"."
		print "The provider for the datasource is =", dsProvider
		print "The provider name is = ",dsProviderName
	#EndIf
	
	#check and see if we have indeed a match with our datasource and item from list
	if dsMember_name == dataSourceName:
		if debug == "YES":
			print "We have a match on the datasource name."
			print "Before the test connection on the cluster scoped datasource ",dsMember_name
		#EndIf 
		
		#Build out containment path for the datasource so we can get the id for it
		proScopeValue = "/Cell:" + mycell + "/ServerCluster:" + clusterName
		dsIDname = proScopeValue + "/JDBCProvider:" + dsProviderName + "/DataSource:" + dsMember_name + "/"
		if debug == "YES":
			print "Datasource containment path is  = ",dsIDname
		#EndIF
	
		# retrieve internal id of datasource
		dsId = AdminConfig.getid(dsIDname)
		if debug == "YES":
			print "Datasource id is = ", dsId
		#Endif
		
		try:
			#now test the connection
			
			AdminControl.testConnection(dsId)
			if debug == "YES":
				print "After the test connection."
			foundDs = "True"
		#Endtry
		except:
			if debug == "YES":
				print "Error with testing data source connection ",dsMember_name
				print "Make sure that the datasource works correctly."
			#EndIf 
			sys.exit(1)
		#EndExcept
	else:
		if debug == "YES":
			print "Not a match for the item in datasource list and our datasource."
		#EndIf 
		
if foundDs == "False":
	if debug == "YES":
		print "We did not find a datasource ", datasourceName," at the cluster scope."
		print "Could not test the data source on all of the cluster nodes."
		sys.exit(1)
	#EndIf 
#EndIf
else:
	if debug == "YES":
		print "Successfully tested cluster level datasource."
	#EndIf
	
if debug == "YES":
		print "Done with cluster restart and testing of datasource. Please review test info."
	#endIF
sys.exit(0)