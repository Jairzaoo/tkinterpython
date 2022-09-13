#import firebase_admin
#pip install pyrebase4
import pyrebase
from firebase_admin import credentials, firestore
#from firebase_admin import credentials, firestore
#cred = credentials.Certificate(r"C:\Users\PICHAU\Desktop\pysimplegui\Nova pasta\spiritual-vent-199906-firebase-adminsdk-stzqd-8764b436f6.json")
#firebase_admin.initialize_app(cred)
#db = firestore.client()  # this connects to our Firestore database
#collection = db.collection('programa')  # opens 'programa' collection
#doc = collection.document('rome')  # specifies the 'rome' document
#deletear collection.document('rome').delete()
#collection.document('barcelona').update({ 'weather': firestore.DELETE_FIELD})
firebaseConfig = {
  "apiKey": "AIzaSyD-m4XCrn-csSJaxJF-c7neJXpVwtjzQGs",

  "authDomain": "spiritual-vent-199906.firebaseapp.com",

  "databaseURL": "https://spiritual-vent-199906-default-rtdb.firebaseio.com",

  "projectId": "spiritual-vent-199906",

  "storageBucket": "spiritual-vent-199906.appspot.com",

  "messagingSenderId": "661585358491",

  "appId": "1:661585358491:web:9f38ebc1228c76bd1f203e",

  "measurementId": "G-9NMV3DB5VL"
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
#firestore_db = firestore.client()
loginsucesso = False
#dbproduto = result = db.child("Produto").get()
#auth = firebase.auth()
#storage = firebase.storage()

#push data
#data={"name":"John", "age":20, "adress":["new york", "los angeels"]}
#db.child("Branch").child("Employee").child("male employes").push(data)
#db.push(data)
#data={"usuario":"12345","senha":"54321"} <<<<<<<
#db.child("Logins").push(data)<<<<<<<<<<<<<
#own key
#data={"age":20, "adress":["new york", "los angeels"]}
#db.child("John").set(data)
#data={"senha":"54321"}
#db.child("Logins").child("12345").set(data)

#retrieve
#users=db.child("Logins").get()
#result = db.child("Logins").order_by_child("usuario").equal_to("12345").get()
#if result is not None:
#    print(result.val())
#    pasword = db.child("Logins").order_by_child("senha").equal_to("54321").get()
#    if pasword is not None:
#        print("senha e pass correto")

#for user in users.each():
#    if users.val() == "12345":
#        print('found')
