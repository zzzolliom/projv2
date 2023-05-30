from new import *
from sqlalchemy import create_engine, inspect, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# Создаем соединение с базой данных
engine = create_engine('sqlite:///my.db')
# Создаем таблицы в базе данных
Base.metadata.create_all(engine)
# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

metadata = Base.metadata


def add_user(f_name, l_name, nickname, birthday, now_place, phone, e_mail):
    new_entry = User(f_name=f_name,
                     l_name=l_name,
                     nickname=nickname,
                     birthday=birthday,
                     now_place=now_place,
                     phone=phone,
                     e_mail=e_mail)
    session.add(new_entry)
    session.commit()


def add_event(name, description, art_form_id, genre_id, date_time, dt_start, dt_over, cost_min, cost_max, currency,
              organizer_id, place_id, link, photo):
    event = Event(name=name,
                  description=description,
                  art_form=art_form_id,
                  genre=genre_id,
                  date_time=date_time,
                  dt_start=dt_start,
                  dt_over=dt_over,
                  cost_min=cost_min,
                  cost_max=cost_max,
                  currency=currency,
                  organizer=organizer_id,
                  place=place_id,
                  link=link,
                  photo=photo)
    session.add(event)
    session.commit()


def add_organizer(name, description):
    organizer = Organizer(name=name,
                          description=description)
    session.add(organizer)
    session.commit()


def add_place(name, description, country, city, district, street, num_building, liter_building, level, mono_address, phone):
    existing_place = session.query(Place).filter_by(name=name, mono_address=mono_address).first()
    if not existing_place :
        place = Place(name=name,
                    description=description,
                    country=country,
                    city=city,
                    district=district,
                    street=street,
                    num_building=num_building,
                    liter_building=liter_building,
                    level=level,
                    mono_address=mono_address,
                    phone=phone)
        session.add(place)
        session.commit()





def add_genre(name):
    genre = Genre(name=name)
    session.add(genre)
    session.commit()


def add_art_form(name):
    art_form = ArtForm(name=name)
    session.add(art_form)
    session.commit()


def add_user_friendly_event(user_id, event_id, friendly, is_visit):
    user_friendly_event = UserFriendlyEvent(id_user=user_id,
                                            id_event=event_id,
                                            friendly=friendly,
                                            is_visit=is_visit)
    session.add(user_friendly_event)
    session.commit()


def add_user_friendly_genre(user_id, genre_id, friendly):
    user_friendly_genre = UserFriendlyGenre(id_user=user_id,
                                            id_genre=genre_id,
                                            friendly=friendly)
    session.add(user_friendly_genre)
    session.commit()


def add_user_friendly_art_form(user_id, art_form_id, friendly):
    user_friendly_art_form = UserFriendlyArtForm(id_user=user_id,
                                                 id_artform=art_form_id,
                                                 friendly=friendly)
    session.add(user_friendly_art_form)
    session.commit()


def add_user_friendly_organizer(user_id, organizer_id, friendly):
    user_friendly_organizer = UserFriendlyOrganizer(id_user=user_id,
                                                    id_organizer=organizer_id,
                                                    friendly=friendly)
    session.add(user_friendly_organizer)
    session.commit()


def add_user_friendly_place(user_id, place_id, friendly):
    user_friendly_place = UserFriendlyPlace(id_user=user_id,
                                            id_place=place_id,
                                            friendly=friendly)
    session.add(user_friendly_place)
    session.commit()


# Функция для удаления всех записей из переданных списком таблиц. Напр.: [User] или [User, Genre, ...]
def full_delete_table_records(tables):

    for table in tables:
        table_up = table.capitalize()
        table_class = globals()[table_up]
        session.query(table_class).delete()
        print(f"Таблица {table_up} полностью очищена.")
    session.commit()


def total_delete_table_records(confirm):
    if not confirm:
        print("Введите в качестве аргумента - 1, для подтверждения полной очистки Базы Данных.")
    elif confirm == 1:
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        for table_name in tables:
            if inspector.has_table(table_name):
                tbl = Table(table_name, metadata)
                session.execute(tbl.delete())

        session.commit()
        print("Все записи были успешно удалены из всех таблиц.")
    else:
        print("Вы вызвали функцию 'удаления всех значений из всех таблиц' и передали аргумент отменяющий это действие.")


def delete_concrete_entry_in_table(table_name, entry_id):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    table_lower = table_name.lower()
    if table_lower in existing_tables:
        # Получаем класс модели таблицы по имени таблицы
        if table_name[0].isupper():
            table_class = globals()[table_name]
        else:
            table_up = table_name.capitalize()
            table_class = globals()[table_up]

        # Ищем запись по первичному ключу
        entry = session.query(table_class).get(entry_id)

        if entry:
            # Удаляем запись из сессии и подтверждаем изменения
            session.delete(entry)
            session.commit()
            print(f"Запись с id={entry_id} успешно удалена из таблицы {table_name.capitalize()}.")
        else:
            print(f"Запись с id={entry_id} не найдена в таблице {table_name.capitalize()}.")
    else:
        print(f"Таблицы {table_name} не существует. Существующие таблицы: {', '.join(existing_tables)}.")


def update_cell_in_table(table_name, field, id, value):
    if table_name[0].isupper():
        table_class = globals()[table_name]
    else:
        table_name = table_name.capitalize()
        table_class = globals()[table_name]
    # Ищем пользователя по первичному ключу
    table = session.query(table_class).get(id)

    if table:
        # Обновляем поле соответствующее переданному значению
        setattr(table, field, value)
        session.commit()
        print(f"Поле '{field}' строки с id={id} успешно обновлено.")
    else:
        print(f"Пользователь с id={id} не найден.")


def print_table(table_name):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    table_lower = table_name.lower()
    # Проверяем, существует ли таблица
    if table_lower in existing_tables:
        # Получаем класс таблицы по названию
        table_class = globals()[table_name]

        # Получаем все записи из таблицы
        records = session.query(table_class).all()

        # Выводим значения записей
        for record in records:
            record_dict = {}
            for column in table_class.__table__.columns:
                if column.name == 'id':
                    # Добавляем поле 'id' со значением record.id в словарь
                    record_dict['id'] = record.id
                else:
                    # Добавляем все остальные поля со значениями в словарь
                    value = getattr(record, column.name)
                    record_dict[column.name] = value
            print(record_dict)
    else:
        print(f"Таблицы {table_name} не существует.")


def get_table(table_name):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    table_lower = table_name.lower()

    # Проверяем, существует ли таблица
    if table_lower in existing_tables:
        # Получаем класс таблицы по названию
        table_class = globals()[table_name]

        # Получаем все записи из таблицы
        records = session.query(table_class).all()

        rows = []

        # Проходимся по записям и формируем значения строк
        for record in records:
            row_dict = {}
            for column in table_class.__table__.columns:
                if column.name == 'id':
                    # Добавляем поле 'id' со значением record.id в словарь
                    row_dict['id'] = record.id
                else:
                    # Добавляем все остальные поля со значениями в словарь
                    value = getattr(record, column.name)
                    row_dict[column.name] = value
            rows.append(row_dict)

        return rows
    else:
        print(f"Таблицы {table_name} не существует.")
        return []

def get_table_row(table_name, row_id):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    table_lower = table_name.lower()

    # Проверяем, существует ли таблица
    if table_lower in existing_tables:
        # Получаем класс таблицы по названию
        table_class = globals()[table_name]

        # Получаем запись из таблицы по указанному идентификатору
        record = session.query(table_class).get(row_id)

        # Проверяем, найдена ли запись
        if record is not None:
            row_dict = {}
            for column in table_class.__table__.columns:
                if column.name == 'id':
                    # Добавляем поле 'id' со значением record.id в словарь
                    row_dict['id'] = record.id
                else:
                    # Добавляем все остальные поля со значениями в словарь
                    value = getattr(record, column.name)
                    row_dict[column.name] = value

            return row_dict
        else:
            print(f"Запись с идентификатором {row_id} не найдена в таблице {table_name}.")
    else:
        print(f"Таблицы {table_name} не существует.")


def help():
    print("add_user, add_genre, ... - добавляет в ручном режиме запись в таб")
    print("add_test_var(n) - автоматически заполняет все таблицы значениями(для тестом). n - желаемое количество строк для каждой таблицы")
    print("full_delete_table_records(table) - удаляет все строки из таблицы. В table можно передавать список: напр. ['event', 'user', 'Genre']")
    print("total_delete_table_records(n) - полностью сносит все таблицы в БД. В качестве подтверждения вайпа таблиц нужно передать аргумент (1)")
    print("delete_concrete_entry_in_table('table', n) - удаляет конкретную запись из нужной таблицы. n - номер строки по полю 'id'")
    print("update_cell_in_table('user', 'f_name', 2, 'Nikita') - обновляет информацию в конкретной ячейке. (таблица, поле, номер строки, заменяемое значение)")
    print("print_table('User') - изи принтит таблицу")
    print("get_table(table_name) - возвращает все значения строк конкретной таблицы в формате словаря")
    print("get_table_row(table_name, 5) - возвращает значения конкретной строки в конкретной таблице")
    print("help() - возвращает описание функций")
    print("")
    print("* названия таблиц в аргументах передаются строкой, строка НЕ чувствительна к регистру")