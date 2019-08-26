"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

from six.moves import xrange

from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


metadata = MetaData()

Person = Table('person', metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String(250), nullable=False))

Address = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('street_name', String(250)),
                Column('street_number', String(250)),
                Column('post_code', String(250), nullable=False),
                Column('person_id', Integer, ForeignKey('person.id')))

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite://')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
metadata.create_all(engine)


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# add 'npeople' people to the database
def run_sqlalchemy(loops, npeople):

    for loops in xrange(loops):
        # drop rows created by the previous benchmark
        cur = Person.delete()
        cur.execute()

        cur = Address.delete()
        cur.execute()

        for i in xrange(npeople):
            # Insert a Person in the person table
            new_person = Person.insert()
            new_person.execute(name="name %i" % i)

            # Insert an Address in the address table
            new_address = Address.insert()
            new_address.execute(post_code='%05i' % i)

        # do 'npeople' queries per insert
        for i in xrange(npeople):
            cur = Person.select()
            cur.execute()


if __name__ == "__main__":
    run_sqlalchemy(10, 100)
