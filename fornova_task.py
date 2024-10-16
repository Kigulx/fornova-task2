import argparse
import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from json_formatter import extract_rates
from urllib.parse import urlencode

# Function to scrape data from the target website
def scrape_data(driver, hotel_id, check_in, check_out):
    params = {
        'adults': 2,
        'checkIn': check_in,
        'checkOut': check_out,
        'children': 0,
        'infants': 0,
        'location': 'London, England, United Kingdom',
        'page': 1,
        'payWith': 'cash',
        'searchType': 'list',
        'sortBy': 'popularity'
    }

    base_url = f"https://www.qantas.com/hotels/properties/{hotel_id}?{urlencode(params)}"
    print(f"Opening URL: {base_url}")

    # URL of the target request to intercept
    target_url = f"https://www.qantas.com/hotels/api/ui/properties/{hotel_id}/availability?checkIn={params['checkIn']}&checkOut={params['checkOut']}&adults={params['adults']}&children={params['children']}&infants={params['infants']}&payWith={params['payWith']}"
    print(f"Target URL: {target_url}")

    driver.get(base_url)

    # Wait for the page to fully load by waiting for a specific element
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Page loaded")

    # Get network logs from the browser for further analysis
    logs = driver.get_log('performance')
    print(f"Collected {len(logs)} logs")

    # Filter logs to find the response containing room availability data
    relevant_logs = [
        json.loads(log['message'])['message']
        for log in logs if 'message' in json.loads(log['message']) and json.loads(log['message'])['message']['method'] == 'Network.responseReceived'
    ]
    print(f"Filtered {len(relevant_logs)} relevant logs")

    # Locate and extract the desired JSON response from network logs
    for log_data in relevant_logs:
        if 'params' in log_data and 'response' in log_data['params'] and 'url' in log_data['params']['response']:
            url = log_data['params']['response']['url']
            if url == target_url:
                request_id = log_data['params']['requestId']
                response = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                json_data = response['body']
                print("JSON successfully intercepted and saved.")
                return json_data, params

    print("Target URL not found in logs")
    return None, params

# Main execution block
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Scrape hotel data and save to JSON.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file containing hotel_id, check_in, and check_out combinations')
    args = parser.parse_args()

    options = Options()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        print(f"Reading CSV file: {args.csv_file}")
        # Read the CSV file containing hotel_id, check_in, and check_out combinations
        with open(args.csv_file, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)
            print(f"Found {len(rows)} rows in the CSV file")
            for row in rows:
                hotel_id = row['hotel_id']
                check_in = row['check_in']
                check_out = row['check_out']
                print(f"Processing hotel_id: {hotel_id}, check_in: {check_in}, check_out: {check_out}")

                # Scrape the data for each combination
                raw_json_data, params = scrape_data(driver, hotel_id, check_in, check_out)
                if raw_json_data:
                    # Parse the intercepted JSON data
                    parsed_json_data = json.loads(raw_json_data)
                    print("Parsed JSON data")

                    # Extract rates information from the parsed JSON data
                    rates_data = extract_rates(parsed_json_data, params)
                    print("Extracted rates data")

                    # Save the extracted rates information to a JSON file
                    output_file = f'OUTPUT_{hotel_id}_{check_in}_{check_out}_2.json'
                    with open(output_file, 'w+', encoding='utf-8') as f:
                        json.dump({"rates": rates_data}, f, indent=2)
                    print(f"Saved data to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the browser is properly closed
        driver.quit()
        print("Driver closed")