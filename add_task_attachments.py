#!/usr/bin/env python3
"""
Migration script to add TaskAttachment table
"""
from app import app, db
from models import TaskAttachment

def migrate():
    with app.app_context():
        print("Creating TaskAttachment table...")
        db.create_all()
        print("✅ Migration completed successfully!")

if __name__ == '__main__':
    migrate()
