from app import app, db
from models import Credential

with app.app_context():
    try:
        db.create_all()
        print("All tables created (if they didn't exist).")
    except Exception as e:
        print(f"Error creating tables: {e}")
