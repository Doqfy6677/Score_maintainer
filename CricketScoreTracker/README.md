# Cricket Score Tracker

A responsive mobile web application for tracking cricket scores with team and player management.

## Features

- Create and manage teams
- Add and delete players
- Track player scores (runs, sixes, fours, wickets)
- Track team extras (wide balls, no balls)
- View best batsman and bowler
- Team and player statistics summary
- Multiple theme options
- Responsive design for mobile devices
- Data persistence using local storage

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory
2. Run the Flask application:

```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`
4. For mobile access, make sure your computer and mobile device are on the same network, then access the application using your computer's IP address: `http://YOUR_IP_ADDRESS:5000`

## Usage

1. Create a team by entering a team name and clicking "Create Team"
2. Click on a team to manage its players
3. Add players to the team
4. Click on a player to start scoring
5. Use the scoring buttons to add runs, wickets, etc.
6. View team summary to see overall statistics

## Technologies Used

- Python Flask for the backend
- HTML5, CSS3, and JavaScript for the frontend
- Local Storage for data persistence
- Responsive design for mobile compatibility

## Themes

The application includes three themes:
- Neon (default)
- Sunset
- Ocean

You can switch between themes using the theme selector in the header.