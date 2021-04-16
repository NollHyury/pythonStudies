import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os
import pathlib

def sendMail(content,template,mailProps):
    path = pathlib.Path().absolute()
    env = Environment(
        loader=FileSystemLoader(searchpath=os.path.join(path, "src/", "templates"))
    )
    template = env.get_template(template)
    output = template.render(data=content)
    mailSend(output,mailProps)    
    return "Mail sent successfully."


def mailSend(bodyContent,mailProps):
    rec_list =  mailProps.recList
    rec =  ', '.join(rec_list)
    to_email = rec
    from_email = 'noreply@wmo_national_market_support_sales.weg.net'
    subject = mailProps.subject
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(bodyContent, "html"))
    msgBody = message.as_string()

    server = smtplib.SMTP(host='mail.weg.net', port=25)

    server.sendmail(
        from_email,rec_list,msgBody
        )
    server.quit()
