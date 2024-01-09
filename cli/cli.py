from database.models import db, User

## This function will add custom CLI commands to our Flask App
def custom_cli(app):
    @app.cli.command("seed")
    def seed():
        test_email = 'test@test.com'
        existing_user = User.query.filter(User.email == test_email).first()
        if existing_user != None:
            print("You have already use the seed command on your database. Command aborted...")
            return -1
        """Seed the database."""
        user = User(full_name='Test User',
                    email=test_email,
                    password_hash=User.hash_password('password'))
        db.session.add(user)
        print('Creating user test user...', user)
        db.session.commit()
