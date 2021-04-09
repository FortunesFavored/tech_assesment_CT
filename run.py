from app import App, db
from app.models import divvyData

if __name__ == "main":
    App.run(host='127.0.0.1', port=5001)


@App.shell_context_processor
def make_shell_context():
    return {'db':db, 'divvyData':divvyData}