#************************************************************************
# Function: setJVMHeap -	Set JVM properties for a given server.
#		Min. and Max. JVM HeapSize values are passed in and set
#		for a given server JVM Java process definition.
#
# Description:	This function takes five parameters.
#
# Parameters:
#		nodeName	-	Name of the node where server resides
#		serverName	-	Name of the server to be changed
#		maxHeapsize	-	Max. JVM Heap size in MB.
#		initHeapsize	-	Initial JVM Heap size in MB. 
#		debug		-	debug value ( YES or NO ).
#
# Return Code:
#		0		-	JVM properties for Heap set OK.
#		1		-	Server does not exist in the cell.
#		2		-	AdminTask operation failed.
#
# *NOTE:  At this point this function only sets the Heap size.  Additional
#	parameters can be added to the optional parm list in the future for 
#	other JVM properties.
#
# Author:	Bruce J. Ryba  02/06/18
#
#**************************************************************************
def eSetJVMProperties( nodeName, serverName,initHeapsize,maxHeapsize,debug):
	
	if debug == "YES":
		print "inside setJvmProperties"
	#endIf
	
	# Check if server exists
        server = AdminConfig.getid("/Node:" +nodeName+"/Server:"+serverName+"/")
        if (len(server) == 0):
           # server does not exist
           if debug == "YES":
           	print "Server = ", serverName, " was not found."
           return 1
        #endIf

        # Construct required parameters
        requiredParamList = ['-serverName', serverName, '-nodeName', nodeName]
                
        # Construct optional parameters
        optionalParamList = []
    
        if (len(initHeapsize) != 0):
           optionalParamList =  ['-initialHeapSize', initHeapsize]
        if (len(maxHeapsize) != 0):
           optionalParamList = optionalParamList + ['-maximumHeapSize', maxHeapsize]
           
        print "before list extend"
        paramList = requiredParamList + optionalParamList     
        
        if debug == "YES":
		print "Parameter list is :"  
   		print paramList
   	#endIf
   	
       	# Set JVM properties
       	try:
       		if debug == "YES":
       			print "right before the AdminTask to set min and max."
       		#endIF
       		AdminTask.setJVMProperties(paramList)
           
        	AdminConfig.save()
        	if debug == "YES":
        		print "set and save completed."
        	#endIF
        #endTry
        except:
        	if debug == "YES":
        		print "Error with the Admin Task and save."
        	#endIf 
        	AdminConfig.reset()
        	return 2
        #endExcept
        if debug == "YES":
        	print " we have a successful set of the JVM min and max."
        #endIf 
        return 0

# main logic 

if __name__ == '__main__':
    if len(sys.argv) < 5:
    	print 'need node name, server name, JVM min, JVM max and debug'
        sys.exit(1)
        
debug=sys.argv[4]
if debug == "YES":
	print "args is :"
	for arg in sys.argv:
    		print arg
#endIF 

if debug == "YES":
	print "before the call to the set JVM heap function."
#endIF 
rtn = eSetJVMProperties( sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4])
if debug == "YES":
	print "back from jvm set and return code is = " + str(rtn)
#endIF 
sys.exit(rtn)