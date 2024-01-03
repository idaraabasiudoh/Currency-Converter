# Currency Converter

This simple currency converter is a Python script that uses the Open Exchange Rates API to convert between different currencies. It retrieves the latest exchange rates and performs currency conversions based on user input. Users can interact with program through user-friendly GUI

## Features

- Convert between various currencies.
- Retrieve real-time exchange rates from the Open Exchange Rates API.
- Easy-to-use GUI.

## Prerequisites

Before using the currency converter, make sure you have the following:

- Python installed on your machine ([Download Python](https://www.python.org/downloads/))
- API key from Open Exchange Rates (instructions on obtaining the key below)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/idaraabasiudoh/currency-converter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd currency-converter
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your API key:

    - Obtain an API key from [Open Exchange Rates](https://openexchangerates.org/signup).
    - Create a `.env` file in the project directory and add your API key:

        ```env
        API_KEY=your_api_key_here
        ```

5. Run the script:

    ```bash
    python currency_converter.py
    ```

6. Follow the on-screen prompts to perform currency conversions.

## Usage

- Enter the original currency, amount, and target currency when prompted.
- The interface will display the converted amount based on the latest exchange rates.

## Contributing

Contributions are welcome! If you'd like to improve the currency converter, feel free to submit pull requests or open issues.
