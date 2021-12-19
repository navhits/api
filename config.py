import os, re

config = {
    "apiKey": os.getenv('FIREBASE_API_KEY'),
    "authDomain": f"{os.getenv('FIREBASE_PROJECT_ID')}.firebaseapp.com",
    "databaseURL": f"https://{os.getenv('FIREBASE_PROJECT_ID')}.firebaseio.com",
    "projectId": os.getenv('FIREBASE_PROJECT_ID'),
    "storageBucket": f"{os.getenv('FIREBASE_PROJECT_ID')}.appspot.com",
    "messagingSenderId": "625751335541",
    "appId": "1:625751335541:web:40cb0d65648b0ac0afce3c",
    "measurementId": "G-66G9G438LF",
    "serviceAccount": {
            "type": "service_account",
            "project_id": os.getenv('FIREBASE_PROJECT_ID'),
            "private_key_id": "2794b23507fc0a762502585ed4c10ecff3b36f5b",
            "private_key": re.sub(r"\\n", "\n", os.getenv('FIREBASE_SERVICE_ACCOUNT_PRIVATE_KEY')),
            "client_email": "firebase-adminsdk-g8lsq@portfolio-nav-fireapp.iam.gserviceaccount.com",
            "client_id": os.getenv("FIREBASE_SERVICE_ACCOUNT_CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-g8lsq%40portfolio-nav-fireapp.iam.gserviceaccount.com"
        }

}