import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.conf import settings  # For accessing Django settings

# def send_email(subject, body, to_email, from_email=settings.DEFAULT_FROM_EMAIL, attachment=None, attachment_name=None):
#     # Brevo SMTP server configuration
#     smtp_server = 'smtp-relay.brevo.com'
#     smtp_port = 587  # Use 465 for SSL
#     smtp_username = settings.BREVO_SMTP_USERNAME
#     smtp_password = settings.BREVO_SMTP_PASSWORD

#     # Create a MIME object
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     # Attach the body to the MIME object
#     msg.attach(MIMEText(body, 'html'))

#     # Attach the PDF if provided
#     if attachment and attachment_name:
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment)
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition', f'attachment; filename={attachment_name}')
#         msg.attach(part)

#     # Connect to the SMTP server
#     try:
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
#             server.login(smtp_username, smtp_password)
#             server.send_message(msg)
#             print("Email sent successfully!")
#     except Exception as e:
#         print(f"Error: {e}")
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

def send_email(subject, body, to_email, from_email=settings.DEFAULT_FROM_EMAIL, attachment=None, attachment_name=None):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = ""

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    sender = {"email": from_email}
    to = [{"email": to_email}]
    email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=body
    )

    if attachment and attachment_name:
        import base64
        email.attachment = [sib_api_v3_sdk.SendSmtpEmailAttachment(
            name=attachment_name,
            content=base64.b64encode(attachment).decode('utf-8')
        )]

    try:
        api_response = api_instance.send_transac_email(email)
        print("Email sent successfully via API!",api_response)
    except ApiException as e:
        print(f"Exception when sending email via API: {e}")
