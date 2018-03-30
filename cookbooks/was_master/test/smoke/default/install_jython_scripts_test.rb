# # encoding: utf-8
# Inspec test for recipe was_master::install_jython_scripts

#path = File.join( Chef::Config[:file_cache_path], 'jythonScripts' )
path = File.join( '/tmp/kitchen/cache', 'jythonScripts' )

describe file(path) do
  its('type') { should cmp :directory }
end
