# Send mail
print("Sending mail...")
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("mundrak21@gmail.com","mjipeehczuzmsxyh")
message1="success"
s.sendmail("mundrak21@gmail.com","mundrak21@gmail.com",message1)
s.quit()
print("Mail send..")
