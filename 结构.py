from flask import Flask, render_template

app = Flask(__name__)

# 静态资源缓存
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=600'  # 设置静态资源缓存为10分钟
    return response

# 压缩响应数据
from flask_compress import Compress
Compress(app)

# 使用异步加载
from flask_cors import CORS
CORS(app)

# 模板渲染
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
