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
   git clone https://github.com/yourusername/hotel-availability-scraper.git
   cd hotel-availability-scraper
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
1. Update the `params` dictionary in `ultra.py` with the desired hotel details, including check-in and check-out dates, number of guests, and location.

2. Run the script to start scraping:
   ```sh
   python ultra.py
   ```

3. After the scraping is complete, the extracted data will be saved in a JSON file named in the format `OUTPUT_<hotel_id>_<checkIn>_<checkOut>_<adults>.json`.

## Project Structure
- `ultra.py`: The main script to initiate the scraping process.
- `json_formatter.py`: Contains the `extract_rates` function, which processes the extracted JSON data.
- `requirements.txt`: Lists the required Python packages for the project.

## Important Notes
- Make sure you have the correct version of ChromeDriver installed to match your browser version.
- This script uses Selenium, which involves browser automation. Be mindful of Qantas' website terms of service.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Disclaimer
This project is for educational purposes only. Scraping websites without permission may be against their terms of service.
