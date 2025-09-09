import emails
import os
from dotenv import load_dotenv

load_dotenv()

def send_verification_email(email: str, user_id: int):
    """Send verification email to user"""
    try:
        # Email configuration from environment variables
        smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER")
        smtp_password = os.getenv("SMTP_PASSWORD")
        
        if not all([smtp_user, smtp_password]):
            print("SMTP credentials not configured. Skipping email send.")
            return
        
        # Create verification link
        base_url = os.getenv("BASE_URL", "http://localhost:8000")
        verification_url = f"{base_url}/verify/{user_id}"
        
        # Email content
        subject = "Verify Your Email - Customer Database App"
        html_content = f"""
        <html>
        <body>
            <h2>Welcome to Customer Database App!</h2>
            <p>Please click the link below to verify your email address:</p>
            <p><a href="{verification_url}">Verify Email</a></p>
            <p>If the link doesn't work, copy and paste this URL into your browser:</p>
            <p>{verification_url}</p>
            <p>Best regards,<br>Customer Database Team</p>
        </body>
        </html>
        """
        
        # Send email
        message = emails.Message(
            subject=subject,
            html=html_content,
            mail_from=(smtp_user, "Customer Database App")
        )
        
        response = message.send(
            to=email,
            smtp={
                "host": smtp_host,
                "port": smtp_port,
                "user": smtp_user,
                "password": smtp_password,
                "tls": True,
            }
        )
        
        if response.status_code == 250:
            print(f"Verification email sent to {email}")
        else:
            print(f"Failed to send email to {email}: {response.status_code}")
            
    except Exception as e:
        print(f"Error sending email: {e}")
        # Don't fail the registration if email fails
        pass

