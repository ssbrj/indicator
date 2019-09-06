import os

from flask import Flask, render_template, send_from_directory


app = Flask(
    __name__,
    static_folder='../frontend/build/static',
    template_folder='../frontend/build'
)
# app.config.from_object('config')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, '../frontend/build/static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='indicator.test', port=port, debug=True)
