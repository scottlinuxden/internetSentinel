import smtplib


class EmailClient:

    def __init__(self, smtp_server, smtp_port, gmail_login_username, gmail_login_password):
        self.gmail_login_username = gmail_login_username
        self.gmail_login_password = gmail_login_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, content):
        # Create Headers
        headers = ["From: " + self.gmail_login_username, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        # Connect to Gmail Server
        session = smtplib.SMTP(self.smtp_server, self.smtp_port)
        session.ehlo()
        session.starttls()
        session.ehlo()

        # Login to Gmail
        session.login(self.gmail_login_username, self.gmail_login_password)

        # Send Email & Exit
        session.sendmail(self.gmail_login_username, recipient, headers + "\r\n\r\n" + content)
        session.quit()


if __name__ == '__main__':
    sender = EmailClient('smtp.server', 'smtp.port', 'gmail_email@gmail.com', 'password')

    sendTo = 'anotheremail@email.com'
    emailSubject = "Hello World"
    emailContent = "This is a test of my Emailer Class"

    # Sends an email to the "sendTo" address with the specified "emailSubject" as
    # the subject and "emailContent" as the email content.
    sender.send_email(sendTo, emailSubject, emailContent)
