from crud import *

def add_test_var(quanttity_records=None):
    if quanttity_records is None:
        print("Таблицы не были заполнены. Аргумент должен передавать количество добавляемых строк в каждую таблицу.")
    else:
        total_delete_table_records(1)
        for i in range(quanttity_records):
            add_user(f_name=f"First Name {i}", l_name=f"Last Name {i}", nickname=f"Nickname {i}",
                     birthday=19900101, now_place=1, phone=1234567890, e_mail=f"user{i}@example.com")
        print("add_user")

        for i in range(quanttity_records):
            add_event(name=f"Event {i}", description=f"Description {i}", art_form_id=1, genre_id=1,
                      date_time=20220101, dt_start=20220101, dt_over=20220102, cost_min=10, cost_max=100,
                      currency="USD", organizer_id=1, place_id=1, link=f"event{i}.com", photo=f"photo{i}.jpg")
        print("add_event")

        for i in range(quanttity_records):
            add_organizer(name=f"Organizer {i}", description=f"Description {i}")
        print("add_organizer")

        for i in range(quanttity_records):
            add_place(name=f"Place {i}", description=f"Description {i}", country="Country", city="City",
                      district="District", street="Street", num_building=i, liter_building="A", level=1,
                      mono_address="Novaya st., h. 1, lit. A")
        print("add_place")

        for i in range(quanttity_records):
            add_genre(name=f"Genre {i}")
        print("add_genre")

        for i in range(quanttity_records):
            add_art_form(name=f"Art Form {i}")
        print("add_art_form")

        for i in range(quanttity_records):
            add_user_friendly_event(user_id=i, event_id=i, friendly=True, is_visit=False)
        print("add_user_friendly_event")

        for i in range(quanttity_records):
            add_user_friendly_genre(user_id=i, genre_id=i, friendly=True)
        print("add_user_friendly_genre")

        for i in range(quanttity_records):
            add_user_friendly_art_form(user_id=i, art_form_id=i, friendly=True)
        print("add_user_friendly_art_form")

        for i in range(quanttity_records):
            add_user_friendly_organizer(user_id=i, organizer_id=i, friendly=True)
        print("add_user_friendly_organizer")

        for i in range(quanttity_records):
            add_user_friendly_place(user_id=i, place_id=i, friendly=True)
        print("add_user_friendly_place")