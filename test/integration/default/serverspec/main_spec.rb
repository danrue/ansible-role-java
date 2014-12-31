require 'serverspec'
set :backend, :exec

describe package('python-boto') do
  it {should be_installed }
end

describe file('/opt/java') do
  it { should be_directory }
end


