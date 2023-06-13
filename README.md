# Axiom

Axiom is a web-based password manager written in Flask. It allows you to easily and securely save your passwords. Every password saved on the site is encrypted and only accessible to you.

This project was developed as the Final Project for the CS50x Course.

## Demo

You can watch a video demo of the project [here](https://youtu.be/Z8jpD8sJ0tk).

## Project Structure

Explanation of each file:

1. **app.py**: This file contains the setup for Flask, including the secret key, session settings, database access, and registration of other site files. It also handles 404 and 500 error pages.

2. **helper.py**: This file contains helper functions used throughout the project:
   - `login_required`: This function prevents unauthorized access to specific pages by requiring users to log in.
   - `encryption`: This function uses the [Cryptography](https://pypi.org/project/cryptography/) library to encrypt messages passed as parameters.
   - `decryption`: This function decrypts messages using the same encryption procedure.

3. **auth.py**: This file contains functions related to user authentication:
   - `login`: Allows users to log in using their credentials.
   - `register`: Enables users to create an account by providing a username and password.
   - `logout`: Logs out the user, requiring them to log in again to access their passwords.

4. **views.py**: This file contains important functions of the site, including:
   - `index`: Displays all saved passwords in a table on the main page by connecting to the database.
   - `add`: Allows users to create items containing information along with the password they want to save.
   - `update`: Enables users to update their existing items.
   - `secret`: Shows all information for a specific item on a dedicated page.
   - `delete`: Deletes a selected item from the database without a chance for recovery.
   - `account`: Displays the account information (username and password) on the "account" page.
   - `updateAccount`: Allows users to update their account information.
   - `deleteAccount`: Deletes the user account, along with all saved passwords.
   - `search`: Enables users to search for specific items by name or email.

5. **database.db**: This file contains the SQLite3 database where account information and encrypted passwords are stored. (Note: All passwords are encrypted, and only the user can decrypt and view them.)

The project also includes two folders:

1. **static**: This folder contains the JavaScript file, `index.js`, which includes functions for various site functionalities, such as password validation, password visibility toggling, item deletion confirmation, copying item information to the clipboard, and account deletion confirmation. It also includes the `style.css` file for website styling, as well as an `images` folder for storing website images.

2. **templates**: This folder contains all the HTML files, including a subfolder for user authentication-related templates.

## Roadmap

Below are the planned improvements for the website:

- Assign a dedicated URL for the site.
- Implement additional security measures.

## Running Locally

Please note that this project is for educational purposes and should not be used to store personal passwords used on other sites.

To run the project locally, follow these steps:

1. Clone the project repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git

2. Go to the project directory

   ```bash
     cd my-project
   ```

3. Install dependencies

   ```bash
     1) pip install Flask
     2) pip install cryptography
     3) pip install cs50
   ```

4. Start the server

   ```bash
     python3 -m flask run
   ```
