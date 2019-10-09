# -*- mode: ruby -*-
# vi: set ft=ruby :


# Simple Vagrant file for testing the Ansible role
Vagrant.configure("2") do |config|

  config.vm.define 'centos7' do |node|
    config.vm.provider "libvirt"
    node.vm.box = "centos/7"
    node.vm.network "forwarded_port", guest: 80, host: 8081
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
  config.vm.define 'ubuntu1804' do |node|
    config.vm.provider "libvirt"
    node.vm.box = "generic/ubuntu1804"
    node.vm.network "forwarded_port", guest: 80, host: 8083
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
  config.vm.define 'debian9' do |node|
    config.vm.provider "libvirt"
    node.vm.box = "generic/debian9"
    node.vm.network "forwarded_port", guest: 80, host: 8084
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yaml"
    end
  end
end
