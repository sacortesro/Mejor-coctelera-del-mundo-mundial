from flask import Flask, render_template
app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


# @app.route('/secciones/', methods=['POST', 'GET'])
# def index():
#     return render_template('cocteles.html')

if __name__== '__main__':
    app.run(debug=True)