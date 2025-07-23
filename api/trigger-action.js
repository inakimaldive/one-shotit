module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }
  const pat = process.env.GHTOKEN;
  const repoOwner = process.env.GITHUB_REPO_OWNER || 'inakimaldive';
  const repoName = process.env.GITHUB_REPO_NAME || 'micro-allinone2-port';
  if (!pat) {
    return res.status(500).json({ error: 'GitHub PAT not configured' });
  }
  const { title, content } = req.body;
  try {
    const response = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/dispatches`, {
      method: 'POST',
      headers: {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': `token ${pat}`,
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
    res.status(500).json({ error: `Internal Server Error: ${error.message}` });
  }
};
