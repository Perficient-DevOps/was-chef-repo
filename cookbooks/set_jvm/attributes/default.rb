default['set_jvm']['profile_name']  = 'Chef2Node1'
default['set_jvm']['install_home']  = '/opt/IBM/WAS8.5.5/'

default['set_jvm']['cell_name']     = 'STLSCVMG02100Cell02'
default['set_jvm']['node_name']     = 'STLSCVMG02100Node02'
default['set_jvm']['server_name']   = 'rory'
default['set_jvm']['was_user']      = 'admin'
default['set_jvm']['was_pass]']      = ''
default['set_jvm']['soap_port']     = '12003'

default['set_jvm']['profile_path']  = File.join( node['set_jvm']['install_home'], 'profiles', node['set_jvm']['profile_name'] )
