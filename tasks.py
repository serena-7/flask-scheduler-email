from extensions import scheduler, mail
from flask_mail import Message


@scheduler.task(
    "interval",
    id="hello",
    seconds=3,
    max_instances=1
)
def say_hello():
    print("Hello I'm still running")


@scheduler.task(
    "interval",
    id="affirmation",
    seconds=7,
    max_instances=1
)
def affirmation():
    print("You're beautiful by the way :)")


@scheduler.task(
    "cron",
    id="cronTask",
    day_of_week="mon",
    hour=14,
    minute=59
)
def at_time():
    print("This was scheduled for day and time")


@scheduler.task(
    "cron",
    id="email-cron",
    day_of_week="mon",
    hour=16,
    minute=37
)
def send_email():
    with scheduler.app.app_context():
        msg = Message('TEST', recipients=['serena7testing+test@gmail.com'])
        msg.body = "This is a test of sending email from Flask!!"
        mail.send(msg)
    print("Message Sent!")
