def test_service_removed(host):
    result = host.run("systemctl is-enabled test-service")
    assert result.rc == 4, (
        f"Service should be removed (expected rc 4, got {result.rc}). "
        f"stdout: {result.stdout}, stderr: {result.stderr}"
    )
    assert "not-found" in result.stdout


def test_service_unit_file_removed(host):
    unit_file = host.file("/etc/systemd/system/test-service.service")
    assert not unit_file.exists, "/etc/systemd/system/test-service.service should not exist after uninstallation"
