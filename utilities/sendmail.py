import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_report_email(sender_addr, sender_pass, receiver_addr, email_subject, email_body, file_path):
    try:
        # Create a multipart message and set headers
        msg = MIMEMultipart()
        msg['From'] = sender_addr
        msg['To'] = receiver_addr
        msg['Subject'] = email_subject

        # Add body to email
        msg.attach(MIMEText(email_body, 'plain'))

        # Open the file to be sent
        with open(file_path, "rb") as attachment:
            # MIMEBase is a base class for all MIME-specific subtypes
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        # Encode the file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(file_path)}",
        )

        # Attach the file to the message
        msg.attach(part)

        # Log in to server using the sender's email and password
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_addr, sender_pass)
            # Send email
            server.sendmail(sender_addr, receiver_addr, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    # Set the email details
    sender_addr = "helplinerealestate1@gmail.com"
    sender_pass = "ayoj lsos zmoi iiru"
    receiver_addr = "annevivian01@gmail.com"
    email_subject = "Test Automation Report"
    email_body = "Please find the attached HTML report."

    # Use absolute path to the report file
    project_directory = os.path.dirname(os.path.abspath(__file__))  # Path to the directory containing this script
    file_path = os.path.join(project_directory, '..', 'report', 'report.html')
    # Resolve absolute path
    file_path = os.path.abspath(file_path)

    # file_path = "../report/report.html"

    # Invoke the send email method
    send_report_email(sender_addr, sender_pass, receiver_addr, email_subject, email_body, file_path)
