default['was']['profile_name']  = 'Chef2Node1'
default['was']['install_home']  = '/opt/IBM/WAS8.5.5/'

default['was']['cell_name']     = 'STLSCVMG02100Cell02'
default['was']['node_name']     = 'STLSCVMG02100Node02'
default['was']['server_name']   = 'rory'
default['was']['was_user']      = 'admin'
default['was']['was_pass]']      = ''
default['was']['soap_port']     = '12003'

default['was']['profile_path']  = File.join( node['was']['install_home'], 'profiles', node['was']['profile_name'] )


#default['start_server']['profile_path']  = '/opt/IBM/WAS8.5.5/profiles/Chef2Node1'
#default['start_server']['profile_name'] = 'Chef2Node1'
