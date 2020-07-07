# Send mail
print("Sending mail...")
import smtplib
s=smtplib.SMTP('smtp.gmail.com',58)8
s.starttls()
s.login("krishana250799@gmail.com","cjibeegczuzmsxyh")
message1="success"
s.sendmail("krishana250799@gmail.com","krishana250799@gmail.com",message1)
s.quit()
print("Mail send..")
