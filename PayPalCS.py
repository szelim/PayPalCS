import ezgmail
import re
import csv

# Collect data from PayPay cancellation notifications emails


def getpaypal():
    threads = ezgmail.search('subject:canceled automatic payments to you')
    i = 0
    while i < len(threads):
        n = 0
        messages = threads[i].messages
        while n < len(messages):
            # Get the data of the email
            source = 'PayPal'
            sender = [threads[i].messages[n].sender]
            timestamp = [str(threads[i].messages[n].timestamp)]
            # Find relevant data from the body of the email
            if re.search(r'Customer name:</th><td width="60%">.*</td></tr></table><table cellpadding="5" '
                         r'cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; '
                         r'font-weight:normal; border-bottom:0px;" width="40%">Customer email:', threads[i].messages[
                n].body) is None:
                customer_name = re.compile(r'Customer name: .*\s').search(threads[i].messages[n].body).group().strip()[15:]
                customer_email = re.compile(r'Customer email: .*\s').search(threads[i].messages[n].body).group().strip()[
                                 16:]
                profile_id = re.compile(r'Profile ID: .*\s').search(threads[i].messages[n].body).group().strip()[12:]
                profile_status = re.compile(r'Profile status: .*\s').search(threads[i].messages[n].body).group().strip()[
                                 16:]
                amount_paid_each_time = re.compile(r'Amount paid each time: .*\s').search(
                    threads[i].messages[n].body).group().strip()[23:-3]
                billing_cycle = re.compile(r'Billing cycle: .*\s').search(threads[i].messages[n].body).group().strip()[15:]
                last_payment_date = re.compile(r'Last payment date: .*\s').search(
                    threads[i].messages[n].body).group().strip()[
                                    19:]
                last_payment_amount = re.compile(r'Last payment amount: .*\s').search(
                    threads[i].messages[n].body).group().strip()[21:-3]
            else:
                customer_name = re.compile(r'Customer name:</th><td width="60%">.*</td></tr></table><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Customer email:').search(threads[i].messages[n].body).group().strip()[35:-192]
                customer_email = re.compile(r'Customer email:</th><td width="60%">.*</td></tr></table><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Profile ID:').search(threads[i].messages[n].body).group().strip()[36:-188]
                profile_id = re.compile(r'Profile ID:</th><td width="60%">.*</td></tr></table><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Profile status:').search(threads[i].messages[n].body).group().strip()[32:-192]
                profile_status = re.compile(r'Profile status:</th><td width="60%">.*</td></tr></table></td></tr></table><table cellpadding="0" cellspacing="0" style="font:1em Calibri, Trebuchet, Arial, sans serif, sans-serif; border:1px solid #eee;margin-top:10px;border-right:0;margin-bottom:10px;" width="100%"><tr><td><span   style="display:inline;"><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Amount paid each time:').search(threads[i].messages[n].body).group().strip()[36:-450]
                amount_paid_each_time = re.compile(r'Amount paid each time:</th><td width="60%">.*HUF</td></tr></table></span><span   style="display:inline;"><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Billing cycle:').search(
                    threads[i].messages[n].body).group().strip()[43:-234]
                billing_cycle = re.compile(r'Billing cycle:</th><td width="60%">.*</td></tr></table></span><span   style="display:inline;"><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Last payment date').search(threads[i].messages[n].body).group().strip()[35:-233]
                last_payment_date = re.compile(r'Last payment date:</th><td width="60%">.*</td></tr></table></span><span   style="display:inline;"><table cellpadding="5" cellspacing="0" width="100%"><tr><th style="background-color:#eee; text-align:left; font-weight:normal; border-bottom:0px;" width="40%">Last payment amount:').search(threads[i].messages[n].body).group().strip()[
                                    39:-236]
                last_payment_amount = re.compile(r'Last payment amount:</th><td width="60%">.*HUF</td></tr></table></span></td></tr></table><br/><!-- EmailClosingSalutation').search(
                    threads[i].messages[n].body).group().strip()[41:-79]

            # Compile all relevant data to a list of lists
            msg.append(
                [source] +
                sender +
                timestamp +
                [customer_name] +
                [customer_email] +
                [profile_id] +
                [profile_status] +
                [amount_paid_each_time] +
                [billing_cycle] +
                [last_payment_date] +
                [last_payment_amount])
            n += 1
        i += 1

# Collect data from PayPay cancellation notifications emails


def getadjuk():
    threads = ezgmail.search('subject:Rendszeres adományozás visszavonva (adjukössze.hu)')

    i = 0

    while i < len(threads):
        messages = threads[i].messages
        n = 0
        while n < len(messages):
            # Get the data of the email
            source = 'AdjukÖssze'
            sender = [threads[i].messages[n].sender]
            timestamp = [str(threads[i].messages[n].timestamp)]
            # Find relevant data from the body of the email
            customer_name = re.compile(r'támogatód (\(.*?\))').search(threads[i].messages[n].body).group().strip()[11:-1]
            customer_email = None
            profile_id = None
            profile_status = 'Canceled'
            amount_paid_each_time = re.compile(r'összeget \W.*\W').search(
                threads[i].messages[n].body).group().strip()[10:-5]
            billing_cycle = None
            last_payment_date = None
            last_payment_amount = None

            # Compile all relevant data to a list of lists
            msg.append(
                [source] +
                sender +
                timestamp +
                [customer_name] +
                [customer_email] +
                [profile_id] +
                [profile_status] +
                [amount_paid_each_time] +
                [billing_cycle] +
                [last_payment_date] +
                [last_payment_amount])
            n += 1
        i += 1

# Create headers for data structure


def createfile():
    header = [['source',
               'sender',
               'timestamp',
               'Customer_name',
               'Customer_email',
               'Profile_ID',
               'Profile_status',
               'Amount_paid_each_time',
               'Billing_cycle',
               'Last_payment_date',
               'Last_payment_amount']]

    # Create a csv file with the necessary data structure

    with open('CancelledContributions.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(header)

        # Copy the relevant data to the workbook

        writer = csv.writer(f, delimiter=',')
        writer.writerows(msg)

# Report on what has been done


def report():
    print('Number of emails downloaded: ' + str(len(msg)))


# Send attachment as email

def sendemail():
    # Add email address here.
    ezgmail.send('my@email.com', 'Canceled contributions', 'Please download the attached file to see canceled '
                                                           'contributions.', ['CancelledContributions.csv'])
    print("Email sent.")


if __name__ == "__main__":
    msg = []
    getpaypal()
    getadjuk()
    createfile()
    report()
    sendemail()