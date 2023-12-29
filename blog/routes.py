from blog.__init__ import app
from flask import render_template
from blog.models import Post


@app.route("/")
@app.route("/home")
def home_page():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_page(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template("post.html", post=post)
