from pprint import pprint
import socket

from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_ip_info():
    # ref: https://www.codegrepper.com/code-examples/python/python+get+private+ip
    
    host_public_ip = requests.get('https://api.ipify.org').text
    hostname = socket.gethostname()
    host_private_ip = socket.gethostbyname(hostname)

    payload = {
        'client-ip': request.remote_addr,
        'host-public-ip': host_public_ip,
        'host-private-ip': host_private_ip,
        'host-name': hostname,
        'host-request-url': request.host_url
    }
    pprint(payload)
    return payload, 200


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)