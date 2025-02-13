import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# لیست ایمیل‌ها
email_list = [
    "email1@example.com",
    "email2@example.com",
    "email3@example.com",
    # ایمیل‌های بیشتر
]

# تنظیمات ایمیل
sender_email = "your_email@gmail.com"  # ایمیل جیمیل خود را وارد کنید
password = "your_app_password"  # پسورد اپلیکیشن خود را وارد کنید

# تابع برای ارسال ایمیل
def send_email(receiver_email, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "پیام روزانه"

    msg.attach(MIMEText(body, 'plain'))

    try:
        # تنظیمات سرور SMTP جیمیل
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # شروع رمزگذاری TLS
        server.login(sender_email, password)  # ورود با ایمیل و پسورد اپلیکیشن
        server.sendmail(sender_email, receiver_email, msg.as_string())  # ارسال ایمیل
        server.quit()  # قطع اتصال از سرور
        print(f"ایمیل به {receiver_email} ارسال شد.")
    except Exception as e:
        print(f"خطا در ارسال ایمیل به {receiver_email}: {e}")

# تابع برای انتخاب یک ایمیل رندوم و ارسال متن
def send_random_email(user_text):
    # انتخاب یک ایمیل رندوم از لیست
    selected_email = random.choice(email_list)
    
    # ارسال ایمیل به ایمیل رندوم
    send_email(selected_email, user_text)

# اجرای برنامه
if __name__ == "__main__":
    # دریافت متن از کاربر (متن دستی که می‌خواهید ارسال کنید)
    user_text = input("لطفاً متن ایمیل را وارد کنید: ")
    
    # ارسال ایمیل به صورت رندوم
    send_random_email(user_text)
