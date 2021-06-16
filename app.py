from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return '''
    <html>
        <head>
            <title>FCA</title>
        </head>
        <body>
            <h1>Faculdade de Ciências Agrárias</h1>
            <p>Página em manutenção. Voltaremos em breve.</p>
            <br><br><br><br><br>
            <marquee>UNILÚRIO - CIÊNCIA- DESENVOLVIMENTO - COMPROMISSO</marquee>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')