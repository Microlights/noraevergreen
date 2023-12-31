from flask import Flask, render_template, request  
  
app = Flask(__name__)  
  
@app.route('/')  
def home():  
    return render_template('home.html')  
  
@app.route('/about')  
def about():  
    return render_template('about.html')  
  
@app.route('/contact')  
def contact():  
    return render_template('contact.html')  
  
@app.route('/users', methods=['POST'])  
def create_user():  
    user = request.form['user']  
    return f"Created user {user}"  
  
if __name__ == '__main__':  
    app.run(debug=True)
