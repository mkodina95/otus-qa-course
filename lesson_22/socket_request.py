import argparse
import socket
import ssl


def parse_args():
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument(
        "--url",
        action="store",
        dest="url",
        help="Request url"
    )
    parser.add_argument(
        "--method",
        action="store",
        dest="method",
        help="Request method"
    )
    parser.add_argument(
        "--host",
        action="store",
        dest="host",
        help="Request host"
    )
    parser.add_argument(
        "--header",
        action="store",
        dest="header",
        help="Request header"
    )
    return parser.parse_args()


def create_ssl_context():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()
    return context


def create_socket(context, host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = context.wrap_socket(sock, server_hostname=host)
    return sock


def connect_socket(sock, host, port=443):
    sock.connect((host, port))


def send_request(sock, request):
    sock.send(request.encode())


def close_socket(sock):
    sock.close()


def get_dict_http_response(sock):
    data = {}
    with sock.makefile("r", encoding="utf-8") as sf:
        line = sf.readline()
        # first is http type, status code, str status
        type, code, status = line.split(" ")
        data["Code"] = code.rstrip()

        while line:
            line = sf.readline()

            header_type, header_value = line.split(": ")
            data[header_type] = header_value.rstrip()

            if header_type == "Transfer-Encoding":
                content = ""

                while True:
                    sf.readline()
                    content_length = sf.readline()

                    if content_length == "0\n":
                        break

                    content_length = content_length.rstrip()
                    content_length = int(content_length, 16)
                    content += sf.read(content_length)

                data["Content"] = content
                break

        sf.close()

    return data


def make_request(args):
    if args.header is None:
        args.header = ""

    return args.method + " / HTTP/1.1\nRequest URL: " + args.host + "\n" + args.header + "\n\n"


def validate_args(args):
    if args.method is None or not "GET":
        return False

    if args.host is None or "":
        return False

    return True


args = parse_args()
is_valid_args = validate_args(args)

if is_valid_args is False:
    print("Argument error")
    exit(0)

ssl_context = create_ssl_context()
sock = create_socket(ssl_context, args.host)
connect_socket(sock, args.host)

request_header = make_request(args)
send_request(sock, request_header)
response_dict = get_dict_http_response(sock)

close_socket(sock)

for key in response_dict:
    print(key + ": " + response_dict[key])
