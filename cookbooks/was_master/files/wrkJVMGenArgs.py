
############################################################################
# 
# Parameters:  Node name, server name, debug, jvm args to be added , and removed
#
# wsadmin -language=jython -f was_jvm.py "nodeName" "serverName" "YES" \
# JVM_ARGS="-Xgcpolicy:gencon -Xcompressedrefs" \ 
# JVM_RM_ARGS="-Xhealthcenter"
#
# if provided argument exists, it will be updated.
# if it does not exit, it will be added
# 
# JVM_ARGS="" are the arguments that you would like to add or change
# JVM_RM_ARGS="" are arguments that you would like to have removed 
############################################################################
global AdminConfig
global AdminTask
global AdminControl 


 
# default parameters
pars = { 
	'JVM_ARGS'     : '',
	'JVM_RM_ARGS'  : ''
 
}
 
if sys.argv[2] == "YES":
	DEBUG = 1
else:
	DEBUG = 0
 
#########################################################
# update defaults from command line
#########################################################
for arg in sys.argv:
	arr = arg.split("=", 1)
	if len(arr) > 1:
		pars[arr[0].upper()] = arr[1]
 
 
if DEBUG :
	for key in pars.keys():
		print key + " = '" + pars[key] + "'"
 
 
#########################################################
# Parse JVM Args
#########################################################
jvm_pars = {}
jvm_rm_pars = {}
 
for jvm_par in pars['JVM_ARGS'].split() :
	pair = jvm_par.split(":", 1)
	jvm_pars[pair[0]] = pair
 
for jvm_par in pars['JVM_RM_ARGS'].split() :
	pair = jvm_par.split(":", 1)
	jvm_rm_pars[pair[0]] = pair
 
if DEBUG:
	for key in jvm_pars.keys() :
		pair = jvm_pars[key]
		if len(pair) > 1 :
			print "Key='" + pair[0] + "', value='" + pair[1] + "'"
		else :
			print "Key='" + pair[0] + "'"
 
	for key in jvm_rm_pars.keys() :
		pair = jvm_rm_pars[key]
		if len(pair) > 1 :
			print "RM Key='" + pair[0] + "', value='" + pair[1] + "'"
		else :
			print "RM Key='" + pair[0] + "'"
# end if
 
#########################################################
# Java Virtual Machine configurations                   #
#########################################################

 
# we need to check and see if node and server exists first
# Check if server exists
if DEBUG:
	print "Before the verfication of the Node and Server"
#EndIf
# check and see if we have a valid server and node name
server_id = AdminConfig.getid("/Node:" +sys.argv[0]+"/Server:"+sys.argv[1]+"/")
if (len(server_id) == 0):
	# server does not exist
        if DEBUG:
        	print "Server = ", sys.argv[1], " was not found."
        	sys.exit(1)
        #EndIf
else:
	print "We do have a valid server and node name."
#Endif
# next lets get the java virtual machine information
jvm = AdminConfig.list('JavaVirtualMachine',server_id)
 
#########################################################
# Set recommended JVM args                              #
#########################################################
jvm_args = {}
try:
	_excp_ = 0
	result = AdminConfig.showAttribute(jvm, 'genericJvmArguments')
	print "\nCurrent JVM Settings: " + result + "\n"
	newJvmSettings = []
	params = result.split()
	for param in params :
		pair = param.split(':', 1)
		key = pair[0]
		jvm_args[key] = 1
		if jvm_rm_pars.get(key) == None :
			if jvm_pars.get(key) == None :
				newJvmSettings.append(param)
			else :
				pair = jvm_pars[key]
				newParam = key
				if len(pair) > 1 :
					newParam += ":" + pair[1]
				# end if
				newJvmSettings.append(newParam)
			# end if
		# end if
	# end for
	for key in jvm_pars.keys() :
		if jvm_args.get(key) == None :
			# new argument has not been set yet
			# in it is not in the list of args to be removed
			if jvm_rm_pars.get(key) == None :
				pair = jvm_pars[key]
				newParam = key
				if len(pair) > 1 :
					newParam += ":" + pair[1]
				# end if
				newJvmSettings.append(newParam)
			# end if	
		# end if
	# end for
	newJvmSettingsString = " ".join(newJvmSettings)
	print "New JVM Settings: " + newJvmSettingsString + "\n"
 
	result = AdminConfig.modify(jvm, [['genericJvmArguments', newJvmSettingsString]])
	if DEBUG:
		print "Successfully modified the generic arguments. - after the AdminConfig.modify."
	#EndIf 
except:
	_type_, _value_, _tbck_ = sys.exc_info()
	result = `_value_`
	_excp_ = 1
#endTry 
if (_excp_ ):
	print "Error setting JVM args"
	print "Error = "+result
	sys.exit(1)
#endIf
	
 
# save configuration
try:
	if DEBUG:
		print "before the save of the configuration"
	#endIf 
	AdminConfig.save()
	if DEBUG:
		print "After the AdminConfig.save() - successful change and save. "
	#endIf
#endTry
except:
	if DEBUG:
		print " We have an exception with the AdminConfig.save operation. Unsuccessful argument add/change/remove."
	#endIf
	sys.exit(1)
#endExcept

sys.exit(0)