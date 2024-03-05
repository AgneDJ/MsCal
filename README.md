# MsCal

MsCal
A Calendar Web app for adding information about periods, meds etc.

Features
Adding events to a calendar
Tracking periods
Adding medications
Counting days left
Adding symptoms

Requirements
Python 3
PostgeSQL

How to use
Expose environment variables:

Install the project:

$ git clone https://github.com/AgneDJ/StepOdyssey.git
$ virtualenv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
(env) $ createdb calendar_data
$ python3 model.py
To run the server:

$ python3 server.py
open localhost: https://127.0.0.1:4000/
