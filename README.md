# Daffodil CSE61 Student CGPA Scrapper

This project is a web application designed to fetch student results from a specified API, calculate SGPA and CGPA for each student, and generate an Excel sheet containing the results.

## Project Structure

```
student-results-processor
├── src
│   ├── app.py                # Main entry point of the application
│   ├── services              # Contains service classes for API, calculations, and Excel generation
│   │   ├── api_service.py    # Handles API requests to fetch student results
│   │   ├── calculation_service.py # Performs SGPA and CGPA calculations
│   │   └── excel_service.py   # Generates Excel sheets with student results
│   ├── models                # Contains data models for students and results
│   │   ├── student.py        # Defines the Student class
│   │   └── result.py         # Defines the Result class
│   ├── utils                 # Utility functions and constants
│   │   ├── constants.py      # Constant values used throughout the application
│   │   └── helpers.py        # Utility functions for data formatting and validation
│   └── templates             # HTML templates for the web application
│       └── index.html        # User interface for inputting student IDs
├── requirements.txt          # Lists project dependencies
├── config.py                 # Configuration settings for the application
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd student-results-processor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage

- Access the web application in your browser at `http://localhost:5000`.
- Input the start and end student IDs to fetch results and generate the Excel sheet.

## License

This project is licensed under the MIT License.
