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
   - This file contains 3 functions that "help" the programmer in some things, the first function is that of login_required that does not allow users to enter certain parts of the site without logging in. 
As second and third function we have one to encrypt and decrypt messages that we pass through the parameter

3. __auth.py__
   - Also this file contains 3 functions that concern user authentication, as first functions there are that of login and registration that allows the user to register and log in the server, while for the third function we have the logout that allows the user to disconnect from their account without losing anything, obviously having the possibility to re-enter the account

4. __views.py__ 
   - This file contains many important functions of the site, specifically contains 9 functions.
The first function is called index that inside gets all the passwords that the user owns and shows them in the table on the main page of the site, as second we have that call Add that contains the process for the user to create other items containing the password of the site he wants, third function there is that called update that allows the user to update an already existing item, as the fourth function we have that called Secret which is the ability to see all the information you have put of that item, as the fifth functions we have delete which allows the possibility to delete any item, the sixth function is called Account, which allows the user to see his username and password information via a dedicated website page, while then we have as sestima and eighth function that to update your account and delete it losing each item in possession. 
As last function we have that called Search that allows the user ( through an input in the navbar ) to search for your item that you want specific without wasting time in searching among others.
  
5. __database.db__
   - This file contains the database ( created with Sqlite3 ) where every account information and passwords it has are kept. 
**( all passwords that are kept are encrypted and only you can see decrypted )**

## Roadmap

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
