from flask import Flask #导入flask
app = Flask(__name__) #初始化app

@app.route('/') #设置网站根目录下返回内容
def index():
    return '<html><h1>Hello World</h1></html>'  #这个就是Hello World啦

if __name__ == '__main__':
    app.run('0.0.0.0',15000) #0.0.0.0 设置本地目录，并且端口号为5000

