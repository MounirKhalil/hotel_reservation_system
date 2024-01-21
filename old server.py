from flask import Flask, redirect, url_for, render_template, request, render_template
from flask_mysqldb import MySQL
from waitress import serve
import json
from tkinter import messagebox

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PASSWORD'] = '351Hotel@'
app.config['MYSQL_DB'] = 'exchange'
 
mysql = MySQL(app)


@app.route("/new_registration", methods = ['POST', 'GET'])
def new_registration():

    if request.method=='POST':
        
        data = request.get_json()
        email =data['email']
        fname = data['fname']
        lname = data['lname']
        contact = data['contact']
        email = data['email']
        security_q = data['security_q']
        security_a = data['security_a']
        passw = data['passw']
        cursor = mysql.connection.cursor()
        query=("select * from register where email=%s")
        value=(email,)
        cursor.execute(query,value)
        row=cursor.fetchone()
        if row!=None:
            return '<h1>USER ALREADY EXISTS</h1>'
        else:
            cursor.execute(''' INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)''',(fname,lname,contact,email,security_q,security_a,passw))
            mysql.connection.commit()
            cursor.close()
        return '<h1>Successfully Registered!</h1>'
        
    else:
        return '<h1>Hi</h1>'

@app.route("/get_registration", methods = ['POST', 'GET'])
def getRegistration():

    if request.method=='POST':
        data = request.get_json()
        email = data['email']
        cursor = mysql.connection.cursor()
        query=("select * from register where email=%s")
        value=(email,)
        cursor.execute(query,value)
        row=cursor.fetchone()
        #print(row)
        #jsondata=json.dumps(row, indent=2, sort_keys=True)
        #print(jsondata)
        if row!=None:
            field1=row[0]
            field2=row[1]
            cursor.close()
            content='<h1>Found one user with following data: ' + field1 + ", " + field2 + '</h1>'
            return content
        else:
            cursor.close()
        return '<h1>Record Not Found!</h1>'

    else:
        return '<h1>Hi</h1>'


@app.route("/login_attempt", methods = ['POST', 'GET'])
def login_attempt():
    if request.method=='POST':
        data = request.get_json()
        email = data['email']
        password = data['password']
        cursor = mysql.connection.cursor()
        cursor.execute("select * from register where email=%s and passw=%s",(email,password))
        row=cursor.fetchone()
        if row==None:
            mysql.connection.commit()
            cursor.close()
            return '<h1>Invalid username or password</h1>'
        else:
            mysql.connection.commit()
            cursor.close()
            return '<h1>Login successfull, start?</h1>'
            
@app.route("/passw_reset", methods = ['POST', 'GET'])
def passw_reset():
    if request.method=='POST':
        data = request.get_json()
        email = data['email']
        security_q = data['security_q']
        security_a = data['security_a']
        password = data['password']
        cursor = mysql.connection.cursor()
        query=("select * from register where email=%s and security_q=%s and security_a=%s")
        value=(email,security_q,security_a)
        cursor.execute(query,value)
        row=cursor.fetchone()
        if row==None:
            return '<h1>Please enter the correct answer</h1>'
        else:
            query=("update register set passw=%s where email=%s")
            value=(password,email)
            cursor.execute(query,value)

            mysql.connection.commit()
            cursor.close()
            return '<h1>Your password was reset, please login using new password</h1>'
            
@app.route("/forget_passw", methods = ['POST', 'GET'])
def forget_passw():
    if request.method=='POST':
        data = request.get_json()
        email = data['email']
        cursor = mysql.connection.cursor()
        query=("select * from register where email=%s")
        value=(email,)
        cursor.execute(query,value)
        row=cursor.fetchone()
        if row==None:
            return '<h1>invalid username</h1>'
        else:
            cursor.close()
            return '<h1>else_case</h1>'

@app.route("/add_data", methods = ['POST', 'GET'])
def add_data():
    if request.method=='POST':
        data = request.get_json()
        Ref = data['Ref']
        Name = data['Name']
        Middle = data['Middle']
        Gender = data['Gender']
        PostCode = data['PostCode']
        Mobile = data['Mobile']
        Email = data['Email']
        Nationality = data['Nationality']
        Idproof = data['Idproof']
        Idnumber = data['Idnumber']
        Address = data['Address']
        cursor = mysql.connection.cursor()
        cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Ref,Name,Middle,Gender,PostCode,Mobile,Email,Nationality,Idproof,Idnumber,Address))
        mysql.connection.commit()
        cursor.execute("Select * from customer")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)


@app.route("/update", methods = ['POST', 'GET'])
def update():
    if request.method=='POST':
        data = request.get_json()
        Ref = data['Ref']
        Name = data['Name']
        Middle = data['Middle']
        Gender = data['Gender']
        PostCode = data['PostCode']
        Mobile = data['Mobile']
        Email = data['Email']
        Nationality = data['Nationality']
        Idproof = data['Idproof']
        Idnumber = data['Idnumber']
        Address = data['Address']
        cursor = mysql.connection.cursor()
        cursor.execute("update customer set NAME=%s,MIDDLE=%s,GENDER=%s,POSTcode=%s,MOBILE=%s,EMAIL=%s,NATIONALITY=%s,IDPROoF=%s,IDnumber=%s,ADDRESS=%s where REF=%s",(Name,Middle,Gender,PostCode,Mobile,Email,Nationality,Idproof,Idnumber,Address,Ref))
        mysql.connection.commit()
        cursor.execute("Select * from customer")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)


@app.route("/dat_delete", methods = ['POST', 'GET'])
def dat_delete():
    if request.method=='POST':
        data = request.get_json()
        Ref = data['Ref']
        cursor = mysql.connection.cursor()
        query = "delete from customer where REF=%s"
        value = (Ref,)
        cursor.execute(query,value)
        mysql.connection.commit()
        cursor.execute("Select * from customer")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)

@app.route("/search_data", methods = ['POST', 'GET'])
def search_data():
    if request.method=='POST':
        data = request.get_json()
        search_var = data['search_var']
        txt_search = data['txt_search']
        cursor = mysql.connection.cursor()
        cursor.execute("select * from customer where "+str(search_var)+" LIKE '%"+str(txt_search)+"%'")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)

@app.route("/fetch_data", methods = ['POST', 'GET'])
def fetch_data():
    if request.method=='POST':
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from customer")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)

@app.route("/fetch_data_det", methods = ['POST', 'GET'])
def fetch_data_det():
    if request.method=='POST':
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from details")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)

@app.route("/add_data_det", methods = ['POST', 'GET'])
def add_data_det():
    if request.method=='POST':
        data = request.get_json()
        Floor = data['Floor']
        RoomNo = data['RoomNo']
        RoomType = data['RoomType']
        avFrom = data['avFrom']
        avTo = data['avTo']
        cursor = mysql.connection.cursor()
        query=("select * from details where RoomNo=%s")
        value=(RoomNo,)
        cursor.execute(query,value)

        row=cursor.fetchone()
        if row!=None:
            return '<h1>Room already exists</h1>'
        else:
            cursor.execute(''' insert into details VALUES(%s,%s,%s,%s,%s) ''',(Floor, RoomNo, RoomType, avFrom, avTo))
            mysql.connection.commit()
            cursor.close()
        return '<h1>Room successfully added!</h1>'

    else:
        return '<h1>Hi</h1>'

        row=cursor.fetchone()
        if row==None:
            return '<h1>invalid username</h1>'
        else:
            cursor.close()
            return '<h1>else_case</h1>'

app.route("/update_det", methods = ['POST', 'GET'])
def update_dat():
    if request.method=='POST':
        data = request.get_json()
        Floor = data['Floor']
        RoomType = data['RoomType']
        RoomNo = data['RoomNo']
        cursor = mysql.connection.cursor()
        cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(Floor,RoomType,RoomNo))
        mysql.connection.commit()
        cursor.close()
        return '<h1>Hi</h1>'

@app.route("/dat_delete_det", methods = ['POST', 'GET'])
def dat_delete_det():
    if request.method=='POST':
        data = request.get_json()
        RoomNo = data['RoomNo']
        cursor = mysql.connection.cursor()
        query = "delete from details where ROOM_NO=%s"
        value = (RoomNo,)
        cursor.execute(query,value)
        mysql.connection.commit()
        cursor.close()
        return '<h1>Hi</h1>'

@app.route("/add_data_room", methods = ['POST', 'GET'])
def add_data_room():
    if request.method=='POST':
        data = request.get_json()
        Contact = data['Contact']
        check_in = data['check_in']
        check_out = data['check_out']
        room_type = data['room_type']
        Room = data['Room']
        meal = data['meal']
        noOfdays = data['noOfdays']
        cursor = mysql.connection.cursor()
        cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(Contact,check_in,check_out,room_type,Room,meal,noOfdays))
        mysql.connection.commit()
        cursor.close()
        return '<h1>Hi</h1>'

@app.route("/fetch_data_room", methods = ['POST', 'GET'])
def fetch_data_room():
    if request.method=='POST':
        cursor = mysql.connection.cursor()
        cursor.execute("Select * from room")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)


@app.route("/update_room", methods = ['POST', 'GET'])
def update_room():
    if request.method=='POST':
        data = request.get_json()
        Contact = data['Contact']
        check_in = data['check_in']
        check_out = data['check_out']
        room_type = data['room_type']
        Room = data['Room']
        meal = data['meal']
        noOfdays = data['noOfdays']
        cursor = mysql.connection.cursor()
        cursor.execute("update room set check_in=%s,check_out=%s,room_type=%s,Room=%s,meal=%s,noOfdays=%s where Contact=%s",(check_in,check_out,room_type,Room,meal,noOfdays,Contact))
        mysql.connection.commit()
        cursor.close()
        return '<h1>Hi</h1>'


@app.route("/dat_delete_room", methods = ['POST', 'GET'])
def dat_delete_room():
    if request.method=='POST':
        data = request.get_json()
        Contact = data['Contact']
        cursor = mysql.connection.cursor()
        query = "delete from room where CONTACT=%s"
        value = (Contact,)
        cursor.execute(query,value)
        mysql.connection.commit()
        cursor.close()
        return '<h1>Hi</h1>'

@app.route("/fetch_contact", methods = ['POST', 'GET'])
def fetch_contact():
    if request.method=='POST':
        data = request.get_json()
        Contact = data['Contact']
        cursor = mysql.connection.cursor()

        query=("select NAME from customer where MOBILE=%s")
        value = (Contact,)
        cursor.execute(query,value)
        row = cursor.fetchone()
        if row==None:
            return '<h1>Number not found</h1>'
        else:
            mysql.connection.commit()
            cursor.close()
        return '<h1>Hi</h1>'


@app.route("/fetch_contact_gender", methods = ['POST', 'GET'])
def fetch_contact_gender():
    if request.method=='POST':
        data = request.get_json()
        Mobile = data['Mobile']
        cursor = mysql.connection.cursor()
        query=("select Gender from customer where Mobile=%s")
        value = (Mobile,)
        cursor.execute(query,value)
        row = cursor.fetchone()
        cursor.close()
        return str(row)

@app.route("/fetch_contact_email", methods = ['POST', 'GET'])
def fetch_contact_email():
    if request.method=='POST':
        data = request.get_json()
        Mobile = data['Mobile']
        cursor = mysql.connection.cursor()
        query=("select Email from customer where Mobile=%s")
        value = (Mobile,)
        cursor.execute(query,value)
        row = cursor.fetchone()
        cursor.close()
        return str(row)

@app.route("/fetch_contact_nation", methods = ['POST', 'GET'])
def fetch_contact_nation():
    if request.method=='POST':
        data = request.get_json()
        Mobile = data['Mobile']
        cursor = mysql.connection.cursor()
        query=("select Nationality from customer where Mobile=%s")
        value = (Mobile,)
        cursor.execute(query,value)
        row = cursor.fetchone()
        cursor.close()
        return str(row)


@app.route("/fetch_contact_address", methods = ['POST', 'GET'])
def fetch_contact_address():
    if request.method=='POST':
        data = request.get_json()
        Mobile = data['Mobile']
        cursor = mysql.connection.cursor()
        query=("select Address from customer where Mobile=%s")
        value = (Mobile,)
        cursor.execute(query,value)
        row = cursor.fetchone()
        cursor.close()
        return str(row)


@app.route("/search_data_room", methods = ['POST', 'GET'])
def search_data_room():
    if request.method=='POST':
        data = request.get_json()
        search_var = data['search_var']
        txt_search = data['txt_search']
        cursor = mysql.connection.cursor()
        cursor.execute("select * from room where "+str(search_var)+" LIKE '%"+str(txt_search)+"%'")
        rows = cursor.fetchall()
        if len(rows)!=0:
            mysql.connection.commit()
        cursor.close()
        return str(rows)


@app.route("/refresh_btnn", methods = ['POST', 'GET'])
def refresh_btnn():
    if request.method=='POST':
        #using details mysql table
        data = request.get_json()
        check_in = data['check_in']
        check_out = data['check_out']
        cursor = mysql.connection.cursor()
        cursor.execute("select * from details where ((DATE(avFrom) <= "+str(check_in)+") AND (DATE(avTo) >= "+str(check_out)+")) ORDER BY RoomType ASC")
        rows = cursor.fetchall()
        if len(rows)!=0:
            display=[]
            for i in range(len(rows)):
                comb=''
                for j in range(3):
                    comb = comb + rows[i][j] + ' '
                display.append(comb)
            display=tuple(display)        
            mysql.connection.commit()
        cursor.close()
        return str(display)



if __name__ == "__main__":
#    app.run(port=8081)
#	app.run(host='0.0.0.0', port=8081)
       serve(app, host='0.0.0.0', port=8081, url_scheme='https')
