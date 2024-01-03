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
    pip3 install -r requirements.txt
    ```

4. Set up your API key:

    - Obtain an API key from [Open Exchange Rates](https://openexchangerates.org/signup).
    - Create a `.env` file in the project directory and add your API key:

        ```env
        API_KEY=your_api_key_here
        ```

5. Run the script:

    ```bash
    python3 tk_currency_converter.py
    ```

6. Follow the on-screen prompts to perform currency conversions.

## Usage

- Enter the original currency, amount, and target currency when prompted.
- The interface will display the converted amount based on the latest exchange rates.

## MacOS Software Guide

For users operating `MacOS`, currency-converter software is availbale as **"Rapid Rates"** for everyday use or testing on local computer as MacOS application. Follow steps below for installation guide:

- Download [Rapid Rates app for Mac](https://drive.google.com/uc?export=download&id=1FxyEmntl9X6TbtusIBEjEDM0ZZd6iNiW)
- Unzip downloaded file and run application.
- Usually, you should recieve the error below that prevents application run:
  
  ![Error](https://github.com/idaraabasiudoh/ERROR/blob/main/ERROR.png)

- While the option to proceed is available for those willing to accept associated risks, it is crucial to exercise caution. To proceed at your own risk, navigate to ``System settings -> Privacy & Security -> Security``
- Under `Security`, locate dialog frame displaying ``"Rapid Rates.app" was blocked from use because it is not from an identified developer``
- Select `Open Anyways`, complete security check and select `open` on new pop-up window to run software securely.

- **DISCLAIMER:** The utilization of the software is undertaken entirely at your own risk, and the user experience may be contingent upon the specifications of your operating system. You bear full responsibility for both the installation and usage of the software. If there is any uncertainty regarding the associated risks, it is advised to refrain from proceeding with the ``MacOS Software Guide``.

## Contributing

Contributions are welcome! If you'd like to improve the currency converter, feel free to submit pull requests or open issues.
