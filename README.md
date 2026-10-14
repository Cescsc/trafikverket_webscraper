# Trafikverket Webscraper

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium&logoColor=white)

A small personal project from September 2023 for checking driver test availability at Trafikverket using Selenium.

This repository opens a browser, navigates to the Trafikverket booking page, selects the relevant test type and vehicle type, and checks whether a time slot is available. If a booking appears, the script exits and optionally plays a beep through the system notification sound.

## Overview

This project was built as a simple automation tool for personal use. It is intentionally minimal and focused on a very specific task: detecting open driver test slots.

## Features

- Opens the Trafikverket booking page in a browser
- Selects test and vehicle type automatically
- Searches for a specific location (currently configured for Sollentuna in the script)
- Stops as soon as a slot is found
- Plays a system beep when a result is found

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver matching your Chrome version
- Selenium

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Cescsc/trafikverket_webscraper.git
   cd trafikverket_webscraper
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install selenium
   ```

4. Make sure ChromeDriver is available on your PATH. If not, place it in a folder that is already on your PATH or specify its location manually.

## Running the project

The main entry point is `launcher.py`:

```bash
python launcher.py
```

This script repeatedly calls the logic in `korkort.py` until a booking is found. When a time is found, it exits and plays a system beep.

## Configuration

The script currently contains hardcoded booking settings such as:

- test type: `Körprov`
- vehicle type: `Automatbil`
- location: `Sollentuna`

If you want to change these values, edit the relevant lines in `korkort.py`.

## How it works

- The script creates a Chrome browser instance with Selenium
- It loads the Trafikverket booking page
- It selects the driver test and car type
- It enters the desired location and submits the search
- If the booking button is available, it prints `Time found!` and exits
- If no slot is available, it waits and retries

## Notes

- This project is for personal use and was created as a small automation experiment.
- The Trafikverket website may change its markup or flow over time, which could break the scraper.
- Please use it responsibly and avoid excessive requests to the site.
- This project is not affiliated with Trafikverket.

## Contributing

This is a small personal project, but improvements are welcome. If you want to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your change
4. Open a pull request with a short explanation of what changed

## License

This repository does not currently include a formal license. If you plan to share or reuse it more broadly, adding an open-source license such as MIT is recommended.

## Project status

- Created: September 2023
- Status: personal / experimental project
