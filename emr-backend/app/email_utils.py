from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

email_config = {
    'MAIL_USERNAME': 'your-email@example.com',
    'MAIL_PASSWORD': 'your-email-password',
    'MAIL_FROM': 'your-email@example.com',
    'MAIL_PORT': 587,
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_STARTTLS': True, 
    'MAIL_SSL_TLS': False, 
    'USE_CREDENTIALS': True, 
    'VALIDATE_CERTS': True,
}

conf = ConnectionConfig(
    MAIL_USERNAME=email_config['MAIL_USERNAME'],
    MAIL_PASSWORD=email_config['MAIL_PASSWORD'],
    MAIL_FROM=email_config['MAIL_FROM'],
    MAIL_PORT=email_config['MAIL_PORT'],
    MAIL_SERVER=email_config['MAIL_SERVER'],
    MAIL_STARTTLS=email_config['MAIL_STARTTLS'],
    MAIL_SSL_TLS=email_config['MAIL_SSL_TLS'],
    USE_CREDENTIALS=email_config['USE_CREDENTIALS'],
    VALIDATE_CERTS=email_config['VALIDATE_CERTS']
)



async def send_email(to_email: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[to_email],
        body=body,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
