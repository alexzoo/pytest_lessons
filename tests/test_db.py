from sqlalchemy import desc

from database.db import session

from database import tables


def test_get_film_by_id():

    result = session.query(tables.Films.film_id, tables.Films.title). \
        filter(tables.Films.film_id == 180).one_or_none()
    if result:
        print('All ok')
    else:
        print('None')


def test_get_with_sub_query():
    # subquery to get sql query like SELECT ... WHERE ...
    film_ids = session.query(tables.Films.film_id).filter(tables.Films.film_id > 180).subquery()

    result = session.query(tables.Films.title).filter(tables.Films.film_id.in_(film_ids))\
        .order_by(desc(tables.Films.film_id)).all()
    print(result)
