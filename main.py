from flask import Flask, request, redirect
import os
app = Flask(__name__)

# データの保存先 --- (*1)
DATAFILE = './board-data.txt'

# ルートにアクセスしたとき --- (*2)
@app.route('/')
def index():
    msg = 'まだ書込はありません。'
    # 保存データを読む --- (*3)
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:
            msg = f.read()
    # メッセージボードと投稿フォーム --- (*4)
    return """
    <html><body>
    <h1>メッセージボード</h1>
    <div style="background-color:yellow;padding:3em;">
    {0}</div>
    <h3>ボードの内容を更新:</h3>
    <form action="/write" method="POST">
        <textarea name="msg"
         rows="6" cols="60"></textarea><br/>
        <input type="submit" value="書込">
    </form>
    </body></html>
    """.format(msg)

# POSTメソッドで/writeにアクセスしたとき --- (*5)
@app.route('/write', methods=['POST'])
def write():
    # データファイルにメッセージを保存 --- (*6)
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:
            f.write(msg)
    # ルートページにリダイレクト --- (*7)
    return redirect('/')

with open("a.txt", 'rt') as f:
    a = f.read()
print(a)

a = 100
with open("a.txt", 'wt') as f:
    f.write(str(a))

# 変数を残すテスト(setting.py)
# 読み込み
import setting
print(setting.b + 10)

# かきこ
b = 100
with open("setting.py", 'wt') as f:
    f.write(f"b = {b}")

if __name__ == '__main__':
    app.run(host='0.0.0.0')