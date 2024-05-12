import { initializeApp } from 'firebase/app'
import {
    getFirestore, collection
    from 'firebase/firestore'
}

const firebaseConfig = {
apiKey: "AIzaSyAJrMkGJjp3nwScsXfzuAGIImtYeltV_08",
authDomain: "fir-9-dojo.firebaseapp.com",
projectId: "fir-9-dojo",
storageBucket: "fir-9-dojo.appspot.com",
messagingSenderId: "631362710531",
appId: "1:631362710531:web:9d0f0a9a051ff1163ab236"
}

// init firebase app
initializeApp (firebaseConfig)

// init services
const db = getFirestore()

const db = firebase.firestor()

db.collection('Web Development')+

// collection ref
const colRef = collection(db, 'Web Development')
// get collection data