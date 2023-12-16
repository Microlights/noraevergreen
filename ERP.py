from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp_database.db'
db = SQLAlchemy(app)

# 定义模型
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)

# 创建数据库表
db.create_all()

# 路由：显示员工列表
@app.route('/')
def employee_list():
    employees = Employee.query.all()
    return render_template('employee_list.html', employees=employees)

# 路由：添加新员工
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        new_employee = Employee(name=name, position=position)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('employee_list'))
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)
