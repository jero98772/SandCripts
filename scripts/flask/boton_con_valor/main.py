from flask import Flask , render_template,request,flash
app = Flask(__name__)
def readtxt(name):
	content = []
	with open(name+".txt", 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content
@app.route("/",methods = ["POST","GET"])
def index():
    msg="test"
    namesblogs = readtxt("data")
    print(namesblogs)
    if request.method == "POST":
        print("post true")
        #delte2 =
        #edit2 = 
        deletechecks = request.form.getlist("delete")
        editchecks = request.form.getlist("edit")
        print("reuest in list")
        answer = "edit"+str(editchecks)+"\ndelete"+str(deletechecks)
        print(answer)
        #flash(answer)
        msg=answer
    return render_template("index.html",blogs = namesblogs,msg = msg)
if __name__ == "__main__":
    	app.run(debug=True,host="0.0.0.0",port=9600)
