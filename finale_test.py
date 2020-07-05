# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

import os, re


fromaddr = str(input("[!] Entre Your adress Email : "))
#toaddr= str(input("[!] Entre Other adress Email : "))
gmail_passwd = str(input("[!] Entre Your password : "))

filepath = 'email_1.txt'
with open(filepath) as fp:
   for cnt, toaddr in enumerate(fp):
       print("Line {}: Email :  {}".format(cnt, toaddr))


# instance of MIMEMultipart
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail 
#body = "Body_of_the_mail"
body = "This is an email Test From the Application Without the password and a the attache file "

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
#global file=' '
re_dir = r'[A-Z][:]([/\\]{1,2}[a-zA-Z]+)+([/\\]{1,2})?'
re_num = r'^0[5-9]([-. ][0-9]{2}){4}$'
fini = True
R = 'Saisir'
while fini :
   try:
       _dir = input("{} l'emplacement de votre fichier txt>>> ".format(R))
       if _dir != '':
           while re.search(re_dir,_dir) is None :
               if re.search(re_dir,_dir) is None and _dir !='':
                   print("[!] Regarder attentivement ce que vous saisissez.")
                   print(" Example : C://Users//admin//Desktop//")
                   fini = True
               try:
                   _dir = input("Now, {} encore l'emplacement de votre fichier>>> ".format(R))
               except KeyboardInterrupt:
                   print("\n   Interruption effectuée avec succé \n")
           try:
               os.chdir(_dir)    
           except FileNotFoundError:
               print("\n[!]Erreur ... Emplacement introuvable.")
               print("Rappel : Le répertoire de travail actuel est \"{}\"\n".format(os.getcwd()))
               R = 'Re-saisir'
               _dir = ''
           except OSError:
               print("\n[!]Erreur ... Emplacement incorrecte !\n Essayer avec // à la place de \\ ")

               print("Reminding : Rappel : Le répertoire de travail actuel est \"{}\"\n".format(os.getcwd()))
               R = 'Re-saisir'
               _dir = ''
           try:
               global file
               file = input ('Nommer votre fichier pdf  [!] ')
               print ('The File name : {} '.format(file))
               print ('[!] Done ')
               
               while file == '':
                   file = input("Nommer votre fichier txt>>> ")
                   print (file)
                   print ('[!] Done ')
##                    with open(file+'.txt','r') as f:
##                        Lines = f.readlines()
##                    f.close()
           except FileNotFoundError:
               print("\n[!]Erreur ... Fichier introuvable !")
               print("Rappel : Le répertoire de travail actuel est \"{}\"\n".format(os.getcwd()))
               R = 'Re-saisir'
               _dir = ''
       if _dir == '':
           fini = True
       else:
           fini = False
##           for num in Lines:
##               if re.search(re_num,num.strip()) is not None:
##                   print(num.strip())
   except KeyboardInterrupt:
       print("\n   Interruption effectuée avec succé \n")

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream')
#fileSource="{}".format(os.getcwd())
#print(_dir)
print(_dir+file)
attachment = open(_dir+file, "rb")
#attachment = open("C:\\Users\\admin\\Desktop\\r.pdf", "rb")
# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % file) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, gmail_passwd) 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 
