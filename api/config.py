import os, re


config = {
    "apiKey": os.getenv('FIREBASE_API_KEY'),
    "authDomain": f"{os.getenv('FIREBASE_PROJECT_ID')}.firebaseapp.com",
    "options": {
        "databaseURL": f"https://{os.getenv('FIREBASE_PROJECT_ID')}.firebaseio.com",
        "projectId": os.getenv('FIREBASE_PROJECT_ID'),
        "storageBucket": f"{os.getenv('FIREBASE_PROJECT_ID')}.appspot.com",
    },
    "serviceAccount": {
        "type": "service_account",
        "project_id": os.getenv('FIREBASE_PROJECT_ID'),
        "private_key_id": "60ccce3f28d794976e671eb9ceb03a4b06226066",
        "private_key": re.sub(r"\\n", "\n", os.getenv('FIREBASE_SERVICE_ACCOUNT_PRIVATE_KEY')),
        "client_email": "firebase-adminsdk-g8lsq@portfolio-nav-fireapp.iam.gserviceaccount.com",
        "client_id": os.getenv("FIREBASE_SERVICE_ACCOUNT_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-g8lsq%40portfolio-nav-fireapp.iam.gserviceaccount.com"
    }
}