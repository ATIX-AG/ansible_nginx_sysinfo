# simple ansible role for deploying nginx

The ansible role in this repository provisions a given host with
nginx, installs a website with basic information about the host
extracted from the facts and starts the service.

For testing purpose there is a Vagrantfile provided. It directly
accesses the role for provisioning the boxes.

```
vagrant up
```

will start four libvirt Vagrantboxes running CentOS7, Ubuntu 18.04 and Debian 9. A portmapping to ports 8081 - 8084 makes
the installed nginx accessible from the host.
