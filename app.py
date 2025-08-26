from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_code():
    return render_template('code.html')



@app.route('/index')
def serve_index():
    return render_template('index.html')


@app.route('/chemistry')
def serve_chemistry():
    return render_template('chemistry.html')

@app.route('/graphics')
def serve_graphics():
    return render_template('graphics.html')

# Serve files from labs folder
@app.route('/labs/<path:filename>')
def serve_labs(filename):
    return send_from_directory("labs", filename)

# Serve static files (CSS, JS, images) automatically
# Flask already serves from /static/ by default








if __name__ == '__main__':
    app.run(debug=True,port=8000)