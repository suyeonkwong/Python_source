from flask import Flask,render_template,request,jsonify
from day10.mydao_emp import DaoEmp

app = Flask(__name__,static_url_path='', static_folder='static')

@app.route('/')
def emp():
    de = DaoEmp()
    list = de.selectlist()
    return render_template('crud.html',list=list)

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)


if __name__ == '__main__':
    app.run(debug=True)
  
   















