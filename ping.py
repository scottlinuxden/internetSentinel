import os
import shlex
import subprocess

if os.name == 'posix':
    WAIT_TIMEOUT = 1
else:
    WAIT_TIMEOUT = 1000


def host(ip_address):
    """
    Pings a network server with the specified ip_address
    Args:
        ip_address: IP Address of the network server to ping

    Returns: 'found' if the internet server could be pinged or 'not found' otherwise

    """

    status = 'not found'
    command = "/bin/ping -n -c %d -W %d %s" % \
              (3, WAIT_TIMEOUT, ip_address)

    process = subprocess.Popen(shlex.split(command),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    output_lines = []

    while True:

        output = process.stdout.readline().decode('utf-8')
        if output == '' and process.poll() is not None:
            break
        if output:
            output_lines.append(output.strip())

    rc = process.poll()

    for line in output_lines:

        if line.find(ip_address) and line.find("bytes from") > -1:
            status = 'found'
            break

        elif line.find(ip_address) and \
                (line.find("Unreachable") > -1 or
                 line.find("100% packet loss") > -1 or
                 line.find("100.0% packet loss") > -1):  # No response from host
            status = 'not found'
            break

    return status


if __name__ == '__main__':
    host('1.2.3.4')
