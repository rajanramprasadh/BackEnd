import json
import time
import datetime
from datetime import date
import pytz
from pytz import country_timezones
from firebase import firebase
from Flag import Flag
firebase=firebase.FirebaseApplication('https://yabrtest.firebaseio.com/')
result=firebase.get('/teams', None)
#u=result
d={
  "teams" : {
    "00518935-E465-4F05-81DA-F24CB0194143" : {
      "country" : "India",
      "email" : "mapancha@cisco.com",
      "members" : {
        "C6E25A1D-6EBD-42EB-88D0-385A988ADA99" : {
          "birthdate" : "Jan 17",
          "email" : "mapancha@cisco.com",
          "name" : "Manikandan P",
          "sendemail" : True
        }
      },
      "organization" : "Cisco Systems",
      "team" : "INSBU Cisco Bangalore",
      "zipcode" : 560103
    },
    "1AAD4A09-43E1-4486-9EB6-CF52FFD04385" : {
      "country" : "India",
      "email" : "msasikumar.in@gmail.com",
      "organization" : "Sample",
      "team" : "Sample",
      "zipcode" : 560076
    },
    "1FD3A21C-B224-4A77-B586-55539A1E3D3A" : {
      "country" : "India",
      "email" : "sgusidi@cisco.com",
      "members" : {
        "ADBA90AB-13CA-46A6-9913-F4F4C33910FB" : {
          "birthdate" : "Apr 6",
          "email" : "",
          "name" : "Vandana",
          "sendemail" : False
        }
      },
      "organization" : "Cisco",
      "team" : "OCC",
      "zipcode" : 560087
    },
    "2435EC11-CB38-4CC6-B8DE-2D2E95D676CD" : {
      "country" : "India",
      "email" : "nitdugga@cisco.com",
      "members" : {
        "705CC361-7C7F-42E7-953D-C91DBE9587B8" : {
          "birthdate" : "Feb 6",
          "email" : "ashriram@cisco.com",
          "name" : "Aditya Shriram",
          "sendemail" : True
        },
        "E2B33BF8-2B57-49BC-B265-3070E44CA3EC" : {
          "birthdate" : "Jan 20",
          "email" : "nitdugga@cisco.com",
          "name" : "Nitish Duggal",
          "sendemail" : True
        }
      },
      "organization" : "CISCO",
      "team" : "ISE",
      "zipcode" : 560103
    },
    "25D9419F-9CF6-4120-92BB-30FEF396110A" : {
      "country" : "India",
      "email" : "mapancha@cisco.com",
      "organization" : "Cisco Systems",
      "team" : "INS-BU Cisco Bangalore",
      "zipcode" : 560103
    },
    "3BEB709D-8EE6-46BA-99D6-BB59958BED1D" : {
      "country" : "India",
      "email" : "abishek@logbase.io",
      "members" : {
        "1DA22979-F757-4A2D-A929-4340355738BF" : {
          "birthdate" : "Nov 20",
          "email" : "rajanramprasadh@gmail.com",
          "name" : "Ramprasadh",
          "sendemail" : True
        },
        "8B505386-A1DA-4078-8375-5CB5D7D2D585" : {
          "birthdate" : "Jan 26",
          "email" : "",
          "name" : "Saravanakumar",
          "sendemail" : False
        },
        "FF2E453B-DC5E-4D6F-819A-1A702769FE1D" : {
          "birthdate" : "Dec 9",
          "email" : "abishek@logbase.io",
          "name" : "Abishek",
          "sendemail" : True
        }
      },
      "organization" : "LogBase",
      "team" : "LogBase Interns",
      "zipcode" : 641004
    },
    "44DD5E32-0574-48F5-8638-365A3A621180" : {
      "country" : "India",
      "email" : "abcd@saggezza.com",
      "organization" : "Saggezza",
      "team" : "SaggezzaAtCisco",
      "zipcode" : 560093
    },
    "4BCFF027-B30B-44FE-AC35-9CB57A183F19" : {
      "country" : "India",
      "email" : "sateeshkumar.529@gmail.com",
      "members" : {
        "659AE5BF-BFA1-4362-B7C0-E1BC8D14983B" : {
          "birthdate" : "Jul 10",
          "email" : "",
          "name" : "Ramu",
          "sendemail" : False
        },
        "6EBB6CEC-DD4C-4651-B2BC-3D706A061569" : {
          "birthdate" : "Feb 5",
          "email" : "sateeshkumar.529@gmail.com",
          "name" : "Sateesh",
          "sendemail" : True
        },
        "9A8F7C96-5514-43B6-B571-DDE1C60317DA" : {
          "birthdate" : "Mar 19",
          "email" : "",
          "name" : "Srinu",
          "sendemail" : False
        },
        "A5C99D87-6BC6-492E-9824-3F7F97899639" : {
          "birthdate" : "Apr 23",
          "email" : "",
          "name" : "Sravan",
          "sendemail" : False
        },
        "BB6FB2EA-D751-41BF-8B47-AFF62CCE621B" : {
          "birthdate" : "Apr 4",
          "email" : "",
          "name" : "Alekhya",
          "sendemail" : False
        },
        "CD24696D-0361-4898-914A-D48CDF80D90E" : {
          "birthdate" : "Jun 23",
          "email" : "",
          "name" : "Jyothi",
          "sendemail" : False
        },
        "FFF0932C-7125-410F-A010-7250353C100A" : {
          "birthdate" : "Aug 3",
          "email" : "",
          "name" : "Sai",
          "sendemail" : False
        }
      },
      "organization" : "Vsspl",
      "team" : "Team7",
      "zipcode" : 500081
    },
    "6C4F0A00-D6C6-4E88-B905-66A561DBEE36" : {
      "country" : "India",
      "email" : "kbarve@cisco.com",
      "members" : {
        "37ACB079-E11A-43AD-A8D7-A8BB1B695BC0" : {
          "birthdate" : "Oct 24",
          "email" : "kbarve@cisco.com",
          "name" : "Sanjiv",
          "sendemail" : True
        },
        "761AB08E-DDD4-405C-8C68-DBB3033B2330" : {
          "birthdate" : "Dec 16",
          "email" : "kbarve@cisco.com",
          "name" : "Kirti Barve",
          "sendemail" : True
        },
        "9964F5F9-09BF-40FE-B1EB-D24A620122B7" : {
          "birthdate" : "Nov 2",
          "email" : "kbarve@cisco.com",
          "name" : "Sasikala",
          "sendemail" : True
        },
        "F7EF3D06-8D44-4057-A330-2154613C3D5B" : {
          "birthdate" : "Jan 7",
          "email" : "kbarve@cisco.com",
          "name" : "Alok",
          "sendemail" : True
        }
      },
      "organization" : "cisco",
      "team" : "MobiltySolution",
      "zipcode" : 560103
    },
    "82C4D6CF-3107-4EA7-8CCD-B221734F451D" : {
      "country" : "India",
      "email" : "rosunil@cisco.com",
      "organization" : "Cisco",
      "team" : "Nexus Doc Team",
      "zipcode" : 560103
    },
    "A55D80C6-07E3-4361-8CD3-C921FBDFF7AE" : {
      "country" : "India",
      "email" : "pundir.himanshi7@gmail.com",
      "organization" : "Cisco",
      "team" : "Prithvi",
      "zipcode" : 560103
    },
    "AEA132DE-8F7F-4CDB-8C27-BA5763EF5EE5" : {
      "country" : "India",
      "email" : "shrjha@cisco.com",
      "members" : {
        "3BF69D4B-1055-49C9-8117-96D032E96DD8" : {
          "birthdate" : "Oct 22",
          "email" : "",
          "name" : "Shraddha",
          "sendemail" : False
        }
      },
      "organization" : "CISCO",
      "team" : "Seesctrl/ICSR",
      "zipcode" : 560103
    },
    "BBE4D13A-B05E-4884-B66E-010293D5BB83" : {
      "country" : "India",
      "email" : "santoshprathod07@gmail.com",
      "members" : {
        "8C8EB16C-12C2-4E00-9FC3-5CC2FA85A2C4" : {
          "birthdate" : "Nov 24",
          "email" : "",
          "name" : "Santosh",
          "sendemail" : False
        }
      },
      "organization" : "Sanp",
      "team" : "Santosh",
      "zipcode" : 560085
    },
    "D4A7BB4B-8D5D-420D-A5CD-7C3DF70F7B9A" : {
      "config" : {
        "notifybefore" : 2
      },
      "country" : "India",
      "email" : "abishek@logbase.io",
      "members" : {
        "042A4EE5-6E7F-4931-8A0F-87495D8F7254" : {
          "birthdate" : "Oct 31",
          "email" : "",
          "name" : "Shridevi",
          "sendemail" : False
        },
        "2E195B01-B94B-4B43-A418-AD50DA7B2541" : {
          "birthdate" : "Dec 9",
          "email" : "abishek@logbase.io",
          "name" : "Abishek",
          "sendemail" : True
        },
        "AE6EAF76-E208-4CCE-8AB3-9D70353BEDE8" : {
          "birthdate" : "Nov 14",
          "email" : "",
          "name" : "Karthik",
          "sendemail" : False
        },
        "C6A3C1B1-0B5E-44BB-A854-C19810344E2A" : {
          "birthdate" : "Mar 4",
          "email" : "",
          "name" : "Kousik",
          "sendemail" : False
        },
        "D6344F22-DE5B-46A7-A7F0-94B6B90DD38B" : {
          "birthdate" : "May 5",
          "email" : "",
          "name" : "Kalai",
          "sendemail" : False
        }
      },
      "organization" : "LogBase",
      "team" : "LogBase",
      "zipcode" : 641045
    },
    "D6817D73-3CC2-4BFA-8A1C-9C83C3D9E637" : {
      "country" : "India",
      "email" : "zahoor1235@gmail.com",
      "members" : {
        "468B2EB4-535B-4C0B-87DC-EEA354B6B07F" : {
          "birthdate" : "May 2",
          "email" : "",
          "name" : "Zahoor Ahmed",
          "sendemail" : False
        },
        "72128D8F-5DB3-4E27-847E-DE6DEE88A727" : {
          "birthdate" : "Feb 14",
          "email" : "zahoor1235@gmail.com",
          "name" : "xyz",
          "sendemail" : True
        }
      },
      "organization" : "xyz",
      "team" : "Zahoor's Team",
      "zipcode" : 560034
    },
    "D7161E30-1422-4943-996E-188B5FCFCF18" : {
      "country" : "India",
      "email" : "denemade@cisco.com",
      "members" : {
        "906C9C5E-A499-49F9-9FB2-31F9FB4ABBAF" : {
          "birthdate" : "Oct 14",
          "email" : "denemade@cisco.com",
          "name" : "DEEPALI NEMADE",
          "sendemail" : True
        }
      },
      "organization" : "Cisco Systems",
      "team" : "MITG ICSR",
      "zipcode" : 560103
    },
    "E08CB114-EDF0-4EB5-BF0B-8952CDCE7BBC" : {
      "country" : "India",
      "email" : "yvishnu81@gmail.com",
      "organization" : "vodafone",
      "team" : "FUNCART",
      "zipcode" : 560103
    },
    "F3DA153F-4608-442C-904E-FE2601B367B3" : {
      "country" : "India",
      "email" : "risagarw@cisco.com",
      "organization" : "Cisco",
      "team" : "Pavan Team",
      "zipcode" : 560103
    }
  }
}
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
                if(time_to_birthday.days==1):
                    print(adv.days ,"days more for ",data['name'],"birthday ")
                    for whom_to_mail in team:
                        a=team[whom_to_mail]
                        if(a['sendemail']==True):
                            print("Mail has to sent to mailid:", a['email'])
			   # client = sendgrid.SendGridClient("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")
                           # message=sendgrid.Mail()
                           # message.add_to(a['email'])
                           # message.set_from("notification@cakebee.com")
                           # message.set_subject("Hi")
                           # message.set_html("")
                           # client.send(message)
			    flag(*data, *a)
