from flask_mail import Message, Mail
mail = Mail()


# def sendEmail(messageBody,messageHtml, recipient):
#     msg = Message(messageBody, sender='se.biruk.kassaw@gmail.com', recipients=[recipient])

#     msg.body = 'Your link is {}'.format(messageBody)
#     msg.html = messageHtml
#     mail.send(msg)
