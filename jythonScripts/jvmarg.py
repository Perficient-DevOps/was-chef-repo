#
# TODO: enter JYTHON code and save
#
global AdminConfig
global AdminTask
global AdminControl
print 'instide test script '


#profile_path  = '<%= @profile_path %>'
#cell_name     = '<%= @cell_name %>'
cell_name = "STLSCVMG95219Cell01"
#node_name     = '<%= @node_name %>'
node_name = "STLSCVMG95219Node01"
#server_name   = '<%= @server_name %>'
server_name = "bruce"

print "before the cell_id"
cell_id          = AdminConfig.getid( '/Cell:%s' % (cell_name)  )
print "after cell id and value is " 
print cell_id
node_id          = AdminConfig.getid( '/Cell:%s/Node:%s' % ( cell_name, node_name ) )
print "after the node id and "
print node_id
server_id        = AdminConfig.getid( '/Cell:%s/Node:%s/Server:%s' % ( cell_name, node_name, server_name ) )
print "After the server_id and "
print server_id

processDef = AdminConfig.list('JavaProcessDef', server_id)
print "**"
print processDef
processDef = AdminConfig.showAttribute(server_id, 'processDefinitions')
print "----"
print processDef
## Update JVM Working Directory
# Find Process Def for this server
#process_definition_array = AdminConfig.showAttribute( server_id, 'processDefinitions')
print "After the process def array"
#print process_definiton_array
#process_def_id = process_definition_array[0]
print "After process def id "
#print process_def_id


#AdminConfig.modify( process_def_id, '[[executableTarget "com.ibm.ws.runtime.WsServer"] [executableName ""] [stopCommand ""] [stopCommandArgs ""] [terminateCommand ""] [workingDirectory "${PS_INSTALL_ROOT}"] [startCommandArgs ""] [executableArguments ""] [startCommand ""] [terminateCommandArgs ""] [processType ""]]')
#AdminConfig.modify( processDef, '[[executableTarget "com.ibm.ws.runtime.WsServer"] [executableName ""] [stopCommand ""] [stopCommandArgs ""] [terminateCommand ""] [workingDirectory "${PS_INSTALL_ROOT}"] [startCommandArgs ""] [executableArguments ""] [startCommand ""] [terminateCommandArgs ""] [processType ""]]')
print "After the process def modify...."
## Custom classpath & Enable Verbose Garbage collection

#custom_classpath = "%s/config/cells/%s/nodes/%s/servers/%s/process-server/config" % ( profile_path, cell_name, node_name, server_name )
#AdminTask.setJVMProperties('[-serverName %s -nodeName %s -classpath [%s ] -verboseModeClass false -verboseModeGarbageCollection true -verboseModeJNI false -initialHeapSize 512 -maximumHeapSize 1024 -runHProf false -hprofArguments -debugMode false -debugArgs "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7777" -genericJvmArguments -executableJarFileName -disableJIT false]' % ( server_name, node_name, custom_classpath ) )

## Add custom JVM properties

# Find JVM
#jvm_id = AdminConfig.list('JavaVirtualMachine', server_id )

# List current properties
# TODO: Check if the property already exists to avoid errors on adding an existing attribute
# AdminConfig.list('Property', jvm_id)

# Add new properties
#AdminConfig.create('Property', jvm_id, '[[validationExpression ""] [name "jvm.environment.name"] [description ""] [value "axwast20-qa6"] [required "false"]]')
#AdminConfig.create('Property', jvm_id, '[[validationExpression ""] [name "providerURL"] [description ""] [value "iiop://localhost:2809"] [required "false"]]')

# JVM arguments ( look specific to Dynatrace, so if this is created for every environment we can add it automatically )
# -agentpath:/var/WebSphere/dynatrace/dynatrace-5.6/aix-ppc-64/agent/lib64/libdtagent.so=name=AZ_BPM_QA2_All_AZLBPM.PS,server=awdntt01:9999

#AdminConfig.save()

