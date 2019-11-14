# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  config.vm.provider "virtualbox" do |v|
      v.name = "python-dev"
      v.memory = 2048
      v.cpus = 2
  end
  
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision "shell", path: "vagrant-install.sh", privileged: false

end
