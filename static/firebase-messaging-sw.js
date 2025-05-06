importScripts("https://www.gstatic.com/firebasejs/10.9.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/10.9.0/firebase-messaging-compat.js");

firebase.initializeApp({
  apiKey: "AIzaSyAv0zcFQaMT_t0hkQfQjL5AMvvuMBPaMRg",
  authDomain: "fcm-core-ef7bd.firebaseapp.com",
  projectId: "fcm-core-ef7bd",
  messagingSenderId: "1003393924896",
  appId: "1:1003393924896:web:abe406fb7da6542c27e145"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
      body: payload.notification.body
    };
  
    self.registration.showNotification(notificationTitle, notificationOptions);
  });