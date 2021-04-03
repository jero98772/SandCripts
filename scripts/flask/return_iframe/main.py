from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
	strpage = "<iframe src='https://jero98772.pythonanywhere.com/blog/manifest.html#own' scrolling='no' style='position: absolute; height: 100%;width: 100%; border: none'> </iframe>"
	return strpage

if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0",port=9600)
