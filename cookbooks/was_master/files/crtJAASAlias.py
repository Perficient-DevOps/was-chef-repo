

if __name__ == '__main__':
    if len(sys.argv) < 5:
    	print 'alias name, user name, password , and debug '
        sys.exit(1)
        
print "args is :"
for arg in sys.argv:
    print arg
    
aliasName=sys.argv[0]
userName=sys.argv[1]
psswName=sys.argv[2]
desName=sys.argv[3]
debug=sys.argv[4]

print "Creating JAAS alias: " + aliasName
	
# Get name of cell using AdminControl
cell = AdminControl.getCell()
	
# Get configuration ID for the parent of the JAAS alias, Security
security = AdminConfig.getid("/Cell:" + cell + "/Security:/")
	
# Create and initialize variables used as
# new alias parameters
alias=["alias", aliasName]
userid=["userId", userName]
password=["password",psswName]
descript=["description",desName]
	
# Assemble the above variables into a list 
jaasAttrs=[alias, userid, password, descript]
	
try:
	if debug == "YES":
		print "Before the call to create the JAAS entry."
	#endIF
	# Use AdminConfig to create the JAAS alias
	AdminConfig.create('JAASAuthData', security, jaasAttrs)
	if debug == "YES":
		print "Created JAAS alias: " + aliasName
	#endIF
except:
	if debug == "YES":
		print "Could not create JAAS alias: " + aliasName
		print "possibly because it already exists..." 
	#endIf
	sys.exit(1)
#endExcept 
		
if debug == "YES":
		print "Created the JAAS and ready to save."
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
	print "Successfully created JAAS entry."
#EndIf		
sys.exit(0)
	