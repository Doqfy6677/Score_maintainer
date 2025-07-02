from app import app

# This file is needed for Vercel deployment
# It imports the Flask app from app.py and makes it available to Vercel

if __name__ == '__main__':
    app.run()