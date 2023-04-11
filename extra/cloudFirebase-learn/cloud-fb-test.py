from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('CSS').document('saltpepper')

doc_ref.set({
    'username':'Atharva',
    'hash':'yuwebc38324tv8gyu3he',
    'salt':'qb97et93r8y39c287y',
    'pepper':'3b0r8ybw973r9w738w3tbr7c3t'
})









