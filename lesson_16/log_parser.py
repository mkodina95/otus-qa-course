""" The file contains log parser"""
import argparse
import glob
import re
import json


parser = argparse.ArgumentParser(description="Parser")
parser.add_argument(
    "--file",
    dest="file",
    action="store",
    help="Path to logfile"
)
parser.add_argument(
    "--dir",
    dest="dir",
    action="store",
    help="Path to dir"
)
args = parser.parse_args()


if args.file is not None and args.dir is not None:
    print("Use only dir or file")
    exit(0)

dir_log_files = []

if args.file is not None:
    dir_log_files = [args.file]

if args.dir is not None:
    dir_log_files = [f for f in glob.glob(args.dir + "**/*_log")]

HOST = r'^(?P<host>.*?)'
SPACE = r'\s'
IDENTITY = r'\S+'
USER = r'\S+'
TIME = r'\[(?P<time>.*?)\]'
METHOD = r'\"(?P<method>(POST|GET|PUT|DELETE|HEAD))'
URL = r'(?P<url>.*?)\"'
STATUS = r'(?P<status>\d{3})'
SIZE = r'(?P<size>\S+)'

REGEX = HOST+SPACE+IDENTITY+SPACE+USER+SPACE+TIME+SPACE+METHOD+URL+SPACE+STATUS+SPACE+SIZE+SPACE

dict_result = {}
total_count_requests = 0
dict_by_type_method_count_request = {}
dict_request_count = {}
list_request = []

for f in dir_log_files:
    with open(f) as file:
        for index, line in enumerate(file.readlines()):
            match = re.search(REGEX, line)
            if match is None:
                continue

            ip = match.group('host')
            time = match.group('time')
            method = match.group('method')
            url = match.group('url')
            status = match.group('status')
            size = match.group('size')

            try:
                size = int(size)
            except ValueError:
                size = 0

            try:
                status = int(status)
            except ValueError:
                size = -1

            # total amount of the requests
            total_count_requests += 1

            # amount of requests by type: GET - 20, POST - 10
            if dict_by_type_method_count_request.get(ip, None) is None:
                dict_by_type_method_count_request[ip] = {
                    "GET": 0,
                    "POST": 0,
                    "PUT": 0,
                    "DELETE": 0,
                    "HEAD": 0
                }
            dict_by_type_method_count_request[ip][method] += 1

            # list of IP's
            if dict_request_count.get(ip, None) is None:
                dict_request_count[ip] = 0
            dict_request_count[ip] += 1

            # list of requests by size
            list_request.append((size, status, method, ip, url, time))


dict_request_count = {k: v for k, v in sorted(dict_request_count.items(), key=lambda item: item[1], reverse=True)}
request_by_size = sorted(list_request, key=lambda tup: tup[0], reverse=True)


dict_result["Total requests"] = total_count_requests
dict_result["IPs by type method count request"] = dict_by_type_method_count_request
dict_result["Top IPs by count request:"] = list(dict_request_count.keys())[:10]
dict_result["Top request by size"] = list(map(lambda x: (x[0], x[2], x[3], x[4], x[5]), request_by_size[:10]))
dict_result["Top request by client errors"] = list(map(
    lambda y: (y[1], y[2], y[3], y[4]),
    filter(lambda x: 400 <= x[1] < 500, list_request)))[:10]
dict_result["Top request by server errors"] = list(map(
    lambda y: (y[1], y[2], y[3], y[4]),
    filter(lambda x: 500 <= x[1] < 600, list_request)))[:10]


with open('res.json', 'w') as f:
    json.dump(dict_result, f, indent=4)
