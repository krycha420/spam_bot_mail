import smtplib
toaddres = 'pbilewicz00@gmail.com'
fromaddres = 'bernaikkardasz@gmail.com'
message = 'pisz odwolanie'
with smtplib.SMTP('smtp.gmail.com','587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('bernaikkardasz@gmail.com', 'kwlwbpvrfncsbeae')
    for i in range (1000):
        smtpserver.sendmail(fromaddres, toaddres, message)
        print(i)
