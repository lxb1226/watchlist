from flask  import Flask, url_for
app = Flask(__name__)

# 注册视图函数,
# 使用app.route()装饰器来为这个函数绑定对应的URL
# 一个视图函数可以绑定多个URL，这通过附加多个装饰器实现
@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    # return "welcome to My watchlist!"
    # return u'欢迎来到我的WatchList'
    return '<h1>helloTotoro！</h1><img src="http://helloflask.com/totoro.gif">'

# app.route装饰器的参数称为URL规则，
# 可以在URL里定义变量部分
@app.route('/user/<name>')
def user_page(name):
    return "User: %s" % name

# url_for：生成URL，第一个参数是端点值,默认为视图函数的名称
@app.route('/test')
def test_url_for():
    # 下面是一些调用示例
    # 输出/
    print(url_for('hello'))
    # 输出/user_page/heyjude
    print(url_for('user_page', name='heyjude'))
    # 输出/user_page/hello
    print(url_for('user_page', name='hello'))
    # 输出/test
    print(url_for('test_url_for'))
    # 输出/test?num=2
    print(url_for('test_url_for', num = 2))
    return 'Test page'