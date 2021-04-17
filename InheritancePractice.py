class Contact(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email

class MailSender():
    def sendEmail(message):
        print("The message is: [" + message + "] to " + self.email)

class EmailableContact(Contact, MailSender):
    pass

contact = EmailableContact("Andrei", "andrei_mungiu@yahoo.com")

contact.sendEmail("HelloWorld!")