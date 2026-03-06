# Corn Weather Project

## Project Structure
- **src/**: Contains the source code for the project.
- **docs/**: Documentation files.
- **tests/**: Contains unit and integration tests.
- **pipeline/**: CI/CD pipeline configuration files.
- **web_app/**: The folder for the web application frontend and backend files.

## Quick Start Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/TylerRing/Math_301_Final.git
   cd Math_301_Final
   ```
2. Checkout the setup-corn-weather branch:
   ```bash
   git checkout setup-corn-weather
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Run the application:
   ```bash
   npm start
   ```

## Installation Instructions
Make sure you have the following installed:
- Node.js (v14 or higher)
- npm (comes with Node.js)
- Git

To install dependencies, navigate to the root of the project and run:
```bash
npm install
```

## Pipeline Setup
To set up the automated pipeline:
1. Configure your CI/CD platform (e.g., GitHub Actions, Travis CI).
2. Use the provided configuration files in the `pipeline/` directory as examples.
3. Make sure your secrets and environment variables are set according to your production requirements.

## Web App Features
- Interactive UI for displaying weather data.
- User authentication for personalized dashboards.
- Real-time data updates using WebSocket.
- Export features to download reports.

## Automated Pipeline Details
The pipeline automates the following:
- Code quality checks using ESLint
- Running tests
- Building the application for production
- Deployment to selected hosting service (Heroku, AWS, etc.)

## Troubleshooting
- If you encounter installation issues, make sure Node.js and npm are properly installed.
- For pipeline errors, check logs in your CI/CD platform for detailed error messages.
- If the web app is unresponsive, ensure the backend server is running and no port conflicts are present.
