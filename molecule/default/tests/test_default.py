import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_listening_http(host):
    socket = host.socket('tcp://0.0.0.0:80')
    assert socket.is_listening


def test_nginx_serving_content(host):
    assert host.addr("localhost").port(80).is_reachable
    result = host.check_output("http GET :80")
    assert "IPv4 addresses" in result
    assert "AppArmor" not in result
    assert "Environment Variables" not in result
