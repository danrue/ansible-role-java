require 'serverspec'
set :backend, :exec

describe file('/tmp/jdk-6u45-linux-x64.bin') do
  it { should be_file }
end

describe file('/opt/java/jdk1.6.0_45') do
  it { should be_directory }
end

describe file('/opt/java/jdk1.6.0_45/bin/java') do
  it { should be_file }
end