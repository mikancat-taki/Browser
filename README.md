# Browser Application

This project is a simple web browser application that allows users to perform searches using Google. It is built using JavaScript for the frontend and Python for the backend.

## Project Structure

- `src/main.js`: Entry point of the application. Initializes the basic browser functionalities and renders the search bar and browser window components.
- `src/main.py`: Contains the backend logic written in Python. Handles requests to the Google search engine and retrieves search results.
- `src/components/BrowserWindow.js`: Defines the browser window component. Includes UI elements to display search results.
- `src/components/SearchBar.js`: Defines the search bar component. Provides functionality for users to input search queries and execute searches.
- `src/templates/index.html`: HTML template for the application. Defines the basic structure of the browser and includes links to JavaScript and CSS files.
- `src/types/index.d.ts`: Contains TypeScript type definitions. Defines types and interfaces used within the application.
- `public/style.css`: Stylesheet for the application. Applies styles to the browser's UI elements.
- `package.json`: npm configuration file. Lists project dependencies and scripts.
- `requirements.txt`: Lists Python dependencies. Used to install necessary packages.
- `tsconfig.json`: TypeScript configuration file. Specifies compiler options and files to include in the compilation.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd browser-app
   ```

2. **Install frontend dependencies**:
   ```
   npm install
   ```

3. **Install backend dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   - Start the backend server:
     ```
     python src/main.py
     ```
   - Open the frontend in your browser:
     ```
     open src/templates/index.html
     ```

## Features

- Search functionality using Google.
- User-friendly interface with a search bar and results display.
- Responsive design with CSS styling.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.