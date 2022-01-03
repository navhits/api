# Naveen's API

You can now view my profile with an API call.

View the docs at [https://api.navs.page/docs](https://api.navs.page/docs)

## Underlying Technology

### Platform

1. [Firebase](https://firebase.google.com/)
    * Realtime Database - Allows me to instantly update my profile with ease.
    * Firebase Storage - To store and access static files.
2. [Deta.sh](https://deta.sh/)
    * Deta Micros - The place where the API is deployed.
    * Deta Base - An object based DB that I use as an Intermediate Key Value store to cache data from Firebase.

### Language and Frameworks

1. Python 3.9
2. [FastAPI](https://fastapi.tiangolo.com/) - Beautiful to use Python web framework.
