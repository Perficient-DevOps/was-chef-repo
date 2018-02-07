# # encoding: utf-8

# Inspec test for recipe test_websphere::install

# The Inspec reference, with examples and extensive documentation, can be
# found at http://inspec.io/docs/reference/resources/

# Check Dmgr Profile
describe file( '/opt/IBM/WebSphere/AppServer/profiles/Dmgr001' ) do
 it { should be_directory }
 it { should be_owned_by 'wasadmin' }
end

describe port(9043) do
  it { should be_listening }
  its('processes') {should include 'java'}
end

describe port(9060) do
  it { should be_listening }
  its('processes') {should include 'java'}
end

# Check Dmgr Profile
describe file( '/opt/IBM/WebSphere/AppServer/profiles/AppSrv01' ) do
 it { should be_directory }
 it { should be_owned_by 'wasadmin' }
end
