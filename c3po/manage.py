"""
Entrypoint of the application.

Manager is set up and the blueprint for the
application is created.
"""

import os
from logging import getLogger

from flask import current_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from c3po.api import blueprint
from c3po.api.create_app import create_app, db
from c3po.logging_config import setup_logger

setup_logger()
LOG = getLogger(__name__)

app = create_app(os.getenv('FLASK_ENV') or 'dev')

app.register_blueprint(blueprint)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    """Run the flask app."""
    LOG.info('initiating app...')
    app.run(host=current_app.config['HOST'],
            port=current_app.config['PORT'], debug=current_app.config['DEBUG'])


if __name__ == '__main__':
    manager.run()
