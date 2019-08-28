from faker import Faker
from flask import Flask, jsonify
from flask_zipkin import Zipkin
import logging


app = Flask('items')
app.config['ZIPKIN_DSN'] = 'http://zipkin:9411/api/v1/spans'
data = []
fake = Faker()
zipkin = Zipkin()
zipkin.init_app(app)


@app.route('/allItems', methods=['GET'])
def all_orders():
    return jsonify(data), 200


@app.route('/item/<int:num>', methods=['GET'])
def get_order(num):
    return jsonify(data[num]), 200


def create_items(num):
    return {
        'id': num,
        'desc': fake.bs()
    }


def create_data():
    return [create_items(num) for num in range(1, 100)]


if __name__ == '__main__':
    data = create_data()
    app.logger.setLevel(logging.INFO)
    app.run(debug=True, host='0.0.0.0')
