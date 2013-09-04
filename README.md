## hazinSES

![hazinses](http://ucuncuadam.files.wordpress.com/2012/02/sami-hazinses-2.jpg?w=500&h=389 "hazinses")

#####ABOUT

Hazinses is a django app, that helps you to send asynchronous email via celery through Amazon-SES. The biggest problem
is complaint and bounce emails that come as feedback from amazon services. Those emails cause you to be reported as Hard Bounce in case you keep sending emails
and prevent forever you to send email to that user again.


#####INSTRUCTIONS

1) install hazinses app

    pip install hazinses
    
make sure that you installed hazinses requirements
    
    ['boto', 'djcelery']
    
2) Add hazinses into your INSTALLED_APPS 


    INSTALLED_APPS += ('hazinses')


3) Add hazinses to your urls.py

    url(r'^hazinses/', include('hazinses.urls')),
    
4) Set following settings to your settings.py

    AMAZON_REGION = '<YOUR AMAZON REGION>'
    AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY_ID>'
    AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
    BOUNCE_TIMEDELTA = <DAYS FOR NOT SENDING EMAIL AFTER BOUNCE NOTIFICTAION>
    COMPLAINT_TIMEDELTA = <DAYS FOR NOT SENDING EMAIL AFTER COMPLAINT NOTIFICATION>

4) Sync your Database
    
    python manage.py syncdb
    
    
5) RUN CELERY...

    python manage.py celeryd
    
6) Use send_email as following in your code. This will make you send async email through your AWS SES account. In case, you receiver
any bounce or complaint notifications, it will prevent you to send email again to that user again.

    from hazinses.tasks import send_email
    
    send_email.delay(subject, body,from_email,
                     to_email, mail_save_subject)
                     
                     
###### THANKS

thanks to serdarakarca
