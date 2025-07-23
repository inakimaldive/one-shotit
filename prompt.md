Let's address the identified issues and refine the project for better security, robustness, and reusability.

"""
FILE: README.md
Micro-Allinone2-Port: A Flask-Based Micro-Blogging Platform
This project is a lightweight and straightforward micro-blogging platform built with Flask. It's designed for easy deployment on Vercel and uses a simple file-based approach for managing blog posts.

Features
Flask-Powered: A robust and popular micro-framework for Python.

Markdown-Based Content: Blog posts are written in Markdown, making them easy to create and edit.

Dynamic Post Listing: The homepage automatically lists all available blog posts, sorted by date.

Vercel-Ready: Includes a vercel.json file for seamless deployment to the Vercel platform.

Automated Content Creation: A GitHub Actions workflow can be triggered to automatically create new, dated Markdown files for blog posts.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.12 or higher

pip for installing Python packages

Installation
Clone the repository:

Bash

git clone https://github.com/inakimaldive/micro-allinone2-port.git
cd micro-allinone2-port
Create and activate a virtual environment:

Bash

python -m venv myenv
source myenv/bin/activate
Install the required dependencies:

Bash

pip install -r requirements.txt
Running the Application
The start.sh script is provided to simplify the process of running the application. It will automatically handle any conflicting processes on port 5000, activate the virtual environment, and start the Flask development server.

Bash

./start.sh
The application will be available at http://127.0.0.1:5000.

Deployment
This project is configured for easy deployment to Vercel. The vercel.json file contains the necessary rewrite rules to ensure that all incoming requests are correctly routed to the Flask application.

API Endpoints
GET /: The main page, which displays a list of all blog posts.

GET /post/<filename>: Displays a single blog post. The <filename> should be the name of the Markdown file in the contents directory (e.g., 2025-07-21-11-10-49.md).

POST /trigger-gh-action: A webhook endpoint that triggers a GitHub Actions workflow to create a new, dated Markdown file in the contents directory. This endpoint is primarily for internal use by the Vercel serverless function.

POST /api/trigger-action: (Vercel Serverless Function) This is the primary endpoint for the frontend to trigger a GitHub Actions workflow.

Content Management
To add a new blog post, simply create a new Markdown file in the contents directory. The filename should follow the format YYYY-MM-DD-HH-MM-SS.md. The title of the post is derived from the filename.

GitHub Actions Integration
The project includes a GitHub Actions workflow defined in .github/workflows/create-file.yml. This workflow is triggered by a repository_dispatch event with the event_type of create-dated-file. When triggered, it creates a new Markdown file in the contents directory with the current date and time as the filename.

The POST /api/trigger-action endpoint (exposed via Vercel's serverless functions) can be used to trigger this workflow. You will need to provide a GitHub personal access token with the repo scope as the GHTOKEN environment variable for the request to be authenticated.

================================================ FILE: 2025-07-21-10-35-48.md
[Empty file]

================================================ FILE: github-actions-and-hooks.md
Expanding GitHub Actions and Webhooks
This document explores ideas for expanding the use of GitHub Actions and webhooks to further automate and enhance the functionality of the micro-blogging platform.

1. Enhancing the Existing create-dated-file Workflow
The current workflow is simple but can be made more powerful.

Pass Content via Dispatch Payload: Modify the trigger-action.js and the GitHub Actions workflow (create-file.yml) to accept a title and content in the client_payload of the dispatch event. This would allow for creating a new post with a specific title and initial content directly from an API call, rather than just an empty file.

Create a Simple Frontend Form: Build a simple HTML form in the admin section of the site that takes a title and content, then makes a POST request to the /api/trigger endpoint. This would provide a basic UI for creating new posts without needing to commit files manually.

Generate SEO-Friendly Slugs: Instead of just using the date and time, the workflow could take a post title and generate a URL-friendly slug (e.g., my-first-post), then append the date to it.

2. New GitHub Actions Workflows
Continuous Integration & Deployment (CI/CD)
Automated Testing: Create a workflow that runs on every push or pull_request to the main branch.

Linting: Use a Python linter like ruff or flake8 to check the code for style and errors.

Unit Tests: Run the test suite using pytest to ensure new changes don't break existing functionality.

Automated Deployment to Vercel: Set up the Vercel GitHub integration. Create a workflow that automatically deploys the application to production whenever changes are merged into the main branch, after all tests have passed.

Content Management & Validation
Markdown Linting: Create a workflow that uses a tool like markdownlint to check all .md files in the contents/ directory for formatting errors or inconsistencies. This can be triggered on pull_request.

Broken Link Checker: Set up a scheduled workflow (e.g., runs once a day) that scans all rendered blog posts for broken internal or external links and creates a GitHub Issue if any are found.

3. Advanced Webhook Integration
External Service Integration
Social Media Notifications: When a new post is created (i.e., a new file is added to the contents directory and pushed to main), a webhook could trigger a GitHub Action to automatically post a link to the new article on social media platforms like X (formerly Twitter) or a Discord server.

Email Newsletters: For a more advanced setup, a webhook could trigger a service like Mailchimp or SendGrid to send out a newsletter to subscribers announcing the new post.

Git-Based Commenting System
Leverage GitHub Issues: A webhook could be configured to listen for comments on specific GitHub Issues that are associated with blog posts.

Action-Powered Comment Updates: When a new comment is posted on a linked issue, a GitHub Action could be triggered. This action would pull the comment content and append it to the corresponding post's data or a separate comments file, effectively creating a static, git-based commenting system.

4. Security and Best Practices
Webhook Secret Verification: The Flask application should verify the signature of incoming webhook payloads from GitHub using a shared secret. This ensures that the requests are genuinely from GitHub and not from a malicious third party.

Secure Token Handling: Ensure that the GHTOKEN is stored securely as a GitHub Secret in the repository settings and is only used in workflows that require it. Avoid exposing it in logs or client-side code.

================================================ FILE: improvements.md
Project Improvement Suggestions
This document outlines potential next steps and improvements for the Micro-Allinone2-Port project.

Core Functionality
Database Integration: Replace the file-based post storage with a database (e.g., SQLite, PostgreSQL). This would provide more robust data management, especially as the number of posts grows.

User Authentication: Implement a user authentication system to allow for registered authors and an admin interface for managing posts.

Content Management System (CMS): Create a simple CMS to allow authors to write, edit, and delete posts through a web interface, rather than by adding files to the contents directory.

Search Functionality: Add a search feature to allow users to easily find posts based on keywords.

Categorization and Tagging: Implement a system for categorizing and tagging posts to improve organization and discoverability.

User Experience
Frontend Framework: Utilize a modern frontend framework like React or Vue.js to create a more dynamic and interactive user experience.

Improved Styling: Enhance the visual design of the blog with more advanced CSS or a CSS framework like Bootstrap or Tailwind CSS.

Pagination: For the blog post list, implement pagination to improve performance and usability as the number of posts increases.

Technical Enhancements
Comprehensive Testing: Develop a suite of unit and integration tests to ensure the application is robust and to prevent regressions.

CI/CD Pipeline: Set up a Continuous Integration/Continuous Deployment (CI/CD) pipeline to automate the testing and deployment process.

Enhanced Error Handling: Improve the application's error handling to provide more informative feedback to users and developers.

Security Hardening: Implement security best practices to protect against common web vulnerabilities such as Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF).

Static Site Generation (SSG): For improved performance and security, consider using a static site generator. The blog content could be converted into static HTML files that are served directly to users.

================================================ FILE: requirements.txt
Flask
python-dotenv
markdown
requests # Added for making secure HTTP requests

================================================ FILE: start.sh
#!/bin/sh

Check and kill conflicting processes on port 5000
echo "Checking for processes on port 5000..."
PID=$(lsof -t -i:5000)

if [ -n "$PID" ]; then
echo "Process with PID $PID found on port 5000. Killing it..."
kill -9 "$PID"
echo "Process killed."
else
echo "No conflicting processes found on port 5000."
fi

Activate the virtual environment
echo "Activating virtual environment..."
. myenv/bin/activate

Run the Flask application
echo "Starting Flask application..."
./myenv/bin/flask run

================================================ FILE: vercel.json
{
"rewrites": [
{ "source": "/admin", "destination": "/api/index" },
{ "source": "/(.*)", "destination": "/api/index" }
],
"functions": {
"api/trigger-action.js": {
"memory": 128
}
}
}

================================================ FILE: api/index.py
from flask import Flask, render_template, url_for, abort, request
import os
import markdown
from datetime import datetime
import requests # Import the requests library
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = Flask(name)

Load repository owner and name from environment variables
GITHUB_REPO_OWNER = os.getenv('GITHUB_REPO_OWNER', 'inakimaldive')
GITHUB_REPO_NAME = os.getenv('GITHUB_REPO_NAME', 'micro-allinone2-port')

def get_blog_posts():
posts = []
content_dir = os.path.join(os.path.dirname(os.path.abspath(file)), '..', 'contents')

if not os.path.exists(content_dir):
    os.makedirs(content_dir) # Ensure contents directory exists

for filename in os.listdir(content_dir):
    if filename.endswith(".md"):
        # Extract title and date from filename
        # Improved title extraction to remove slug part for cleaner display
        parts = os.path.splitext(filename)[0].split("-")
        date_str_parts = parts[0:6] # YYYY-MM-DD-HH-MM-SS
        title_parts = parts[6:] # The rest is the slug
        
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

@app.route('/post/

if not os.path.exists(filepath):
    abort(404) # Return 404 if file not found

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    html_content = markdown.markdown(content)

# Extract title, similar to get_blog_posts for consistency
parts = os.path.splitext(filename)[0].split("-")
title_parts = parts[6:] # The rest is the slug
title = ' '.join(title_parts).title() if title_parts else "Untitled Post"

return render_template('post.html', post={'title': title, 'html_content': html_content})
@app.route('/test')
def test():
return 'Test'

@app.route('/result')
def result():
data = {'phy':50,'che':60,'maths':70}
return render_template('result.html', result = data)

@app.route('/admin')
def admin():
return render_template('admin.html')

This endpoint is internal and should ideally not be called directly from the frontend
The frontend now calls the Vercel serverless function /api/trigger-action
@app.route('/trigger-gh-action', methods=['POST'])
def trigger_github_action_internal():
# This endpoint is now specifically for an internal trigger,
# or if you decided to handle GitHub dispatch directly from Flask on a non-Vercel deploy.
# On Vercel, the api/trigger-action.js function handles this more securely.
# For local testing without Vercel, you would still need GHTOKEN set in your environment.

github_token = os.getenv('GHTOKEN')
if not github_token:
    return 'GitHub token not configured', 500

headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'token {github_token}',
}
data = {
    "event_type": "create-dated-file",
    # client_payload can be extended if this endpoint is meant to receive it
    # For now, it's just a basic trigger for the workflow.
    # The Vercel `api/trigger-action.js` passes payload from frontend.
}

try:
    response = requests.post(
        f'[https://api.github.com/repos/](https://api.github.com/repos/){GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/dispatches',
        headers=headers,
        json=data
    )
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    return 'GitHub Actions workflow triggered successfully (internal)', 200
except requests.exceptions.RequestException as e:
    app.logger.error(f"Error triggering GitHub Action: {e}")
    return f'Error triggering GitHub Action: {e}', 500
Basic error handlers for better user feedback
@app.errorhandler(404)
def page_not_found(error):
return render_template('404.html'), 404

Add a default 404.html template for better user experience
FILE: api/templates/404.html (create this file)
"""








404 - Page Not Found
The page you are looking for does not exist.

Go back to the homepage

"""
================================================ FILE: api/trigger-action.js
module.exports = async (req, res) => {
if (req.method !== 'POST') {
return res.status(405).json({ error: 'Method Not Allowed' });
}

const pat = process.env.GHTOKEN;
const repoOwner = process.env.GITHUB_REPO_OWNER || 'inakimaldive'; // Use environment variable for owner
const repoName = process.env.GITHUB_REPO_NAME || 'micro-allinone2-port'; // Use environment variable for name

if (!pat) {
return res.status(500).json({ error: 'GitHub PAT not configured' });
}

const { title, content } = req.body;

try {
const response = await fetch(https://api.github.com/repos/${repoOwner}/${repoName}/dispatches, {
method: 'POST',
headers: {
'Accept': 'application/vnd.github.v3+json',
'Authorization': token ${pat},
'Content-Type': 'application/json',
},
body: JSON.stringify({
event_type: 'create-dated-file',
client_payload: {
title: title || 'New Post',
content: content || ''
}
}),
});

if (response.ok) {
  res.status(200).json({ message: 'Webhook triggered successfully' });
} else {
  const errorData = await response.json();
  console.error('GitHub API error response:', errorData);
  res.status(response.status).json({ error: `GitHub API error: ${response.statusText}`, details: errorData });
}
} catch (error) {
console.error('Internal Server Error:', error);
res.status(500).json({ error: Internal Server Error: ${error.message} });
}
};

================================================ FILE: api/static/style.css
body {
font-family: sans-serif;
line-height: 1.6;
margin: 0;
padding: 0;
background: #f4f4f4;
color: #333;
}

.container {
width: 80%;
margin: auto;
overflow: hidden;
padding: 20px 0;
}

h1, h2 {
color: #333;
}

a {
color: #333;
text-decoration: none;
}

a:hover {
color: #000;
}

.blog-post {
background: #fff;
padding: 20px;
margin-bottom: 20px;
border-radius: 5px;
}

.post-meta {
font-size: 0.8em;
color: #666;
}

button {
background: #333;
color: #fff;
border: 0;
padding: 10px 15px;
cursor: pointer;
border-radius: 5px;
}

button:hover {
background: #555;
}

/* Added basic styling for 404 page /
.error-page {
text-align: center;
padding-top: 50px;
}
.error-page h1 {
font-size: 3em;
color: #d9534f; / A red-ish color */
}
.error-page p {
font-size: 1.2em;
}

================================================ FILE: api/templates/admin.html









Create New Post
<script>
    document.getElementById('create-post-form').addEventListener('submit', async (event) => {
        event.preventDefault();

        const title = document.getElementById('title').value;
        const content = document.getElementById('content').value;

        // Frontend now calls the Vercel serverless function /api/trigger-action
        const response = await fetch('/api/trigger-action', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, content }),
        });

        if (response.ok) {
            alert('Post creation triggered successfully! It may take a moment to appear.');
            window.location.href = '/';
        } else {
            const errorData = await response.json();
            alert(`Error creating post: ${errorData.error || response.statusText}. Check console for details.`);
            console.error('Error details:', errorData);
        }
    });
</script>
================================================ FILE: api/templates/index.html







My Awesome Blog
{% if posts %} {% for post in posts %}
{{ post.title }}
{{ post.date }}

{% endfor %} {% else %}
No blog posts yet. Start by creating one!

{% endif %}
================================================ FILE: api/templates/post.html







Back to Home
{{ post.title }}
{{ post.html_content | safe }}
================================================ FILE: api/templates/result.html



{% for key, value in result.items() %} {% endfor %}
{{ key }}	{{ value }}

Export to Sheets
================================================ FILE: api/templates/404.html







404 - Page Not Found
The page you are looking for does not exist.

Go back to the homepage

================================================ FILE: contents/2025-07-21-13-13-03.md
[Empty file]

================================================ FILE: myenv/pyvenv.cfg
home = /usr/bin
include-system-site-packages = false
version = 3.12.3
executable = /usr/bin/python3.12
command = /usr/bin/python -m venv /home/ignat/Documents/000_aa_more-actual-apps/auto-git-blog/flaskALLINONE-2/micro-bothinone/myenv

================================================ SYMLINK: myenv/lib64 -> lib
================================================ FILE: .github/workflows/create-file.yml
name: Create Dated File

on:
repository_dispatch:
types: [create-dated-file]

jobs:
create_file:
runs-on: ubuntu-latest
permissions:
contents: write
steps:
- name: Checkout code
uses: actions/checkout@v3

  - name: Create dated file
    run: |
      now=$(date +"%Y-%m-%d-%H-%M-%S")
      title="${{ github.event.client_payload.title || 'New Post' }}"
      content="${{ github.event.client_payload.content || '' }}"
      # Generate SEO-friendly slug
      slug=$(echo "$title" | iconv -t ascii//TRANSLIT | sed -r 's/[^a-zA-Z0-9]+/-/g' | sed -r 's/^-+|-+$//g' | tr '[:upper:]' '[:lower:]')
      filename="$now-$slug.md"

      mkdir -p contents
      echo -e "---\ntitle: $title\ndate: $now\n---\n\n$content" > "contents/$filename"

      git config --global user.name 'github-actions[bot]'
      git config --global user.email 'github-actions[bot]@users.noreply.github.com'
      git add "contents/$filename"
      git commit -m "Create post: $title"
      git push
================================================ FILE: .env.example
Example .env file - do NOT commit this to version control
Copy this to .env and fill in your values
GHTOKEN="your_github_personal_access_token_here"
GITHUB_REPO_OWNER="your_github_username"
GITHUB_REPO_NAME="your_repository_name"
