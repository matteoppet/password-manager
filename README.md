# Axiom

A web-based password manager written in Flask.

Axiom is a password manager that allows you to save every password you want easily and safely. 
Every password saved on the site is encrypted and only you can see it.

- This site is a project for the Final Project of the __CS50x Course__.

## Demo

Video demo with all the explanations:

## Explanation
Explanation of each file:
1. __app.py__
   - This file contains all the setup that Flask will have to start when the server is started, By setting a Secret Key, the settings for the session, database access and the "registration" of two files containing other parts of the site.

2. __helper.py__
   - This file contains 3 functions that "help" me in some things: 

      - ```login_required``` -> This function does not allow the user to enter certain specified pages without logging in.
      
      - ```encryption``` -> This function allows you to encrypt any message you pass through the parameter using the [Cryptography](https://pypi.org/project/cryptography/) library.
      
      - ```decryption``` -> This function has the same procedure as the Encryption function, but this instead of encrypting, decrypts the message.

3. __auth.py__
   - Also this file contains 3 functions that concern user authentication:

      - ```login``` -> This function allows access through your credentials to the site where you keep saved passwords.

      - ```register``` -> This function that allows the creation of your account by entering a username and a password.

      - ```logout``` -> This fuction allows you to disconnect from your account without deleting it __(by default the disconnection from your account takes place every 24 hours)__ and to regain access to your passwords you will need to login first.

4. __views.py__ 
   - This file contains many important functions of the site, specifically contains 9 functions:

      - ```index``` -> this function allows you to see all your saved passwords (in a table on the main page) by connecting to the database.
      
      - ```add``` -> This function allows you to create items containing all the information you will put together with the password you want to save.

      - ```update``` -> This is a function that allows you to update your item that you already have.

      - ```secret``` -> This function shows you, in a dedicated page, all the information of your item.

      - ```delete``` -> This function deletes the item you want from the database without having a chance to retrieve it.

      - ```account``` -> This function refers to the page named "account" and allows you to see your account information (username and password)

      - ```updateAccount``` -> This is a function very similar to the one called "update" that instead of updating the item, you can update your account information

      - ```deleteAccount``` -> This function is also very similar to the one called "delete", but this allows you to delete the account losing all the passwords you have saved.

      - ```search``` -> This function allows you to search for items you own without wasting time searching for a specific item among others, in the search there is only 1 parameter, you can search by name or by email.
  
5. __database.db__
   - This file contains the database ( created with Sqlite3 ) where every account information and passwords it has are kept. 
**( all passwords that are kept are encrypted and only you can see decrypted )**

Now we have two (three with flask_session that is created automatically when you access the site starting it locally) folders:

1. __static__
      
      - __index.js__
         - ```passwordCheck``` -> This function checks if the password and password confirmation on the registration page are longer than 7 characters.
         
         - ```confirmCheck``` -> This function checks if the password and password confirmation are the same, always on the registration page.

         - ```deleteItem``` -> This function, when you delete an item, makes you appear a request for confirmation for deletion and if the confirmation is confirmed, sends the id of the item you have to the function in the ```views.py``` file.

         - ```copyToClipboard``` -> This function allows you to copy the information you have in an item, through a special button.

         - ```deleteAccount``` -> This is a function exactly the same as the function above DeleteItem, but it sends the id of your account to the function located in the file ```views.py``` to delete your account.


      - __style.css__ -> This file is used for formatting the website layout making it more cool.


      - __images__ -> This folder is used for keep the images used on the website.

2. __templates__ 
     - This folder is used to store all the HTML files, inside there is also another folder that inside it there are 2 HTML files regarding user authentications.

## Roadmap

Below, I will list all the changes I want to make to the website.

- A URL for the site

- More security on site

- Dark and Light themes

- Improve the design of the site

## Run Locally

> __Do not__ put any personal password that you currently use on any site. This site is a test and it’s one of my first projects I have done.

Clone the project

```bash
  git clone https://(link-to-project)
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  1) pip install Flask
  2) pip install cryptography
  3) pip install cs50
```

Start the server

```bash
  python3 -m flask run
```
