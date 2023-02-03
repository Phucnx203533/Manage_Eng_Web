from flask import Flask,session,render_template,url_for, redirect, jsonify, request
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os   
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

# app.config['SECRET_KEY'] = 'abc'
# app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

# photos = UploadSet('photos',IMAGES)
# configure_uploads(app,photos)
# UPLOAD_FOLDER = os.path.join('static', 'img')
# ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = 'You can write anything, is just a test'
# UPLOAD_FOLDER = 'static/img'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])



@app.route('/', methods=['GET', 'POST'])
def login():
    global _userId
    msg = ''
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM account")
    accs = cursor.fetchall()
    for acc in accs:
        if(acc[4] == 1):
            _userId = acc[0]
            return redirect('/getName')
    if request.method == "POST":
        details = request.form
        email = details['Email']
        password = details['Pass']
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM account WHERE Email = %s AND Password = %s"
        val = (email, password,)
        cursor.execute(sql, val)
        account = cursor.fetchone()
        if account:
            _userId = account[0]
            if(account[3] == 1):
                try:
                    if(details['formCheck-1']):
                        cursor.execute("UPDATE account SET account.rememberlogin = 1 WHERE account.userId = %s",(_userId,))
                        mysql.connection.commit()
                        cursor.close()
                except:
                    print(1)
                return redirect('/getName')
            elif(account[3] == 2):
                return redirect('/getprofileteacher')
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE account SET account.rememberlogin = 0 WHERE account.userId = %s",(_userId,))
    mysql.connection.commit()
    return render_template('login.html')


@app.route('/getName')
def getName():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[6]).get_url(user['idToken'])
    # blob = bucket.blob(_userId)
    # print(blob.public_url
    date = str(data[2])
    x = date.split("-")
    date = x[2]+'-'+x[1]+'-'+x[0]        
    return render_template("student_accountprofile.html",data = data,URL_Img = url,date = date)
# Thong tin hoc phi

@app.route('/navTution')
def navTution():
    return redirect(url_for('getPayperstu'))

@app.route('/getPayment')
def getPayperstu():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p WHERE p.userId = %s",(_userId,))
    data = cursor.fetchall()
    cursor.execute("SELECT SUM(tution) FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p WHERE p.userId = %s",(_userId,))
    sumpay = cursor.fetchone()
    cursor.execute("SELECT SUM(tution) FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p WHERE p.userId  = %s AND p.paid = 0",(_userId,))
    lefttution = cursor.fetchone()
    cursor.execute("SELECT SUM(tution) FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p WHERE p.userId =  %s AND p.paid = 1",(_userId,))
    paidtution = cursor.fetchone()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    _data = cursor.fetchone()
    url = storage.child(_data[6]).get_url(user['idToken'])
    cursor.close()
    paidtution = str(paidtution[0])
    print(paidtution)
    if(paidtution == "None"):
        paidtution ="0"
    return render_template('student_payment.html',tutions = data,sumtution = sumpay, lefttution = lefttution, paidtution = paidtution,URL_Img = url,_data = _data)

@app.route('/getnowclass')
def getinforclass():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,classes.timedate,classes.location,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p WHERE p.userId = %s",(_userId,))
    data_class = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    return render_template('student_classlist.html',data_class = data_class,URL_Img = url,data = data)

@app.route('/getdataclass')
def getdataclass():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,classes.timedate,classes.location,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p JOIN (SELECT teacher.name,teacher.mTeacher FROM teacher) t ON t.mTeacher = p.mTechacer WHERE p.userId = %s",(_userId,))
    data_class = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    cursor.close()
    return render_template('student_classlist.html',data_class = data_class,URL_Img = url,data = data)

@app.route('/getdetailclass/<string:id_class>')
def getindetailclass(id_class):
    cursor = mysql.connection.cursor()
    print(id_class)
    cursor.execute("SELECT count(*) userId FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,classes.timedate,classes.location,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p WHERE p.mClass = %s", (id_class,))
    count_member = cursor.fetchone()
    cursor.execute("SELECT * FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,classes.timedate,classes.location,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p JOIN teacher ON p.mTechacer = teacher.mTeacher WHERE p.userId = %s AND p.mClass = %s",(_userId, id_class,))
    infor_class = cursor.fetchall()
    cursor.execute("SELECT user.name,user.userId FROM (SELECT classes.mClass,classes.mTechacer,classes.name,classes.tution,classes.timedate,classes.location,tution.userId,tution.paid FROM classes JOIN tution ON classes.mClass = tution.mClass) p JOIN user ON p.userId = user.userId WHERE p.mClass = %s",(id_class,))
    detail_student = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    cursor.close()
    return render_template('student_classinfor.html',count_member = count_member, infor_class = infor_class, detail_student=detail_student,id =id_class,URL_Img = url,data=data)

@app.route('/getdetailstudent/<string:id_student>,<string:id_class>')
def getdetailstudent(id_student,id_class):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(id_student,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[6]).get_url(user['idToken'])
    if(id_student == _userId):
        return redirect(url_for('getName'))
    else:
        return render_template('student_profile.html',data=data,URL_img = url,id = id_class)

@app.route('/getgrade')
def getgrade():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT grade.userId,classes.name,classes.mClass,grade.midterm,grade.finalterm,grade.commnet,grade.fgrade FROM classes,grade WHERE grade.mClass = classes.mClass) p WHERE p.userId = %s",(_userId,))
    data_grade = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    return render_template('student_grade.html',data_grade = data_grade,URL_Img = url,data=data)

@app.route("/getdetailgrade/<string:id_class>")
def getdetailgrade(id_class):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT grade.userId,classes.name,classes.mClass,grade.midterm,grade.finalterm,grade.commnet,grade.fgrade FROM classes,grade WHERE grade.mClass = classes.mClass) p WHERE p.userId = %s AND p.mClass = %s ",(_userId,id_class,))
    datadetail_grade = cursor.fetchone()
    cursor.execute("SELECT * FROM user WHERE user.userId = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    return render_template('student_commentbyteacher.html',datadetail_grade = datadetail_grade,URL_Img = url,data=data)

@app.route("/getprofileteacher")
def getprofileteacher():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM teacher WHERE teacher.mTeacher = %s",(_userId,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[5]).get_url(user['idToken'])
    date = str(data[1])
    x = date.split("-")
    date = x[2]+'-'+x[1]+'-'+x[0]
    return render_template("teacher_accountprofile.html",data = data,URL_Img = url,date = date)
@app.route("/editprofileteacher")
def editprofileteacher():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM teacher WHERE teacher.mTeacher = %s",(_userId,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[5]).get_url(user['idToken'])
    date = str(data[1])
    x = date.split("-")
    date = x[2]+'-'+x[1]+'-'+x[0]
    return render_template("teacher_editprofile.html",data = data,URL_Img = url,date = date)
@app.route("/editavatar",methods=("POST", "GET"))
def editavatar():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        files = request.files.getlist('uploaded-file')
        for file in files:
            f = str(file)
            f=f.split("'")
            print(f[1])
        return redirect("/editprofileteacher")

@app.route('/getdataclass_teacher')
def getdataclass_teacher():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM `classes` JOIN teacher ON classes.mTechacer = teacher.mTeacher WHERE classes.mTechacer = %s",(_userId,))
    data_class = cursor.fetchall()
    cursor.execute("SELECT * FROM teacher WHERE teacher.mTeacher  = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    cursor.close()
    return render_template('teacher_classlist.html',data_class = data_class,URL_Img = url,data = data)




if __name__ == '__main__':
    app.run(debug=True)
