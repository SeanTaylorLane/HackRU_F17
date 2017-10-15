from firebase import firebase

testFirebase = firebase.FirebaseApplication('https://hackru-5d3f1.firebaseio.com/')
print(testFirebase.get('/Event/Attendees/Sal/', 'Locations'))
