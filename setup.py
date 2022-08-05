from setuptools import setup, find_packages
from distutils.cmd import Command
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy_utils.functions import database_exists, create_database

from tsp.poc.mysql.models import Base, Data

MYSQL_CONNECTION_STRING = "mysql://root:rootpassword@0.0.0.0:3306/tsp"
POSTGRES_CONNECTION_STRING = "postgresql://postgres:password@phoenix:5432/tsp"

DATABASE_STRING = POSTGRES_CONNECTION_STRING


class InitCommand(Command):
    """A custom command to run Pylint on all Python source files."""

    description = 'Initialize database'
    user_options = [
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run command."""
        engine = create_engine(DATABASE_STRING, echo=True, future=True)
        with Session(engine) as session:
            if not database_exists(engine.url):  # Checks for the first time
                create_database(engine.url)  # Create new DB
                Base.metadata.create_all(engine)
                print("Database 'tsp' created")
            else:
                print("Database Already Exists")

            # Trigger to backup a new row insert
"""
            insert_trigger = '''
DELIMITER $$

CREATE TRIGGER `create_partition` BEFORE INSERT ON `tsp_tokens`
FOR EACH ROW
BEGIN
ALTER table tsp_tokens PARTITION BY hash (YEAR(date)+MONTH(date)) partitions 12;

END$$

DELIMITER ;
'''
            try:
                session.execute(insert_trigger)
            except:
                import traceback
                print(traceback.format_exc())

            partition_sql = ''' 
ALTER table tsp_tokens PARTITION BY hash (YEAR(date)+MONTH(date)) partitions 12
            '''

            try:
                session.execute(partition_sql)
            except:
                import traceback
                print(traceback.format_exc())
"""



class DropCommand(Command):
    """Drop test database."""

    description = 'Drop database'
    user_options = [
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run command."""

        engine = create_engine(DATABASE_STRING, echo=True, future=True)
        with Session(engine) as session:
            if not database_exists(engine.url):  # Checks for the first time
                print("Database 'tsp' does not exist")
            else:
                if DATABASE_STRING == MYSQL_CONNECTION_STRING:
                    session.execute("drop database tsp")
                else:
                    Base.metadata.drop_all(engine)
                session.commit()

        print("Database dropped.")


class PopulateCommand(Command):
    """Populate database with data."""

    description = 'Populate database'
    user_options = [
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run command."""

        engine = create_engine(DATABASE_STRING, echo=True, future=True)
        with Session(engine) as session:
            if not database_exists(engine.url):  # Checks for the first time
                print("Database 'tsp' does not exist")
            else:
                for i in range(0,100):
                    data = Data(key="somekey"+str(i), value="somevalue"+str(i))
                    session.add(data)
                session.commit()

        print(f"{i} rows added.")

setup(
    name='mysql-clean-poc',
    version='0.1.0',
    packages=find_packages(include=['tsp', 'tsp.*']),
    cmdclass={
        'init': InitCommand,
        'populate': PopulateCommand,
        'drop': DropCommand
    }
)
