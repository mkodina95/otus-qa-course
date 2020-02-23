import os
import sys
import subprocess
import argparse


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument(
        '--package',
        dest="package",
        default='selenium'
    )
    args.add_argument(
        '--directory',
        dest="directory",
        default='/Users/m.kodina'
    )
    args.add_argument(
        '--port',
        dest="port",
        default='22'
    )
    args.add_argument(
        '--service',
        dest="service",
        default='network'
    )
    return args.parse_args()


def get_info():

    args = parse_args()

    # netstat
    network_interface = subprocess.check_output('netstat -i', shell=True)
    # default path
    default_path = os.getenv('PATH')
    # cpu info
    cpu_info = subprocess.check_output('sysctl -n machdep.cpu.brand_string', shell=True).strip()
    # process info
    process_id = os.getpid()
    # list of processes
    current_processes = subprocess.check_output('ps aux', shell=True)
    # interfaces stat
    interface_stat = subprocess.check_output('ifconfig').strip()
    # service status
    service_status = subprocess.check_output(f'launchctl list | grep {args.service}',  shell=True)
    # port status
    port_status = subprocess.check_output(f'nmap scanme.nmap.org | grep {args.port}', shell=True)
    # python package version
    package_version = subprocess.check_output(f'pip freeze | grep {args.package}', shell=True)
    # list of files and dirs
    list_dir = os.listdir(args.directory)
    # current directory
    current_directory = os.getcwd()
    # core version
    core_version = sys.version.strip()
    # os version
    os_version = f'{os.uname()[0]} {os.uname()[2]}'

    return {
        'network_interfaces': network_interface,
        'default_path': default_path,
        'cpu_info': cpu_info,
        'process_id': process_id,
        'current_processes': current_processes,
        'interfaces_stat': interface_stat,
        'service_status': service_status,
        'port_status': port_status,
        'package_version': package_version,
        'dir_contains_list': list_dir,
        'current_directory': current_directory,
        'core_version': core_version,
        'os_version': os_version,
    }


os_info = get_info()

for item in os_info:
    print(f'{item}:  {os_info[item]}')
