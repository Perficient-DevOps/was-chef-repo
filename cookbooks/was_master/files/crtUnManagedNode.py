
if __name__ == '__main__':
    print "amount of args passed in is ", sys.argv
    if len(sys.argv) < 4:
    	print 'Need node name, hostname, OS,  and debug'
        sys.exit(1)
        
debug=sys.argv[3]

if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

nodeV=sys.argv[0]
hostV=sys.argv[1]
osV=sys.argv[2]

if debug == "YES":
		print "Ready to create the unmanaged node. "
	#endIF
	
nodeId = AdminConfig.getid("/Node:" +nodeV)
print "after the get of the node and server and values is = ", nodeId
if (len(nodeId) != 0):
	# node exists 
        if debug == "YES":
           	print "Node   = ", nodeV, " already exists."
        sys.exit(1)
#endIf

# we do not have a node by this name yet, create the unmanaged node 
try:
	if debug == "YES":
		print "Before creation of unmanaged node."
	#endIF
	# Call AdminTask to create the cluster.
	AdminTask.createUnmanagedNode(['-nodeName', nodeV, '-hostName', hostV, 
	'-nodeOperatingSystem', osV])
	
#endTry
except:
	print "Exception with create unmanaged node  call."
	sys.exit(1)
#endExcept	

if debug == "YES":
	print "After the creation of the unmanaged node."
#EndIf 

# Save the configuration change.
#
if debug == "YES":
		print "Created the unmanaged node and now ready to save."
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
		print "Done with name unmanaged node creation."
	#endIF
sys.exit(0)