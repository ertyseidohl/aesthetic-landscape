import base64

from flask import Flask, request

from motif import motif

app = Flask(__name__)

@app.route('/')
def homepage():
    seed = request.args.get('seed')
    seed, image = motif(seed=seed, is_webapp=True)

    return """
        <html>
        <head>
            <title>a e s t h e t i c</title>
            <meta charset="utf-8">
        </head>
        <body>
            <p><img src="data:image/png;base64,{image}"></p>
            <p>Seed: <a href='./?seed={seed}'>{seed}</p>
            <p><a href="./">New Image</a></p>
        </body>
        </html>
    """.format(image=image.decode("utf-8"), seed=seed)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
