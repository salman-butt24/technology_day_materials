# User Email DataModel
# Separating User Email information from User information allows for
# support of multiple emails per user.
# can be applied to both the All-in-one User DataModel and the separated User/UserAuth DataModel

# Define User DataModel. Make sure to add flask_user UserMixin !!!
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    ...
    # Relationship
    user_emails = db.relationship('UserEmail')

# Define UserEmail DataModel.
class UserEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())
    is_primary = db.Column(db.Boolean(), nullable=False, default=False)

    # Relationship
    user = db.relationship('User', uselist=False)
