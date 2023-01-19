from flask import Flask,session,render_template,url_for, redirect, jsonify, request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tlc_web'
app.secret_key='web'
mysql = MySQL(app)

import firebase_admin
# from firebase_admin import credentials,storage
import pyrebase

config ={
    "apiKey": "AIzaSyBLKJzZT-it5evKo7Gt2R_v4mK9-5337xo",
    "authDomain": "web-thi-online-92393.firebaseapp.com",
    "databaseURL": "https://web-thi-online-92393-default-rtdb.firebaseio.com",
    "projectId": "web-thi-online-92393",
    "storageBucket": "web-thi-online-92393.appspot.com",
    "messagingSenderId": "139904512267",
    "appId": "1:139904512267:web:240c23d5376ab18eb8720e",
    "measurementId": "G-J5GC4G5YKL"
}
# config={
#     "type": "service_account",
#     "project_id": "web-thi-online-92393",
#     "private_key_id": "aa35f6a40b1d32a63670f6e571dd2ea23d22a2f3",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCRxekrvRqdYiJ5\ngcfXir0DlB8vJ9fpHLf1DdzaNJrx9xojI4Rn8IDgK6Bc/ZIDCXhuymZINxKq48ZZ\n34cJvmoPDpYkX76Fc100roezJCLPvLgW0+sZS6ayk0IA9OowR1yL0nh/DAHSAlhx\nAP3BpFFKyP5Tv7+wHeUOa5OeW5NewxGa0Wa19RM0+lLDdP2TEOE3InUBTlyPVtlF\nzd3iH5GMIm6IJgT10w0PpziKrYq/dsgRrUigm4BtXwmxP6ffLzhwX9etSk2h18w7\nSJq2s8GXE0aBJy9/GEtjB5io/LYeM/bQlB4OxD/axKOA/nGb/pYFqsYPB14WHAqY\nYDdehv7xAgMBAAECggEABbWGFC/z5sqmn5kGtIYOMNTJ9qtTtSE3G5JY6w5ykqjP\n7b6UDqWoYav9VYo0Zm9zBFSWwxvhD8johksou0F2K7PLC1tyl0BogjBjR4+4cbSQ\nhlhZyOPus4GGU4pEBIyiIiaMKis6t2v4scHm4YDn31fWDUqhUJD2XRiEFgiJHrkF\nU3JHvsiHsLlVGZv4ukw/eeI/g8bMT7+TDPGpG/2plgfixOEv7kBXYBFwvXNTIf+X\n4xhykj2eQUgtxYn+GMBwkXKB3FZ+x9+oHfEo3VSDt6t0SCrNoUBytWsnCmFKQe4v\nMOnCldjE+oPVk1p5yctS7Xu3zNdPQkyycFC3odpt1wKBgQDJRM/e2Ku2u1MQgEbJ\n8TKpSnGOGoNzLXnnYxwUCY0FO5NMJkVlZhLRTXMnTu59VHaIBIn4FE4PtKS+Rd80\ndrwLyxISxTlS1DvEChrDs7W4eLL9hQO9gh3TLi09deZN/L1BZw9ZMJafEkF98gJN\nGff/1ZDzOqWH/XadvzsPAP/fiwKBgQC5ac21CjEHDano1RJNDw4BiKP0u51FtLzR\nrY/7SptY7gouqeSxDUkAuOBQ0WDSGdSvh9py3APSy37GZ+EmgT3KyHvykABPu+bv\n2JA2NqtOsCrZi2AEXA/Ow2TO1/kR3UxEf3neIY5xMHqZmyXhE9Ad9jpPaF0oluZw\n8j5tQgsq8wKBgE08yQDd6Vegn4nPkFri4uwwk09TQWqr4wI2+Il/+MwvRqGMdkkp\nWMNVk4FcOw2BolMkWsYHFMXWLvqN2dBKWHO2JGNrqEnvBFiBADBmALCgMSA1MXBC\nRKvMJrRVUGJRQVed8zfo+4Rj/xoUC2oHMzLMhGmy8d80F5cF0eY6HfdtAoGBALJn\nFpKS6tfBkvJASmqxCKX7Jt8twsc2f9Q072w4vj8UU+HQgQbHJK44NUYuIL4oMphu\n3IdWIaurOCGKBH77Lky3GWQsoNAXmb7AHwq7EZwWMDTAQbQQLPmi0pWgA7zntSHX\nkphkq11H6z9vpEPsv3yE1lhfr/uFLtgQjnasbHh3AoGACU0oaHQH90zAU4p6L7JZ\nt5KzsME0JLD0fOy0nJPhm4U2KVgEvO7V73f03FQzQloktIB+GNignda2Rs+/1MJ9\ngxDvHyti+MCupvYi6FNnYA5TSeVsUO3mA3Ef2NbHDW/paH6nFwst3GLnScMKLXn0\nM+2kQNZWty9tDKPXlxmURr0=\n-----END PRIVATE KEY-----\n",
#     "client_email": "firebase-adminsdk-ang5t@web-thi-online-92393.iam.gserviceaccount.com",
#     "client_id": "118414752321987878111",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ang5t%40web-thi-online-92393.iam.gserviceaccount.com"
#   }
  
# cred = credentials.Certificate(config)
# firebase_admin.initialize_app(cred,{"storageBucket": "web-thi-online-92393.appspot.com"})
# bucket = storage.bucket()
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
auth = firebase.auth()
_email = "1@gmail.com"
_password = "123456"
user = auth.sign_in_with_email_and_password(_email, _password)



@app.route('/', methods=['GET', 'POST'])
def login():
    global _userId
    msg = ''
    if request.method == "POST":
        details = request.form
        email = details['Email']
        password = details['Pass']
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM account WHERE Email = %s AND Password = %s"
        val = (email, password,)
        cursor.execute(sql, val)
        account = cursor.fetchone()
        cursor.close()
        if account:
            _userId = account[0]
            return redirect('/getName')
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)
@app.route('/getName')
def getName():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[6]).get_url(user['idToken'])
    # blob = bucket.blob(_userId)
    # print(blob.public_url)
    return render_template("studentProfile.html",data = data,URL_Img = url)
# Thong tin hoc phi

@app.route('/navTution')
def navTution():
    return redirect(url_for('getPayperstu'))

@app.route('/getPayment')
def getPayperstu():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM classes WHERE classes.member = %s",(_userId,))
    data = cursor.fetchall()
    cursor.execute("SELECT sum(tution) FROM classes WHERE classes.member = %s",(_userId,))
    sumpay = cursor.fetchone()
    cursor.execute("SELECT sum(tution) FROM classes WHERE classes.member = %s AND classes.paid = 0",(_userId,))
    lefttution = cursor.fetchone()
    cursor.execute("SELECT sum(tution) FROM classes WHERE classes.member = %s AND classes.paid = 1",(_userId,))
    paidtution = cursor.fetchone()
    cursor.close()
    return render_template('payment.html',tutions = data,sumtution = sumpay, lefttution = lefttution, paidtution = paidtution )
    

if __name__ == '__main__':
    app.run(debug=True)
