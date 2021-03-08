import smtplib 
import ssl
import os
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

pengirim_email = 'suryasilalahi00@gmail.com'
penerima_email = ['suryasilalahi00@gmail.com', 'surya.lahi23@gmail.com', 'muly4g0kil@gmail.com'] #tuple untuk menyimpan beberapa data email yang dituju
password = input('Password anda : ')

# f = open("receiver_list.txt", "a")
# f.write(penerima_email[])
# f.close()

email_body = '''
    Halo, nama saya Surya Silalahi. Asal kota Balige. Terimakasih.
'''


print('\n\nSedang Mengirim email...\n')

for penerima_email in zip(penerima_email):
    msg = MIMEText(email_body, 'plain') #Menambahkan body ke email
    msg['From'] = (pengirim_email)
    msg['To'] = ', '.join(penerima_email)
    msg['Subject'] = 'Perkenalan Diri'

    filename = "E:\Kuliah\Indonesia AI Mentorship Batch 4\Final Project\surya.jpeg"
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)

# files = ["surya.jpg"]    
# for image in files:
#     image_file = open(image, 'rb')
#     image_data = image_file.read()
#     image_type = imghdr.what(image_file.name)
#     image_name = image_file.name
#     msg.add_attachment(image_data, maintype = "image", subtype = image_type, filename = image_name)

    # with open("surya.jpeg", "rb") as f:
    #     file_data = f.read()
    #     file_type = imghdr.what(f.name)
    #     file_name = f.name
    
    # msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)
    
    # try:
    #     with open(filename, 'rb') as attachment:
    #         part = MIMEBase("application", "octet-stream")
    #         part.set_payload(attachment.read())   

    #     encoders.encode_base64(part)

    #     part.add_header('Content-Disposition', 'attachment', filename = {filename})
    #     msg.attach(part)
    
    # except Exception as e:
    #     print(f'Foto tidak ditemukan!\n{e}')

    try:
        # Creating a SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 465)
        # Mengenkripsi email
        context = ssl.create_default_context()
        server.starttls(context=context)
        # We login into our Gmail account
        server.login(pengirim_email, password)
        # Send the email
        server.sendmail(pengirim_email, penerima_email, msg.as_string())
        print('Email terkirim!\n')

    except Exception as e:
        print(f'----Salah password----\n{e}')

    finally:
        print('Tutup server.\n')
        server.quit()