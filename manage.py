import os
import unittest
from flask_script import Manager
from app import create_app, dbsql as db
from dotenv import load_dotenv, find_dotenv
from flask_migrate import MigrateCommand

# load dotenv in the base root
load_dotenv(find_dotenv())
app = create_app(os.getenv('APP_ENV') or 'dev')
app.app_context().push()
manager = Manager(app)

# A command for migrations
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)

@manager.command
def test():
    """
    Unit Tests
    """
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def create_db():
    """
    Creates a new database with tables
    """
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
