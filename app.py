from flask import Flask, render_template, request,flash
from flask import Response
from matplotlib.figure import Figure
from flask import session
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from DBConfig import DBConnection
import pickle

from BlockChain import load_contract_address, add_data, get_user_data, dataget


app = Flask(__name__)
app.secret_key = "abc"




@app.route('/')
def index():
    load_contract_address()
    return render_template('index.html')

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/adminhome")
def adminhome():
    return render_template("admin_home.html")


@app.route("/userhome")
def userhome():
    return render_template("user_home.html")

@app.route("/newuser")
def newuser():
    return render_template("register.html")


@app.route("/train")
def train():
    return render_template("model.html")

    
    
@app.route("/testing")
def testing():
    return render_template("testing.html")

    
    
@app.route("/adddata")
def adddata():
    return render_template("adddata.html")

    
    

@app.route("/adminlogout")
def adminlogout():
    return render_template("admin.html")


    

@app.route("/userlogout")
def userlogout():
    return render_template("user.html")


    

@app.route("/trainmodel",methods =["GET", "POST"])
def trainmodel():
    try:
        model = request.form.get('model')
        from Training import Training
        Training.main(model)
        return render_template("model.html", msg="Model creation completed !!")


    except Exception as e:
        f=open('log.txt','w')
        f.write(e)

    return ""
   

@app.route("/testingmodels",methods =["GET", "POST"])
def testingmodels():
    try:
        file = request.form.get("file")
        from Testing import Testing
        Testing.main(file)
        return render_template("testing.html", msg="Testing process completed !!")


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))

    return ""



@app.route("/uploadaction",methods =["GET", "POST"])
def uploadaction():
    try:
        file = request.form.get('file')
        file='Uploads/'+file
        f=open(file, 'r')
        data=f.read()
        cont=[]
        for d in data.splitlines():
            if len(d)>3:
                cont.append(d)
        

        protein=[]
        from Prediction import Prediction
        classs=Prediction.main(cont)


        from Freq import CountFrequency
        res=CountFrequency(classs)

        d=[]


        for i in range(len(cont)):
            d.append([cont[i][:50]+'..',classs[i]])



        
        for i in range(len(classs)):
            if classs[i]=='Protein':
                protein.append(cont[i])
        


        session['protein']=protein
        


        return render_template("adddata2.html", data=d, res=res)


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))


@app.route("/uploadaction2",methods =["GET", "POST"])
def uploadaction2():
    try:
        protein=session['protein']
        email=session['uid']
        tot_str=''
        for s1 in protein:
            tot_str=tot_str+s1

        from CreateHash import generateHash
        hash_value=generateHash(tot_str)
        import random as r
        from DateTime import getdate
        ts=getdate()
        tid=r.randint(1000, 100000)
        data=[str(tid), email, hash_value, str(ts)]  
        load_contract_address()
        add_data(email, data)

        database = DBConnection.getConnection()
        cursor = database.cursor()

        for s1 in protein:
            sql = "insert into results values(%s,%s,%s)"
            values = (tid, email,s1)
            cursor.execute(sql, values)
            database.commit()


        
        
        
        return render_template("adddata.html", msg='Data block added successfully!! ')


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))



@app.route("/viewown",methods =["GET", "POST"])
def viewown():
    try:
        email=session['uid']
        
        load_contract_address()
        res = get_user_data(email) #data=[str(tid), email, hash_value, str(ts)]  
        tot_data=[]
        database = DBConnection.getConnection()
        cursor2 = database.cursor()
        
        for r1 in res:
            tid=r1[0]
       
            sql= "select * from results where tid='"+str(tid)+"' "
            cursor2.execute(sql)
            records = cursor2.fetchall()
            for row in records:
                tot_data.append(row[2])


                


        return render_template("viewown.html", data=tot_data)


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))




@app.route("/viewall",methods =["GET", "POST"])
def viewall():
    try:
        

        load_contract_address()
        res=dataget()
        tot_data=[]
        database = DBConnection.getConnection()
        cursor2 = database.cursor()
        
        for r1 in res:
            tid=r1[0]
       
            sql= "select * from results where tid='"+str(tid)+"' "
            cursor2.execute(sql)
            records = cursor2.fetchall()
            for row in records:
                tot_data.append(row[2])


                


 
        
        return render_template("viewall.html", data=tot_data)


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))



@app.route("/viewbc",methods =["GET", "POST"])
def viewbc():
    try:
        

        load_contract_address()
        seqs=dataget()
        
        return render_template("viewbc.html", data=seqs)


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))

@app.route("/getseqdata",methods =["GET", "POST"])
def getseqdata():
    
    database = DBConnection.getConnection()
    cursor2 = database.cursor()
    
    tid = request.form.get('tid')
    
    sql= "select * from results where tid='"+str(tid)+"' "

    cursor2.execute(sql)
    records = cursor2.fetchall()
    return render_template("viewresults.html", data=records)




@app.route("/results")
def results():
    from bargraph import bargraph
    try:
        bargraph.view()
    except:
        pass
    from bargraph2 import bargraph2
    try:
        bargraph2.view()
    except:
        pass
    from bargraph3 import bargraph3
    try:
    
        bargraph3.view()
    except:
        pass

    database = DBConnection.getConnection()
    cursor2 = database.cursor()
    
    sql= "select * from evaluations "
    cursor2.execute(sql)
    records = cursor2.fetchall()
    return render_template("results.html", data=records)




@app.route("/results2")
def results2():
    
    database = DBConnection.getConnection()
    cursor2 = database.cursor()
    
    sql= "select * from evaluations2 "
    cursor2.execute(sql)
    records = cursor2.fetchall()
    return render_template("results2.html", data=records)



@app.route("/adminlogin",methods =["GET", "POST"])
def adminlogin():

        uid = request.form.get("uid")
        pwd = request.form.get("pwd")
        if uid=="admin" and pwd=="admin":

            return render_template("admin_home.html")
        else:
            return render_template("admin.html",msg="Invalid Credentials")







@app.route("/user_register",methods =["GET", "POST"])
def user_register():
    try:
        sts=""
        name = request.form.get('name')
        
        pwd = request.form.get('pwd')
        mno = request.form.get('mno')
        email = request.form.get('email')
        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql = "select count(*) from register where email='" + email + "'"
        cursor.execute(sql)
        res = cursor.fetchone()[0]
        if res > 0:
            sts = 0
        else:
            sql = "insert into register values(%s,%s,%s,%s)"
            values = (name, pwd,email,mno)
            cursor.execute(sql, values)
            database.commit()
            sts = 1
        print(sts,'*************')

        return render_template("register.html", msg="Registered Successfully..! Login Here.")



    except Exception as e:
        f=open('log.txt','w')
        f.write(e)

    return ""


@app.route("/userlogin_check",methods =["GET", "POST"])
def userlogin_check():

        uid = request.form.get("uid")
        pwd = request.form.get("pwd")

        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql = "select count(*) from register where email='" + uid + "' and passwrd='" + pwd + "'"
        cursor.execute(sql)
        res = cursor.fetchone()[0]
        if res > 0:
            session['uid'] = uid

            return render_template("user_home.html")
        else:

            return render_template("user.html", msg2="Invalid Credentials")

        return ""


@app.route("/verify",methods =["GET", "POST"])
def verify():
    
    database = DBConnection.getConnection()
    cursor2 = database.cursor()
    
    tid = request.form.get('tid')
    hash_val = request.form.get('hash')
    
    sql= "select * from results where tid='"+str(tid)+"' "


    cursor2.execute(sql)
    records = cursor2.fetchall()

    tot_str=''
    
    for row in records:
        tot_str=tot_str+row[2]

    from CreateHash import generateHash
    hash_value=generateHash(tot_str)
    msg=''
    if hash_value==hash_val:
        msg='The Data is verified successfully, the Hash is matched !!'
    else:
        msg='The Data is not verified, the Hash is mismatched !!'


    try:
        

        load_contract_address()
        seqs=dataget()
        
        return render_template("viewbc.html", data=seqs, msg=msg)


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))



    

@app.route("/testingmodels2",methods =["GET", "POST"])
def testingmodels2():
    try:
        file = request.form.get("file")
        from Testing2 import Testing2
        Testing2.main(file)
        return render_template("testing.html", msg="Testing process completed !!")


    except Exception as e:
        f=open('log.txt','w')
        f.write(str(e))

    return ""




if __name__ == '__main__':
    app.run(host="localhost", port=1234, debug=True)
