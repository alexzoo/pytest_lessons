from sqlalchemy import desc

from database import tables


def test_get_film_by_id(get_db_session):
    result = get_db_session.query(tables.Films.film_id, tables.Films.title). \
        filter(tables.Films.film_id == 180).one_or_none()
    if result:
        print('All ok')
    else:
        print('None')


def test_get_with_sub_query(get_db_session):
    data = get_db_session
    # subquery to get sql query like SELECT ... WHERE ...
    film_ids = data.query(tables.Films.film_id).filter(tables.Films.film_id > 180).subquery()

    result = data.query(tables.Films.title).filter(tables.Films.film_id.in_(film_ids))\
        .order_by(desc(tables.Films.film_id)).all()
    print(result)


def test_delete_data(get_db_session, get_delete_method):
    get_delete_method(get_db_session, tables.Films.film_id, (tables.Films.film_id == 100))


def test_add_data(get_db_session, get_add_method, get_film_generator):
    item = tables.Films(**get_film_generator.build())
    get_add_method(get_db_session, item)

