from email.message import EmailMessage
import ssl
import smtplib


def send_email(sender_email, receiver_emails, subject, body, password):

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = r', '.join(receiver_emails)
    em['Subject'] = subject
    em.set_content(body)

    # Secure the connection
    context = ssl.create_default_context()

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_emails, em.as_string())