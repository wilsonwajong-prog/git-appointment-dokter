from app import db 
from flask_migrate import Migrate
from app import create_app
from app.model import Patient, Appointment, Doctor
application = create_app()
migrate = Migrate(application, db)


@application.shell_context_processor
def make_shell_context():
    return dict(db=db, Patient=Patient, Appointment=Appointment, Doctor=Doctor)


if __name__=='__main__':
    application.run(debug=True)
