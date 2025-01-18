from classes.users import User, Admin, Customer
from classes.session import Session


adm = Admin('Админ', 'adm@adm.in', 'admin', 5)

active_sessions = Session.get_all_sessions()

if __name__ == '__main__':
    print(adm.list_users())              # Вывод: ['Админ']
    print([Admin.get_user_info('Vik')])  # Вывод: ['Wrong username']
    print(adm.get_details())             # Вывод: {'Имя': 'Админ', 'Эл.почта': 'adm@adm.in', 'Уровень прав': 5}
    Customer.register_user(
        'Vik', 'vik@vik.com', '123456, Country, City', 'qwerty'
    )                                                           # Вывод: Пользователь Vik зарегистрирован.
    print(adm.list_users())                                     # Вывод: ['Админ', 'Vik']
    print([Admin.get_user_info('Vik')])  # Вывод: ['Имя: Vik \nАдрес: 123456, Country, City \nЭл.почта: vik@vik.com']
    User.log_in('Vik', 'qwer')           # Вывод: Неверный пароль
    User.log_in('Vik', 'qwerty')         # Вывод: Вход выполнен
    User.log_in('Админ', 'admin')
    print(f'Количество активных сессий: {len(active_sessions)}')
    User.log_out('Админ')                  # Вывод: Пользователь Админ вышел из системы
    User.log_out('Админ')                  # Вывод: Админ, Вы не были авторизованы
    print(f'Количество активных сессий: {len(active_sessions)}')
    Session.get_active_sessions_by_username('Админ')  # Вывод: У пользователя Админ нет активных сессий.
    Admin.get_sessions('Админ')  # Вывод: У пользователя Админ нет активных сессий.
    print(Admin.delete_user('Vik'))  # Вывод: Пользователь Vik удален!





