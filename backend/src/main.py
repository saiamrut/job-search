"""Main application runner"""
import os
from pathlib import Path
from config import app, db
from setupdb import seed_database
import controllers.job_board
import controllers.job_opportunity


def main():
    """Main runner function"""
    sqlite_db = Path(__file__).parent / "site.db"
    if not os.path.isfile(sqlite_db):
        # Seeds datbase if empty
        seed_database()
    # Run Flask app
    app.run(debug=True)


if __name__ == "__main__":
    """Start server app"""
    main()
