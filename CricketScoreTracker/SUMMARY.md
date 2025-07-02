# Cricket Score Tracker - Project Summary

## Overview
Cricket Score Tracker is a responsive mobile web application built with Python Flask, HTML, CSS, and JavaScript. It allows users to track cricket match scores with detailed team and player statistics.

## Features Implemented

### Team Management
- Create teams with custom names
- Delete teams
- View list of all teams with summary statistics

### Player Management
- Add players to teams
- Delete players from teams
- View player list with summary statistics

### Scoring System
- Track detailed player statistics:
  - Sixes (6 runs each)
  - Fours (4 runs each)
  - Other runs
  - Wickets taken
- Track team extras:
  - Wide balls
  - No balls
- Automatic calculation of total runs

### Statistics and Summary
- View comprehensive team summary
- View detailed player statistics
- Automatic identification of best batsman and bowler
- Sortable player list by performance

### User Interface
- Responsive design that works on all screen sizes
- Mobile-first approach for optimal mobile experience
- Three beautiful themes:
  - Neon (default)
  - Sunset
  - Ocean
- Animated transitions and effects
- Intuitive card-based layout
- Help page with usage instructions

### Technical Features
- Single-page application architecture
- Local storage for data persistence
- Progressive Web App (PWA) capabilities:
  - Service worker for offline functionality
  - Web app manifest for installability
  - Responsive design for all devices
- Clean, modular code structure

## Project Structure
```
CricketScoreTracker/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── run.bat                # Windows batch file to run the app
├── SUMMARY.md             # Project summary
├── static/
│   ├── styles.css         # Additional CSS styles
│   ├── script.js          # Additional JavaScript
│   ├── service-worker.js  # Service worker for PWA
│   └── manifest.json      # Web app manifest
└── templates/
    ├── index.html         # Main application (with embedded CSS/JS)
    └── help.html          # Help page
```

## How to Run
1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```
   or double-click `run.bat` on Windows

3. Access the application:
   - Locally: http://127.0.0.1:5000
   - From other devices on the same network: http://YOUR_IP_ADDRESS:5000

## Future Enhancements
- Export match summary as PDF
- Share scorecard via social media
- Save and load previous matches
- Timer/overs management
- Cloud sync using Firebase
- Team vs Team match tracking
- Player performance history and statistics
- Advanced analytics and visualizations