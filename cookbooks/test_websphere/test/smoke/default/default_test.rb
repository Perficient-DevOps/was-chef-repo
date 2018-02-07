# # encoding: utf-8

# Inspec test for recipe test_websphere::default

# The Inspec reference, with examples and extensive documentation, can be
# found at http://inspec.io/docs/reference/resources/

# WAS Console
describe port(9043) do
  it { should be_listening }
end
