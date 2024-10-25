import os
import base64
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings

def send_email(subject, body, to_email, from_email=settings.DEFAULT_FROM_EMAIL, attachment=None, attachment_name=None):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'  # Securely use the API key from settings

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
        email.attachment = [sib_api_v3_sdk.SendSmtpEmailAttachment(
            name=attachment_name,
            content=base64.b64encode(attachment).decode('utf-8')
        )]

    try:
        api_response = api_instance.send_transac_email(email)
        print("Email sent successfully via API!")
    except ApiException as e:
        print(f"Exception when sending email via API: {e}")
