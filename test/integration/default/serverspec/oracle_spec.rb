require 'serverspec'
set :backend, :exec

describe file('/tmp/jdk-7u71-linux-x64.gz') do
  it { should be_file }
end

describe file('/opt/java/jdk1.7.0_71') do
  it { should be_directory }
end

describe file('/opt/java/jdk1.7.0_71/bin/java') do
  it { should be_file }
end

describe file('/tmp/jdk-8u25-linux-x64.gz') do
  it { should be_file }
end

describe file('/opt/java/jdk1.8.0_25') do
  it { should be_directory }
end

describe file('/opt/java/jdk1.8.0_25/bin/java') do
  it { should be_file }
end