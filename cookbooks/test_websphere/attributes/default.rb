
default[:test_websphere][:install_repo_path]  = ''

default[:test_websphere][:install_location]   = '/opt/IBM/WebSphere/AppServer'
default[:test_websphere][:shared_location]    = '/opt/IBM/Shared'
default[:test_websphere][:install_profilename]= 'IBM WebSphere Application Server V8.5'
default[:test_websphere][:install_arch]       = 'x86'
default[:test_websphere][:install_profile_id] = 'com.ibm.websphere.ND.v85'
default[:test_websphere][:install_versiontag] = '8.5.5000.20130514_1044'

default[:test_websphere][:run_user]           = 'wasadmin'
default[:test_websphere][:run_user_passwd]    = '$3cr3t$!'
default[:test_websphere][:run_group]          = 'wasadmin'

default[:test_websphere][:dmgr_profilename]   = 'Dmgr001'
default[:test_websphere][:dmgr_node_name]     = 'Default01Node'
default[:test_websphere][:appsrv_profilename] = 'AppSrv01'
default[:test_websphere][:appsrv_node_name]   = 'Default02Node'
default[:test_websphere][:cell_name]          = 'Defaul01Cell'
