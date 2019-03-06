# -*- mode: ruby -*-
# vi: set ft=ruby :


# Simple Vagrant file for testing the Ansible role
Vagrant.configure("2") do |config|

  config.vm.define 'centos7' do |node|
    node.vm.box = "geerlingguy/centos7"
    node.vm.network "forwarded_port", guest: 80, host: 8081
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
  
  config.vm.define 'ubuntu1604' do |node|
    node.vm.box = "geerlingguy/ubuntu1604"
    node.vm.network "forwarded_port", guest: 80, host: 8082
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
  
  config.vm.define 'ubuntu1804' do |node|
    node.vm.box = "geerlingguy/ubuntu1804"
    node.vm.network "forwarded_port", guest: 80, host: 8083
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
  
  config.vm.define 'debian9' do |node|
    node.vm.box = "geerlingguy/debian9"
    node.vm.network "forwarded_port", guest: 80, host: 8084
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
  
end
