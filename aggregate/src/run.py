from flask import Flask, jsonify, request
from flask_zipkin import Zipkin
import logging
import requests


app = Flask('aggregate')
app.config['ZIPKIN_DSN'] = 'http://zipkin:9411/api/v1/spans'
zipkin = Zipkin()
zipkin.init_app(app)


@app.route('/detail/<int:order_id>', methods=['GET'])
def detail(order_id):
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    order = requests.get('http://demo_orders:5000/order/{}'.format(order_id), headers=headers).json()
    items = [_fetch_item(item_id) for item_id in order.get('items', [])]
    del order['items']
    order['items'] = items
    return jsonify(order), 200


def _fetch_item(item_id):
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    return requests.get('http://demo_items:5000/item/{}'.format(item_id), headers=headers).json()


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(debug=True, host='0.0.0.0')
