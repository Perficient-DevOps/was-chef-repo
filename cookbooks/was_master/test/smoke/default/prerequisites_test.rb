# # encoding: utf-8

# Inspec test for recipe was_master::prerequisites

# The Inspec reference, with examples and extensive documentation, can be
# found at http://inspec.io/docs/reference/resources/

describe user( 'wasadmin' ) do
  it { should exist }
end

describe group('wasadmin') do
  it { should exist }
end
