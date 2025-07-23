from flask import Flask, render_template, url_for, abort, request
import os
import markdown
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Load repository owner and name from environment variables
GITHUB_REPO_OWNER = os.getenv('GITHUB_REPO_OWNER', 'inakimaldive')
GITHUB_REPO_NAME = os.getenv('GITHUB_REPO_NAME', 'micro-allinone2-port')

def get_blog_posts():
    posts = []
    content_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'contents')

    if not os.path.exists(content_dir):
        os.makedirs(content_dir)  # Ensure contents directory exists

    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            # Extract title and date from filename
            # Improved title extraction to remove slug part for cleaner display
            parts = os.path.splitext(filename)[0].split("-")
            date_str_parts = parts[0:6]  # YYYY-MM-DD-HH-MM-SS
            title_parts = parts[6:]  # The rest is the slug
            
            title = ' '.join(title_parts).title() if title_parts else "Untitled Post"
            
            # Reconstruct date string for sorting
            date_sort_key = "-".join(date_str_parts) if len(date_str_parts) == 6 else "1970-01-01-00-00-00"
            display_date = datetime.strptime(date_sort_key, "%Y-%m-%d-%H-%M-%S").strftime("%Y-%m-%d %H:%M")

            posts.append({
                'filename': filename,
                'title': title,
                'date': display_date,
                'date_sort_key': date_sort_key
            })
    # Sort posts by date_sort_key, newest first
    posts.sort(key=lambda x: x['date_sort_key'], reverse=True)
    return posts

@app.route('/')
def hello():
    posts = get_blog_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<filename>')
def post(filename):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'contents', filename)
    
    if not os.path.exists(filepath):
        abort(404)  # Return 404 if file not found

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        html_content = markdown.markdown(content)

    # Extract title, similar to get_blog_posts for consistency
    parts = os.path.splitext(filename)[0].split("-")
    title_parts = parts[6:]  # The rest is the slug
    title = ' '.join(title_parts).title() if title_parts else "Untitled Post"

    return render_template('post.html', post={'title': title, 'html_content': html_content})

@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
    data = {'phy':50,'che':60,'maths':70}
    return render_template('result.html', result=data)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/trigger-gh-action', methods=['POST'])
def trigger_github_action_internal():
    github_token = os.getenv('GHTOKEN')
    if not github_token:
        return 'GitHub token not configured', 500

    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {github_token}',
    }
    data = {
        "event_type": "create-dated-file",
    }

    try:
        response = requests.post(
            f'https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/dispatches',
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return 'GitHub Actions workflow triggered successfully (internal)', 200
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error triggering GitHub Action: {e}")
        return f'Error triggering GitHub Action: {e}', 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
