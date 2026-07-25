import os
import psycopg2
from dotenv import load_dotenv

# Charge les variables du .env
load_dotenv()

database_url = os.getenv("DATABASE_URL")

try:
    # Connexion à Neon
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    
    # Exécute une requête simple
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(" Connexion réussie à Neon !")
    print("Version de PostgreSQL :", db_version[0])

    cursor.close()
    connection.close()

except Exception as error:
    print("❌ Erreur de connexion :", error)

DATABASE_URL=postgresql://neondb_owner:npg_UYR2Vl1mDAra@ep-sparkling-sky-asw4m230-pooler.c-4.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
