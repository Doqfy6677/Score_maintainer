# Fixing 404 Error on Vercel Deployment

If you're encountering a 404 error after deploying your Cricket Score Tracker app to Vercel, follow these steps to fix it:

## Step 1: Check Your Project Structure

Make sure your project structure is correct:
- app.py (main Flask application)
- index.py (entry point for Vercel)
- vercel.json (configuration for Vercel)
- requirements.txt (dependencies)
- static/ (static files)
- templates/ (HTML templates)

## Step 2: Update Your vercel.json

Make sure your vercel.json file looks like this:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "PYTHONUNBUFFERED": "1"
  }
}
```

## Step 3: Deploy with the Vercel CLI

1. Install the Vercel CLI:
   ```
   npm install -g vercel
   ```

2. Login to Vercel:
   ```
   vercel login
   ```

3. Deploy with the --prod flag:
   ```
   vercel --prod
   ```

## Step 4: Check Vercel Logs

If you're still encountering issues:

1. Go to your Vercel dashboard
2. Select your project
3. Go to the "Deployments" tab
4. Click on the latest deployment
5. Check the "Functions" tab for any errors

## Step 5: Try Alternative Deployment Methods

If Vercel continues to give you issues, consider these alternatives:

1. **Render.com**: Excellent for Python applications
   - Sign up at render.com
   - Create a new Web Service
   - Connect your repository
   - Set the build command: `pip install -r requirements.txt`
   - Set the start command: `gunicorn app:app`

2. **PythonAnywhere**: Specifically designed for Python web apps
   - Sign up at pythonanywhere.com
   - Upload your code
   - Set up a web app with Flask

## Additional Troubleshooting

If you're still having issues with the 404 error:

1. Make sure your app.py has a route for the root path ('/'):
   ```python
   @app.route('/')
   def index():
       return render_template('index.html')
   ```

2. Check that your templates directory contains index.html

3. Try adding a simple test route to verify the app is running:
   ```python
   @app.route('/test')
   def test():
       return "App is running!"
   ```

4. Make sure your requirements.txt includes all necessary dependencies:
   ```
   flask==2.0.1
   gunicorn==20.1.0
   ```