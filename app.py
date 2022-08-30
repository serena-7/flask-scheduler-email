import atexit
import os
from flask import Flask
from extensions import scheduler, mail


app = Flask(__name__)
app.config.from_object('config')

mail.init_app(app)
scheduler.init_app(app)
# this if ensures that when in debug mode the tasks don't get scheduled twice
if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    import tasks  # NOQA:F401
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


@app.route("/")
def home():
    return "Homepage Running!"


if __name__ == "__main__":
    app.run()
