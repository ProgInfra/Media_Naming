# Media Naming : Account Naming

![Icon](../icon.png)

## Table Of Contents

- [Media Naming : Account Naming](#media-naming--account-naming)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Basic Fields](#basic-fields)
  - [Store Password](#store-password)
  - [Basic Account](#basic-account)
  - [Development Account](#development-account)

## Description

When you wan to go on **internet**, you need some basic account in some web services to start to exist on internet. Setup some **account** is normal and to access a lot of **web services** you need to create a new account on this web service. But before create other account, you need some **basic account** that everyone need some to do or create something on internet.

In this documentation, we will see these account we need first and who to **manage them**.

## Basic Fields

First for each account you will create, you need some **basic fields** to define your account. Before setup your basic account, you need to search to create these basic fields.

There are two type of basic fields :

- **Real Basic Fields** : There are fields based on your real identity on this earth, your real name, your real age, ...
- **Virtual Basic Fields** : There are fields based on your imagination, you have to create one to be anonyms on internet and this is a must.

For each of these type of basic fields, you have the same fields to create and store securely, you have just to create these fields twice, one for your real identity on internet, you must protect these and another for your virtual identity on internet, you must protect these but there are virtual, so don't panic.

Here a list of some basic fields with example for real or virtual type :

- **Pseudo** :
  - Real : Gilbert45
  - Virtual : TheSwordMan
- **First Name** :
  - Real : Gilbert
  - Virtual : TheSwordMan
- **Last Name** :
  - Real : Gast
  - Virtual : Sword
- **Email** :
  - Real : gilbert.gast@gmail.com
  - Virtual : theswordman@gmail.com
- **Password** : For password it's a little complicated, you can generate one with **KeePass** (see later) or create one with your imagination but don't create a simple password, you need to setup a big and difficult password. You don't have to keep in your memory this password because we will save it in a safe place.

## Store Password

Next you have to store your **password** and there are difficult password, so remember all of these is impossible. For this we use two **technologies** :

- **Password Manager** : There are software to store every **password** you want with account, you can also **generate** some password if you want. All you need to remember is your **master pass**, a big password to access to all your password **securely** (a complete **phrase** for example).
  - [**KeePass**](https://keepass.info/) ([KeePassXC](https://keepassxc.org/) for better UI) : This is a **free** and **open source** software that you have to download and install on your computer or phone.
  - [**BitWarden**](https://bitwarden.com/) : Complete **web service** available **online** for **computer** or **phone** (**self hosted** available but on big server).
  - [**VaultWarden**](https://github.com/dani-garcia/vaultwarden) : Full implementation of **BitWarden API** but **smaller** and **self hosted**.
- **Backup** :
  - **Cloud Drive (Google Drive)** : With your Google account you have access to Google Drive services with 15 Go of storage available, with this you can store you encrypted password file (contains all your password and unlocked by your master pass) in this drive on the cloud. Thanks to this you can synchronise it with your local file on your PC and all your account with password are saved everywhere and you can access to it everywhere.
  - Any other **backup** system (other cloud provider, CD, USB Key, ...)

With these **technologies**, you can't lost your password and account, all of these are securely created and stored in everywhere.

## Basic Account

Now, for your first step on internet, you need some basic account to create another account and manage these :

- **Google** : The first is the Google account, with it you can access a lot of web services :
  - **Drive** : For your password file, backup or other files
  - **Gmail** : For your main email box
- **Microsoft** : The second is the Microsoft account, with it you can access a lot of web services :
  - **OneDrive** : Alternative drive for emergency.
  - **Outlook** : Second email box for emergency and second protection for many other account.

You can use software for synchronise drive contents and **Thunderbird** for manage email.

With these basic account you can create a lot of new account on internet securely, today, you need to add phone number for better security and **2 Factor Authenticate**.

## Development Account

For development you need a lot of account for a lot of web services :

- **Git** : You need a place to store your code, so a git repository provider is the solution, choice one of these or create an account for each :
  - **GitHub**
  - **GitLab**
- **Docker Hub** : This is only if you need to publish some docker images
