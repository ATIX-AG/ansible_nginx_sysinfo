import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx_serving_content(host):
    assert host.addr("localhost").port(80).is_reachable
    result = host.check_output("curl localhost:80")
    assert "IPv4 addresses" in result
    assert "AppArmor" in result
    assert "Environment variables" in result
