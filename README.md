# Hotel Availability Scraper / Fornova-home-task

This project is a web scraper that extracts hotel availability and pricing information from Qantas' website using Selenium and Python. The scraper is capable of intercepting network requests to capture JSON data related to room offers, which is then processed and saved to a file for further analysis.

## Features
- Uses Selenium to automate the browser and intercept network requests.
- Extracts detailed hotel room rates, including room names, prices, cancellation policies, and more.
- Saves the extracted data to a JSON file for later use.

## Prerequisites
To run this project, you will need the following:
- Python 3.8+
- Google Chrome browser
- ChromeDriver (ensure the version matches your Chrome browser)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Kigulx/fornova-task2.git
   cd fornova-task2
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Prepare a CSV file (e.g., test.csv) with columns for hotel_id, check_in, and check_out. The CSV file should include multiple hotel IDs and date combinations, for example:

test.csv:

   ```csv
   hotel_id,check_in,check_out
   18482,2024-10-27,2024-10-28
   18482,2024-10-28,2024-10-29
   18482,2024-10-29,2024-11-30
   ```
Run the script:

2. Run the script to start scraping:
   ```sh
   python fornova_task.py test.csv
   ```
The script will iterate over each row in the CSV file, scrape the hotel availability data for each combination, and save the results in separate JSON files.

3. After the scraping is complete, the extracted data will be saved in a JSON file named in the format `OUTPUT_<hotel_id>_<checkIn>_<checkOut>_<adults>.json`.

## Usage without a Virtual Environment

If you prefer not to use a virtual environment, you can install all the required packages globally. Here are the steps you need to follow:

1. Ensure you have Python and pip installed. To check, run the following commands in your terminal:
   ```sh
   python --version
   pip --version
2. Install the required packages globally:
   ```sh
   pip install selenium
3. Download and install ChromeDriver, ensuring that its version matches your Chrome browser version. Place the chromedriver executable in a directory included in your system's PATH, or specify the path to chromedriver in your code.
4. Run the script to start scraping:
   ```sh
   python fornova_task.py test.csv
   ```

## Project Structure
- `fornova_task.py`: The main script to initiate the scraping process.
- `json_formatter.py`: Contains the `extract_rates` function, which processes the extracted JSON data.
- `requirements.txt`: Lists the required Python packages for the project.
- `test.csv`: A sample CSV file with three example hotel ID and date combinations for testing.
- `OUTPUT_18482_2024-10-29_2024-10-30_2.json`: Example of JSON output.
## Important Notes
- Make sure you have the correct version of ChromeDriver installed to match your browser version.
- This script uses Selenium, which involves browser automation. Be mindful of Qantas' website terms of service.
## TODO
- Implement proxy support to handle requests more efficiently and avoid IP blocking.

