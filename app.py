from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🚀 My DevOps Pipeline is Working!</h1>
    <p>Deployed automatically via Jenkins + Docker on AWS EC2</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
