#*************************************************************************
# Script: setJVMGenArgs.py - Set JVM generic arguments
#
# Description:   Script to set the generic JVM arguments for a server 
#
# Parameters:
#		Script takes three parameters.
#		1) Node name
#		2) Server name
#		3) Argument string - JVM arguments.
#		4) Debug "YES" or "NO" for printing debug statements for script 
#
# Return Codes:
#		0 = Completed without errors
#		2 = Error with one of the parameters
#			*NOTE:  Error processing will validate web application name, 
#				node name and server name for valid objects.   If 
#				there is an error, a corresponding error message will be printed 
#				indicating the incorrect parameter.
#
# Invocation Example:
#		wsadmin.sh ( or .bat ) -profileName Dmgr -lang jython 
#			/ -f setJVMGenArgs.py "mnNode" "myServer"
#                       /  "[-Dsun.net.http.allowRestrictedHeaders=true -Dlog4j.configuration=file:/opt/IBM/BPM/rybalog4j.xml]" 
#                       /  "YES"
# Author:
#	Bruce Ryba
# Date: 02/07/2018
#
#################################################################################
def eSetJVMGenericArgs( nodeName, serverName, genArg,debug):
	
	if debug == "YES":
		print "inside setJvmGenericArgs"
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
    
        if (len(genArg) != 0):
           optionalParamList =  ['-genericJvmArguments', genArg]
        
           
        print "before list extend"
        paramList = requiredParamList + optionalParamList     
        
        if debug == "YES":
		print "Parameter list is :"  
   		print paramList
   	#endIf
   	
       	# Set JVM properties
       	#try:
       	if debug == "YES":
       		print "right before the AdminTask to set generic JVM arguments."
       	#endIF
       	AdminTask.setJVMProperties(paramList)
           
        AdminConfig.save()
        if debug == "YES":
        	print "set and save completed."
        #endIF
        #endTry
        #except:
        	#if debug == "YES":
        	#	print "Error with the Admin Task and save."
        	#endIf 
        	#AdminConfig.reset()
        	#return 2
        #endExcept
        if debug == "YES":
        	print " we have a successful set the generic JVM Arguments. "
        #endIf 
        return 0

# main logic
if __name__ == '__main__':
    if len(sys.argv) < 4:
    	print 'need node name, server name, generic arguments and debug'
        sys.exit(1)
        
debug=sys.argv[3]
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
# call function to set JVM generic arguments
rtn = eSetJVMGenericArgs( sys.argv[0], sys.argv[1], sys.argv[2],sys.argv[3])
if debug == "YES":
		print "back from jvm set generic args and return code is = " + str(rtn)
#endIF
	
print "done with script"
sys.exit(rtn)

