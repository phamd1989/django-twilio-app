from django.http import HttpResponse
from django.template import Template, Context
from django_twilio.client import twilio_client
# from django.views.decorators.csrf import csrf_protect
# from django.core.context_processors import csrf
import models

MY_TWILIO_NUMBER = '+15029473430'


def home(request):
    return HttpResponse("Hello from django, try out <a href='/admin/'>/admin/</a>\n")


def main(request):
    """main page to send text updates to all subscribed numbers
    
    Pull all subscribed numbers from database and send a text update to those numbers.
    """
    
    # TODO: figure out how to use /templates. Currently stuck with TEMPLATES_DIR being
    # empty when deploying to AWS Beanstalk
    raw_template = """
    <html>
    <head>
    	<title>Main page</title>
    </head>
    <body>
	{% if error %}
	    <p style="color: red;"> please share your update  </p>
    {% endif %}
	<form action="" method="get">
            <input type="text" name="share">
            <input type="submit" value="Submit">
    	</form>
    </body>
    </html>
    """
    
    error = False
    if 'share' in request.GET:
        share = request.GET['share']
	if not share:
	    error = True
	else:
        # get all numbers that are subscribed
	    sub_instances = models.Subscrption.objects.filter(is_subscribed=True)
	    # send a text to each number with a status update.
        for instance in sub_instances:
	  		twilio_client.messages.create(
           	    body=share,
            	to=instance.phone_number,
                from_=MY_TWILIO_NUMBER,
        	)
    t = Template(raw_template)
    html = t.render(Context({'error': error}))
    return HttpResponse(html)


def sms(request):
    """ This method pulls attributes from a GET request from Twilio API
    
    Then update databases accordingly. Create new instance for Status table
    and create new instance or update an existing entry in Subscription table
    """
    msid = request.GET.get('MessageSid', '2')
    accsid = request.GET.get('AccountSid', '1')
    from_number = request.GET.get('From', '1')
    to_number = request.GET.get('To', '1')
    body = request.GET.get('Body', '1')
    
    # create new entry on Status table
    status_instance = models.Status(msid=msid, from_number=from_number,
                                    accsid=accsid, to_number=to_number, message=body)
    status_instance.save()
    
    # determine if this number is already in the Subscrption table
    try:
	    sub_instance = models.Subscrption.objects.get(phone_number=from_number)
    except models.Subscrption.DoesNotExist:
        sub_instance = models.Subscrption(phone_number = from_number)
    
    # Then change the subscribed field accordingly to the text message
    if body == 'dunca_subscribed':
  	    sub_instance.is_subscribed = True
    elif body == 'dunca_unsubscribed':
	    sub_instance.is_subscribed = False
    sub_instance.save()
    
    return HttpResponse('<p>Thank you for your text!</p>')

