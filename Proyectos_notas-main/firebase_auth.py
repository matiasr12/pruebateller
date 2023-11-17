import firebase_admin
from firebase_admin import credentials

# Coloca la ruta al archivo JSON de configuración que descargaste desde Firebase
cred = credentials.Certificate('proyectonotas-41662-firebase-adminsdk-496e1-1732814dcb.json')
firebase_admin.initialize_app(cred)



