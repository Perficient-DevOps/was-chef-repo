# # encoding: utf-8
# Inspec test for recipe nrg_websphere::test_create_base_environment


# Things to validate WebSphere
# * Dmgr01 exists
# * Dmgr process is running
# * Dmgr is listing on soap_port
# * Node1 & Node2 exists


# Check Dmgr Profile
describe file( '/opt/IBM/WebSphere/AppServer/profiles/Dmgr01' ) do
 it { should be_directory }
 it { should be_owned_by 'wasadmin' }
end

describe processes( Regexp.new('^/opt/IBM/WebSphere/AppServer/java/bin/java .* dmgr$' ) ) do
  it { should exist }
  its('entries.length') { should eq 1 }
  its('users') { should include 'wasadmin' }
  # its('commands') { should match /dmgr/i }
end

describe port(14003) do
  it { should be_listening }
  its('processes') {should include 'java'}
end

# describe port(9060) do
#   it { should be_listening }
#   its('processes') {should include 'java'}
# end

# Check AppSrv Profile
describe file( '/opt/IBM/WebSphere/AppServer/profiles/Node1' ) do
 it { should be_directory }
 it { should be_owned_by 'wasadmin' }
end

describe processes( Regexp.new('^/opt/IBM/WebSphere/AppServer/java/bin/java .* Defaul01Cell Node1 nodeagent$' ) ) do
  it { should exist }
  its('entries.length') { should eq 1 }
  its('users') { should include 'wasadmin' }
  #its('commands') { should match /Node1/ }
end

describe port(14053) do
  it { should be_listening }
  its('processes') {should include 'java'}
end

describe file( '/opt/IBM/WebSphere/AppServer/profiles/Node2' ) do
 it { should be_directory }
 it { should be_owned_by 'wasadmin' }
end

describe port(14153) do
  it { should be_listening }
  its('processes') {should include 'java'}
end
