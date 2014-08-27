import os

from flask import Flask, render_template, request, jsonify

from must import query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/')
def api():
    work_title = request.args.get('name', '')
    work_ip = request.args.get('ip', '')

    data = query(work_title, work_ip)

    return jsonify(**data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
