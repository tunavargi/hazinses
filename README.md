## Hazinses

#####ABOUT

Hazinses is a django app, that helps you to send asynchronous email via celery through Amazon-SES. The biggest problem
is complaint and bounce emails that come as feedback from amazon services. Those emails cause you to reported as Hard Bounce and
prevent you to send email again.

![hazinses](http://ucuncuadam.files.wordpress.com/2012/02/sami-hazinses-2.jpg?w=500&h=389 "hazinses")

#####INSTRUCTIONS

Add hazinses into your INSTALLED_APPS 


    INSTALLED_APPS += ('hazinses')
