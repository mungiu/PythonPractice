class Contact(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class MailSender:
    def send_email(self, message):
        print("The message is: [" + message + "] to " + self.email)


class MailableContact(Contact, MailSender):
    pass


contact = MailableContact("Andrei", "andrei_mungiu@yahoo.com")

contact.send_email("HelloWorld!")
