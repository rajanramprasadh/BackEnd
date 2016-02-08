import time
import datetime
from datetime import date
import pytz
from pytz import country_timezones
from firebase import firebase
firebase=firebase.FirebaseApplication('https://yabrtest.firebaseio.com/')
result=firebase.get('/teams', None)
u=result
u=d['teams']
for key in u:
    print('team name:',key)
    mem=u[key]
    for k in mem:
        if("members" in k):
            team=mem['members']
            for t in team:
                data=team[t]
                bday=data['birthdate']#mon day
                bmon=bday[0:3]#mon
                bdate=int(bday[4:6])#day
                if(bday[0:3]=="Jan"):
                    bmon=1
                elif (bday[0:3]=="Feb"):
                    bmon=2
                elif(bday[0:3]=="Mar"):
                    bmon=3
                elif(bday[0:3]=="Apr"):
                    bmon=4
                elif(bday[0:3]=="May"):
                    bmon=5
                elif(bday[0:3]=="Jun"):
                    bmon=6
                elif(bday[0:3]=="Jul"):
                    bmon=7
                elif(bday[0:3]=="Aug"):
                    bmon=8
                elif(bday[0:3]=="Sep"):
                    bmon=9
                elif(bday[0:3]=="Oct"):
                    bmon=10
                elif(bday[0:3]=="Nov"):
                    bmon=11
                elif(bday[0:3]=="Dec"):
                    bmon=12
                #today = date.today()
                #print(today)
                current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                today=date(2000+int(current_time.strftime('%y')),int(current_time.strftime('%m')),int(current_time.strftime('%d')))
                #today == date.fromtimestamp(time.time())
                adv=datetime.timedelta(days=0)#1 day advance mail
                my_birthday = date(today.year, bmon, bdate)
                today=today+adv;
                if my_birthday < today:
                    my_birthday = my_birthday.replace(year=today.year + 1)
                time_to_birthday = abs(my_birthday - today)
                if(time_to_birthday.days==0):
                    print(adv.days ,"days more for ",data['name'],"birthday ")
                    for whom_to_mail in team:
                        a=team[whom_to_mail]
                        if(a['sendemail']==True):
                            print("Mail has to sent to mailid:", a['email'])
                            client = sendgrid.SendGridClient("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")
                            message=sendgrid.Mail()
                            message.add_to(a['email'])
                            message.set_from("notification@cakebee.com")
                            message.set_subject("Birthday Notification")
                            message.set_html("Your friend", data['name'], " has a birthday on ", data['birthdate'])
                            client.send(message)
