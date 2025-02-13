import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# List of emails
email_list = [
     "email1",
     "email2",
    # Add more emails
]

# Email settings
sender_email = "email"  # Your Gmail address
password = "pass"  # Your App Password

# Function to send email
def send_email(receiver_email, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "hiiii"

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Gmail SMTP server settings
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Login with email and app password
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Send email
        server.quit()  # Disconnect from the server
        print(f"Email sent to {receiver_email}.")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")

# Function to randomly select an email and send the message
def send_random_email(user_text):
    # Randomly choose an email from the list
    selected_email = random.choice(email_list)
    
    # Send email to the randomly selected email
    send_email(selected_email, user_text)

# Running the program
if __name__ == "__main__":
    # Get the email body from the user (manually entered)
    user_text = input("Please enter the email text: ")
    
    # Send the email randomly
    send_random_email(user_text)
