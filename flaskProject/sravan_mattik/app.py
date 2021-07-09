from flask import Flask, render_template, request

app = Flask(__name__,template_folder='templates')


@app.route('/form')
def form():
    return render_template('hello.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    print ("--------- Reaching here----------")
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print ("Form data is : {0}".format(form_data))
        return render_template("data.html", form_data=form_data)


app.run(host='localhost', port=5000)