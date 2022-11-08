import time

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

# app = Celery("tasks", broker="redis://localhost")


@shared_task
def send_email(to, content=""):
    # sender = settings.EMAIL_SENDER
    # subject = "CY{} Inventory Stocktaking_Counting Start".format("2020")
    # content = (
    #     "<p>All the inventory related data has been uploaded to the Stocktaking System.<br>You can start "
    #     "counting now.</p> "
    # )
    # content += "<p>The link to the System as below:<br><a>http://127.0.0.1/stock_checking/</a></p>"
    # content += "<p>Best Regards,<br>Controlling</p>"
    #
    # msg = EmailMultiAlternatives(subject, content, sender, [to])
    # msg.attach_alternative(content, "text/html")
    # msg.send()

    print("send email task")

    return True
