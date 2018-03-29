# # encoding: utf-8
# Inspec test for recipe was_master::prerequisites

describe user('wasadmin') do
  it { should exist }
end

describe group('wasadmin') do
  it { should exist }
end
