from flask import Flask, request, render_template, redirect, url_for
import json


app = Flask(__name__)

# ---------------------------
# JSON Utility Functions
# ---------------------------


def load_json():
    """Load blog posts from JSON file and return them as a Python list."""
    with open("blog_postes.json", 'r') as file:
        return json.load(file)


def save_json(posts):
    """Save the current list of blog posts back to the JSON file."""
    with open("blog_postes.json", 'w') as file:
        json.dump(posts, file, indent=4)


# ---------------------------
# ROUTES
# ---------------------------


@app.route('/')
def index():
    """Display all blog posts."""
    blog_posts = load_json()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add a new blog post (form + processing)."""
    if request.method == 'POST':
        blog_posts = load_json()

        # Read form fields
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Generate new unique ID
        id_post = blog_posts[-1]["id"] + 1 if blog_posts else 1

        # Create new post object
        neu_poste = {
            "id": id_post,
            "author": author,
            "title": title,
            "content": content
        }

        # Save new post
        blog_posts.append(neu_poste)
        save_json(blog_posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """Delete a blog post by its ID."""
    blog_posts = load_json()

    # Find and remove the matching post
    for post in blog_posts:
        if post["id"] == post_id:
            blog_posts.remove(post)
            break

    save_json(blog_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Update an existing blog post."""
    blog_posts = load_json()

    # Locate the post by ID
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')
        save_json(blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>')
def like(post_id):
    """Increment the like counter of a blog post."""
    blog_posts = load_json()

    for post in blog_posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break

    save_json(blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

