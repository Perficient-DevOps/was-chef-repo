
default[:test_websphere][:install_path]       = '/opt/IBM/WebSphere/AppServer'
default[:test_websphere][:run_user]           = 'wasadmin'
default[:test_websphere][:run_user_passwd]    = '$3cr3t$!'
default[:test_websphere][:run_group]          = 'wasadmin'


default[:test_websphere][:dmgr_profilename]   = 'Dmgr001'
default[:test_websphere][:dmgr_node_name]     = 'Default01Node'
default[:test_websphere][:appsrv_profilename] = 'AppSrv01'
default[:test_websphere][:appsrv_node_name]   = 'Default02Node'
default[:test_websphere][:cell_name]          = 'Defaul01Cell'
