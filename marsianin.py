from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if prof.lower() == 'engineer':
        header = 'Инженерные симуляторы'
        image = '/static/img/eng.png'
    elif prof.lower() == 'scientist':
        header = 'Научные симуляторы'
        image = '/static/img/sci.jpg'
    print(f'''<html>
    <head>
        <title>Симуляторы</title>
    </head>
    <body>
            <h1>{header}</h1>
            <img src="{image}" alt="Схема">
    </body>
</html>''')
    return f'''<html>
    <head>
        <title>Симуляторы</title>
    </head>
    <body>
            <h1>{header}</h1>
            <img src="{image}" alt="Схема">
    </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
