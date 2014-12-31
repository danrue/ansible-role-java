require 'serverspec'
set :backend, :exec

describe file('/opt/java/java6') do
  it { should be_symlink }
end

describe file('/opt/java/java7') do
  it { should be_symlink }
end

describe file('/opt/java/java8') do
  it { should be_symlink }
end
