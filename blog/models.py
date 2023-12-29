from blog.__init__ import db


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=20), nullable=False)
    description = db.Column(db.String(length=60), nullable=False)
    content = db.Column(db.Text(), nullable=False, unique=True)
    blog_image = db.Column(db.LargeBinary(), nullable=False)

    def __repr__(self):
        return self.title
