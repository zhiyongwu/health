from flask import Flask
import data_query

app = Flask(__name__)


@app.route("/query/<name>")
def api_query(name):
    data = data_query.query_data(name)
    print(data)
    return {'data': data, 'status': 'success'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
