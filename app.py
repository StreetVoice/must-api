import os

from flask import Flask, render_template, request, json

from must import query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/')
def api():
    work_title = request.args.get('work_title', '')
    work_ip = request.args.get('work_ip', '')
    work_title_exact = request.args.get('work_title_exact', 'N')
    work_ip_exact = request.args.get('work_ip_exact', 'N')

    data = query(work_title, work_ip, work_title_exact, work_ip_exact)

    return json.dumps(data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
