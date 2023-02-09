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
            if(acc[3] == 1):
                return redirect('/getName')
            elif(acc[3] == 2):
                return redirect('/getprofileteacher')    
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
                try:
                    if(details['formCheck-1']):
                        cursor.execute("UPDATE account SET account.rememberlogin = 1 WHERE account.userId = %s",(_userId,))
                        mysql.connection.commit()
                        cursor.close()
                except:
                    print(1)
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
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
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
    cursor.execute("SELECT * FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,tution.HPLop,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaHV = %s",(_userId,))
    data = cursor.fetchall()
    cursor.execute("SELECT SUM(tution) FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaHV = %s",(_userId,))
    sumpay = cursor.fetchone()
    cursor.execute("SELECT SUM(tution) FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaHV  = %s AND p.paid = 0",(_userId,))
    lefttution = cursor.fetchone()
    cursor.execute("SELECT SUM(tution) FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaHV =  %s AND p.paid = 1",(_userId,))
    paidtution = cursor.fetchone()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
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
    cursor.execute("SELECT * FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaHV = %s",(_userId,))
    data_class = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    return render_template('student_classlist.html',data_class = data_class,URL_Img = url,data = data)

@app.route('/getdataclass')
def getdataclass():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p JOIN (SELECT teacher.HoTen,teacher.MaGV FROM teacher) t ON t.MaGV = p.MaGV WHERE p.MaHV = %s",(_userId,))
    data_class = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    cursor.close()
    return render_template('student_classlist.html',data_class = data_class,URL_Img = url,data = data)

@app.route('/getdetailclass/<string:id_class>')
def getindetailclass(id_class):
    cursor = mysql.connection.cursor()
    print(id_class)
    cursor.execute("SELECT count(*) userId FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaLop = %s", (id_class,))
    count_member = cursor.fetchone()
    cursor.execute("SELECT * FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p JOIN teacher ON p.MaGV = teacher.MaGV WHERE p.MaHV = %s AND p.MaLop = %s",(_userId, id_class,))
    infor_class = cursor.fetchall()
    cursor.execute("SELECT user.HoTen,user.MaHV FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p JOIN user ON p.MaHV = user.MaHV WHERE p.MaLop = %s",(id_class,))
    detail_student = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    cursor.close()
    return render_template('student_classinfor.html',count_member = count_member, infor_class = infor_class, detail_student=detail_student,id =id_class,URL_Img = url,data=data)

@app.route('/getdetailstudent/<string:id_student>,<string:id_class>')
def getdetailstudent(id_student,id_class):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(id_student,))
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
    cursor.execute("SELECT * FROM (SELECT grade.MaHV,classes.TenLop,classes.MaLop,grade.DiemGK,grade.DiemCK,grade.NhanXet,grade.DiemTK FROM classes,grade WHERE grade.MaLop = classes.MaLop) p WHERE p.MaHV = %s",(_userId,))
    data_grade = cursor.fetchall()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    return render_template('student_grade.html',data_grade = data_grade,URL_Img = url,data=data)

@app.route("/getdetailgrade/<string:id_class>")
def getdetailgrade(id_class):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT grade.MaHV,classes.TenLop,classes.MaLop,grade.DiemGK,grade.DiemCK,grade.NhanXet,grade.DiemTK FROM classes,grade WHERE grade.MaLop = classes.MaLop) p WHERE p.MaHV = %s AND p.MaLop = %s ",(_userId,id_class,))
    datadetail_grade = cursor.fetchone()
    cursor.execute("SELECT * FROM user WHERE user.MaHV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[6]).get_url(user['idToken'])
    return render_template('student_commentbyteacher.html',datadetail_grade = datadetail_grade,URL_Img = url,data=data)

@app.route("/getprofileteacher")
def getprofileteacher():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV = %s",(_userId,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[5]).get_url(user['idToken'])
    date = str(data[1])
    x = date.split("-")
    date = x[2]+'-'+x[1]+'-'+x[0]
    return render_template("teacher_accountprofile.html",data=data,URL_Img =url,date=date)
@app.route("/editprofileteacher")
def editprofileteacher():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV = %s",(_userId,))
    data = cursor.fetchone()
    cursor.close()
    url = storage.child(data[5]).get_url(user['idToken'])
    date = str(data[1])
    x = date.split("-")
    date = x[2]+'-'+x[1]+'-'+x[0]
    return render_template("teacher_editprofile.html",data=data,URL_Img =url,date=date)

@app.route('/getdataclass_teacher')
def getdataclass_teacher():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM `classes` JOIN teacher ON classes.MaGV = teacher.MaGV WHERE classes.MaGV = %s",(_userId,))
    data_class = cursor.fetchall()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV  = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    cursor.close()
    return render_template('teacher_classlist.html',data_class = data_class,URL_Img = url,data = data)
@app.route('/getdetailclass_teacher/<string:id_class>')
def getindetailclass_teacher(id_class):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT count(*) MaHV FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p WHERE p.MaLop = %s", (id_class,))
    count_member = cursor.fetchone()
    cursor.execute("SELECT * FROM `classes` JOIN teacher ON classes.MaGV = teacher.MaGV WHERE classes.MaLop = %s",(id_class,))
    infor_class = cursor.fetchall()
    cursor.execute("SELECT user.HoTen,user.MaHV FROM (SELECT classes.MaLop,classes.MaGV,classes.TenLop,classes.tution,classes.ThoiGian,classes.DiaDiem,tution.MaHV,tution.paid FROM classes JOIN tution ON classes.MaLop = tution.MaLop) p JOIN user ON p.MaHV = user.MaHV WHERE p.MaLop = %s",(id_class,))
    detail_student = cursor.fetchall()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV  = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    cursor.close()
    return render_template('teacher_classinfor.html',count_member = count_member, infor_class = infor_class, detail_student=detail_student,id =id_class,URL_Img = url,data=data)
@app.route('/getdetailstudent_teacher/<string:id_user>,<string:id_class>')
def getdetailstudent_teacher(id_user,id_class):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM (SELECT grade.MaHV,classes.TenLop,classes.MaLop,grade.DiemGK,grade.DiemCK,grade.NhanXet,grade.DiemTK,classes.MaGV FROM classes,grade WHERE grade.MaLop = classes.MaLop) p WHERE p.MaHV = %s AND p.MaLop = %s ",(id_user,id_class,))
    datadetail_grade = cursor.fetchone()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    cursor.execute("SELECT * FROM (SELECT user.MaHV,user.HoTen,grade.MaLop,user.fileImg FROM grade,user WHERE grade.MaHV =user.MaHV) p WHERE p.MaHV = %s AND p.MaLop = %s",(id_user,id_class,))
    data_student = cursor.fetchone()
    url_student = storage.child(data_student[3]).get_url(user['idToken'])
    global id_c
    global id_u
    id_c = id_class
    id_u = id_user
    
    return render_template('teacher_commentstudent.html',datadetail_grade = datadetail_grade,URL_Img = url,data=data,data_student=data_student,url_student=url_student)

@app.route('/getsalary')
def getsalary():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM `salary` WHERE salary.MaGV = %s",(_userId,))
    list_salary = cursor.fetchall()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    return render_template("teacher_listsalary.html",list_salary=list_salary,data=data,URL_Img = url)
@app.route('/getdetailsalary/<string:codesalary>')
def getdetailsalary(codesalary):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM `salary` WHERE salary.MaLuong = %s",(codesalary,))
    detailsalary = cursor.fetchone()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    basic_salary = detailsalary[1]*detailsalary[2]
    fsalary = basic_salary + detailsalary[5]
    return render_template("teacher_salary.html",detailsalary=detailsalary,data=data,URL_Img = url,basic_salary=basic_salary,fsalary=fsalary)

@app.route('/getnumberofteach')
def getnumberofteach():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM salary WHERE salary.MaGV = %s",(_userId,))
    numberteach = cursor.fetchall()
    cursor.execute("SELECT * FROM teacher WHERE teacher.MaGV = %s",(_userId,))
    data = cursor.fetchone()
    url = storage.child(data[5]).get_url(user['idToken'])
    return render_template("teacher_numberteach.html",numberteach=numberteach,data=data,URL_Img = url)

@app.route('/updateprofileteacher',methods=['GET', 'POST'])
def updateprofileteacher():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        details = request.form
        try:
            phonenumber = details['number-phone']
        except:
            phonenumber = None
        try:
            address = details['_address']
        except:
            address = None
        if(phonenumber != None):
            cursor.execute("UPDATE teacher SET teacher.DiaChi = %s WHERE teacher.MaGV = %s",(address,_userId,))
            mysql.connection.commit()
       
        if(address != None):
            cursor.execute("UPDATE teacher SET teacher.SDT = %s WHERE teacher.MaGV = %s",(phonenumber,_userId,))
            mysql.connection.commit()
        try:
            des = details['descrip']
        except:
            des=None
        if(des != None):
            cursor.execute("UPDATE teacher SET teacher.TrinhDo = %s WHERE teacher.MaGV = %s",(des,_userId,))
            mysql.connection.commit()
    return redirect('/getprofileteacher')

@app.route('/updateprofiledescription')
def updateprofiledescription():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        details = request.form
        des = details['descrip']
        cursor.execute("UPDATE teacher SET teacher.TrinhDo = %s WHERE teacher.MaGV = %s",(des,_userId,))
        mysql.connection.commit()
    return redirect('/editprofileteacher')

@app.route('/updategrade',methods=['GET', 'POST'])
def updategrade():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        details = request.form
        print(id_u)
        try:
            midterm = details['midterm']
        except:
            midterm = -1.0
        try:
            finalterm = details['finalterm']
        except:
            finalterm = -1.0
        if(midterm != -1.0):
            cursor.execute("UPDATE grade SET grade.DiemGK = %s WHERE grade.MaHV = %s AND grade.MaLop = %s",(midterm,id_u,id_c,))
            mysql.connection.commit()
        if(finalterm != -1.0):
            cursor.execute("UPDATE grade SET grade.DiemCK = %s WHERE grade.MaHV = %s AND grade.MaLop = %s",(finalterm,id_u,id_c))
            mysql.connection.commit()
        cursor.execute("SELECT grade.DiemGK,grade.DiemCK FROM grade WHERE grade.MaHV = %s AND grade.MaLop = %s",(id_u,id_c,))
        grade = cursor.fetchone()
        cursor.execute("UPDATE grade SET grade.DiemTK = %s WHERE grade.MaHV = %s AND grade.MaLop = %s",(grade[0]*0.3+ grade[1]*0.7,id_u,id_c,))
        mysql.connection.commit()
    return redirect('/getdataclass_teacher')

@app.route('/checkin')
def checkin():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT salary.SoBuoi FROM salary WHERE salary.MaGV = %s ",(_userId,))
        numberTeach = cursor.fetchone()
        nTeach = numberTeach[0]+1
        cursor.execute("UPDATE salary SET salary.SoBuoi = %s WHERE salary.MaGV =%s",(nTeach,_userId))
        mysql.connection.commit()
        return redirect('/getnumberofteach')


if __name__ == '__main__':
    app.run(debug=True)
