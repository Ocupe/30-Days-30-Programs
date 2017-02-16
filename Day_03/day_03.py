#
# Todays program sets up a very simple db with pony orm.
#

from pony.orm import *
from elizabeth import Personal, Numbers
from elizabeth import Food as _Food

db = Database()


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)
    foods = Set('Food')


class Food(db.Entity):
    id = PrimaryKey(int, auto=True)
    type = Required(str)
    price = Required(float)
    persons = Set(Person)


db.bind('sqlite', ':memory:', create_db=True)
db.generate_mapping(create_tables=True)


# sql_debug(True)


@db_session
def create_dummy_data():
    _f = _Food()
    _n = Numbers()
    _p = Personal()
    for _ in range(100):
        Person(name=_p.full_name(), age=_p.age(), foods=Food(type=_f.fruit(), price=_n.between(0, 100)))
    commit()


@db_session
def select_cheap_fruits():
    select(f for f in Food if f.price < 10).show()


if __name__ == '__main__':
    create_dummy_data()
    select_cheap_fruits()
