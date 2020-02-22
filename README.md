# PayPalCS
 Collects canceled PayPal and AjdukÖssze subscriptions from an email account.

## The problem:
PayPal and Hungarian charity payment provider AdjukÖsssze do not provide an option to export a list of canceled subscriptions.
However they send email notification about each cancellation. 

## The solution: 
This script 
1) logs in to a Gmail account, 
2) collects data from the email notifications, 
3) compiles them to a .csv file and 
4) sends the .csv file in email.

Most useful if set up as a recurring task.  

## How to:
1) The script uses ezgmail to collect data and to send the .csv file. For installation and quickstart guide follow: https://pypi.org/project/EZGmail/
2) Don't forget to specify what email address to send the .csv file to (line 148)