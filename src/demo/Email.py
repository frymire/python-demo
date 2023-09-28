'''
Created on May 17, 2014

@author: Mark.E.Frymire
'''


# NOTE: This doesn't work.  Need to figure out how to specify the password and such, but the tutorial didn't include it.

import smtplib

sender = "frymiretest@verizon.net"
receivers = ["mark.frymire@dac.us"]

message = """From: From Person <frymiretest@verizon.net>
To: To Person <mark.frymire@dac.us>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP("smtp.verizon.net", 465)
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
except smtplib.SMTPException:
    print "Error: unable to send email"
