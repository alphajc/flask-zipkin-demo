from flask import Flask, json, jsonify, request
from flask_zipkin import Zipkin
import logging
import requests


app = Flask('backend')
app.config['ZIPKIN_DSN'] = 'http://zipkin:9411/api/v1/spans'
zipkin = Zipkin()
zipkin.init_app(app)


@app.route('/orders', methods=['GET'])
def orders():
    count = request.args.get('count')
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    data = requests.get('http://demo_orders:5000/allOrders', headers=headers).json()
    if count:
        return jsonify(data[:int(count)]), 200
    else:
        return jsonify(data), 200


@app.route('/detail/<int:order_id>', methods=['GET'])
def detail(order_id):
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    data = requests.get('http://demo_aggregate:5000/detail/{}'.format(order_id), headers=headers).json()
    return jsonify(data), 200


@app.route('/custSearch/<string:name>', methods=['GET'])
def cust_search(name):
    payload = {'name': name}
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    data = requests.post('http://demo_orders:5000/custSearch', json=payload, headers=headers).json()
    return jsonify(data), 200


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(debug=True, host='0.0.0.0')
