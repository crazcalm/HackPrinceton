import secret, sendgrid


def main(body):
    
    # make a secure connection to SendGrid
    s = sendgrid.Sendgrid(secret.user_name, secret.user_password, secure=True)

    # make a message object
    message = sendgrid.Message("crazcalm@gail.com", "Friends_first_app", "This doesn't show...",
    body)
    # add a recipient
    message.add_to("crazcalm@gmail.com", "Marcus Willock")

    # use the Web API to send your message
    s.web.send(message)
    
    print "\n email sent!"
    
if __name__ == "__main__":
    main()
    
    