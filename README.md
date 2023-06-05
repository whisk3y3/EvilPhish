# EvilPhish

EvilPhish is a tool designed for phishing simulations and testing the security awareness of individuals or organizations. It provides a framework for serving a phishing domain and monitoring captured credentials. The webpage is designed to persuade users to login using their network credentials, following a successful copmuter patch verification scan.

**Note: Before performing the assessment, you will need to buy a domain and generate DNS and A records pointing to the server running EvilPhish.**

## Tool Contents

- `EvilPhish.py`: The main Python script that serves the credential harvesting webpage.
- `LICENSE.txt`: The license file for EvilPhish (MIT License).
- `README.md`: This file provides instructions and information about the tool.
- `Requirements.txt`: A list of required Python packages.
- `templates/`: A directory containing templates for the phishing campaign.
  - `index.html`: The HTML template for the phishing page.
- `static/`: A directory containing static assets for the phishing page.
  - `css/`: A directory containing CSS stylesheets.
    - `styles.css`: The CSS file for styling the phishing page.
  - `images/`: A directory containing images used in the phishing page.
    - `EvilPhish_Logo.png`: The logo image for EvilPhish.

## Getting Started

1. Clone or download the EvilPhish repository.
2. Install the required Python packages using `pip install -r Requirements.txt`.
3. Update the `index.html` file in the `templates/` directory with your organization's branding.
4. Place any additional images or assets in the appropriate directories in the `static/` directory.

### Generating SSL/TLS Certificates

5. Generate SSL/TLS certificate and private key files:
   - Open a terminal and navigate to the EvilPhish directory.
   - Run the following command to generate the SSL/TLS certificate and private key files:

     ```bash
     sudo openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout private_key.key -out ssl_certificate.crt -days 365
     ```

   - This command generates a self-signed certificate and private key pair that is valid for 365 days.
   - Save the generated `private_key.key` and `ssl_certificate.crt` files in a secure location.

### Configuring EvilPhish

6. Edit the path to the private key file and certificate file in the `EvilPhish.py` script:
   - Open `EvilPhish.py` in a text editor.
   - Locate the lines that specify the `key_file` and `cert_file` variables.
   - Update the file paths to reflect the locations where you saved each file.

7. Customize the email domain and password policy in the `EvilPhish.py` script:
   - Open `EvilPhish.py` in a text editor.
   - Find the following line of code:

     ```
    if email.endswith('@evilphishinc.com') and len(password) >= 8:

     ```

   - Modify the domain name to match your organization.

### Running EvilPhish

8. Start EvilPhish:
   - Open a terminal and navigate to the EvilPhish directory.
   - Run the following command to start the phishing simulation:

     ```bash
     sudo python3 EvilPhish.py
     ```

9. Monitor captured credentials:
   - Open a separate terminal window.
   - Navigate to the EvilPhish directory.
   - Run the following command to tail the `credentials.txt` file and monitor captured credentials:

     ```bash
     tail -f credentials.txt
     ```

   - You will see the captured credentials in real-time as the targets interact with the phishing page.

## Disclaimer

Please note that EvilPhish should only be used for authorized and legal security testing purposes. The misuse of this tool can violate privacy laws and may have serious legal consequences. The developer of this tool is not responsible for any illegal or unethical activities performed using this tool.

## Contributing

Contributions to EvilPhish are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on GitHub.

## License

EvilPhish is released under the [MIT License](LICENSE).
