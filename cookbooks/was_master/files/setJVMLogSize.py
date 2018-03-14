
def setJVMLogSize( nodeName, serverName,log, sizeL,debug):
	
	if debug == "YES":
		print "inside setJVMLogSize"
	#endIf
	
	# Check if server exists
        server = AdminConfig.getid("/Node:" +nodeName+"/Server:"+serverName+"/")
        if (len(server) == 0):
           # server does not exist
           if debug == "YES":
           	print "Server = ", serverName, " was not found."
           return 1
        #endIf

	try:
		if debug == "YES":
			print "Before the show attribute of the log"
		#endIF
		# next we need to get the log of interest
		log = AdminConfig.showAttribute(server, log)
		if debug == "YES":
			print "After the get attribute of log  and value is = ", log
		#endIf
	#endTry
	except:
		print "Error with the showAttribute for log."
		return 1
	#endExcept

        # now lets update the rolloverSize for the log
        
        try:
		if debug == "YES":
			print "Before the show attribute of the log"
		#endIF
		# next we need to get the log of interest
		AdminConfig.modify(log,[['rolloverSize', sizeL]])
		if debug == "YES":
			print "After the modify of log  size."
		#endIf
	#endTry
	except:
		print "Error with modify server with new log size."
		return 1
	#endExcept
        
	try:
		# Save the configuration
		AdminConfig.save()
	
		if debug == "YES":
			print "Saved changes to repository."
		#endIF
	except:
		AdminConfig.reset()
		print "Failed to save changes, error with save operation - reset."
		return 2
        
        if debug == "YES":
        	print "set and save completed."
        
        return 0

# main logic
if __name__ == '__main__':
    if len(sys.argv) < 5:
    	print 'need node name, server name, log type, log size and debug'
        sys.exit(1)
        
debug=sys.argv[4]
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

print "args is :"
for arg in sys.argv:
    print arg
    
 
cell=AdminConfig.list('Cell')
print "cell is =", cell
cellName=AdminConfig.showAttribute(cell, 'name')
if debug == "YES":
		print "cell is =", cell
		print "cellname is = ",cellName
		print "before the test"
		print "server name =",sys.argv[1]
		print "node name =",sys.argv[0]
#endIF
# call function to set JVM log size
rtn = setJVMLogSize( sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3], sys.argv[4])
if debug == "YES":
		print "back from jvm set log size and return code is = " + str(rtn)
#endIF
	
print "done with script"
sys.exit(rtn)

