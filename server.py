from flask import Flask, render_template,redirect,session
app=Flask(__name__)
app.secret_key="guarda el secreto"


@app.route('/')
def index():
    if 'contador' in session:
        session['contador']=session['contador'] +1
    else:
        session['contador']=1
    return render_template( 'index.html')

@app.route('/destroy',methods=['Get'])
def resetear():
    session.clear()
    return redirect ('/')

@app.route('/contar2',methods=['Get'])
def contar2():
    session['contador']+=2
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)