#
# TODO: enter JYTHON code and save
#
import sys
global AdminConfig
global AdminTask
 
if __name__ == '__main__':
    if len(sys.argv) < 4:
    	print 'need virtual host name, hostname, port, and debug '
        sys.exit(1)
        
print "args is :"
for arg in sys.argv:
    print arg
    
 

virtualHostName = sys.argv[0]
hostName=sys.argv[1]
portValue=sys.argv[2]
debug=sys.argv[3]

if debug=="YES":
	print "hostNames is = ", hostName
	print "portValue is = ",portValue
	print "virtualHostName is = ", virtualHostName
#endIf 


cell=AdminConfig.list('Cell')
#print "cell is =", cell
cellName=AdminConfig.showAttribute(cell, 'name')
#print "cellname is = ",cellName
#print "before the get of the id for default host"

#first check and see if we have a valied virtual host to update
# first check and see if the cluster already exists
if debug == "YES":
	print "First check and see if we have a valid virtual host name."
#EndIf
hostID=AdminConfig.getid('/Cell:'+cellName+'/VirtualHost:' + virtualHostName + '/')
if hostID == "":
	print "Virtual Host  ", virtualHostName, " does not exist."
	sys.exit(1)
if debug == "YES":
	print "We have a valid virtual host name, now lets update the host alias."
#EndIf		
# we have valid virtual host - lets add host name and port to alias.

if debug == "YES":
       	print "right before the AdminConfig to set VirtualHostInfo"
#endIF
try:
	if debug == "YES":
		print "before AdminConfig to set virtual host."
	#endIF
	AdminConfig.create('HostAlias', hostID, '[[hostname '+hostName+'] [port '+portValue+']]') 
	if debug == "YES":
		print "After AdminConfig to set virtual host - successful."
	#endIF
#endTry
except:
	print "Exception with AdminConfig.create  call."
	print "Error with the Admin config create host alias- reset repository."
	sys.exit(1)
#endExcept

# Save the configuration change.
#
if debug == "YES":
		print "Created the virtual host entry  and ready to save."
	#endIF
try:
	if debug == "YES":
		print "Before AdminConfig.save."
	#endIF
	# Call save
	AdminConfig.save()
	if debug == "YES":
		print "After AdminConfig.save - successful."
	#endIF
#endTry
except:
	print "Exception with AdminConfig.save call."
	sys.exit(1)
#endExcept

print "Done with script setVirtualHost"
sys.exit(0)

