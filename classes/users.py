import hashlib
import uuid
from classes.session import Session


class User:
    """
        Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, name, email, pswd):
        self.name = name
        self.email = email
        self.pswd = self.hash_password(pswd)  # Хэшируем пароль перед сохранением
        self.uuid = str(uuid.uuid4())  # Уникальный идентификатор пользователя
        self.is_authenticated = False  # Флаг для отслеживания состояния авторизации
        User.users.append(self)

    @classmethod
    def register_user(cls, name, email, address, pswd):
        """
        Метод для регистрации нового пользователя.
        Проверяется уникальность имени пользователя и создается новый объект класса Customer.
        """
        for user in cls.users:
            if user.name == name:
                raise ValueError("Пользователь с таким именем уже существует.")

        new_customer = Customer(name, email, address, pswd)
        print(f"Пользователь {new_customer.name} зарегистрирован.")
        return new_customer

    @classmethod
    def log_in(cls, username, pswd):
        """
        Метод для входа пользователя в систему.
        Проверяются имя пользователя и соответствие пароля.
        """
        for user in cls.users:
            if user.name == username:
                if user.is_authenticated:
                    print(f"{username} уже авторизован")
                    return False
                elif cls.check_password(user.pswd, pswd):
                    user.is_authenticated = True
                    Session.start_session(user)
                    print(f"{username}: Вход выполнен")
                    return True
                else:
                    print("Неверный пароль")
                    return False
        print(f"Пользователь {username} не найден")
        return False

    @classmethod
    def log_out(cls, username):
        """
        Метод для выхода пользователя из системы.
        Осуществляется проверка наличия пользователя в списке и его текущего состояния авторизации.
        """
        for user in cls.users:
            if user.name == username:
                if user.is_authenticated:
                    user.is_authenticated = False
                    print(f"Пользователь {username} вышел из системы")
                    Session.end_session(user)
                    return True
                else:
                    print(f"{username}, Вы не были авторизованы")
                    return False
        print("Пользователь не найден")
        return False

    @staticmethod
    def hash_password(pswd):
        return hashlib.sha256(pswd.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        hashed_provided_password = User.hash_password(provided_password)
        return stored_password == hashed_provided_password

    def get_details(self):
        pass


class Customer(User):
    def __init__(self, name, email, address, pswd):
        super().__init__(name,email,pswd)
        self.address = address

    def __str__(self):
        return f"Имя: {self.name} \nАдрес: {self.address} \nЭл.почта: {self.email}"

    def get_details(self):
        return {'Имя': self.name, 'Адрес': self.address, 'Эл.почта': self.email}


class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """

    def __init__(self, name, email, pswd, admin_level):
        super().__init__(name, email, pswd)
        self.admin_level = admin_level

    def __str__(self):
        return (
            f"Имя: {self.name} \nЭл.почта: {self.email} \nУровень: {self.admin_level}"
        )

    def get_details(self):
        return {'Имя': self.name, 'Эл.почта': self.email, 'Уровень прав': self.admin_level}

    def get_sessions(self):
        return Session.get_active_sessions_by_username(self)

    @staticmethod
    def list_users():
        """
        Выводит список имен всех пользователей.
        """
        return [user.name for user in User.users]

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя в списке пользователей.
        """
        for user in User.users:
            if user.name == username:
                User.users.remove(user)
        return f'Пользователь {username} удален!'

    @staticmethod
    def get_user_info(username):
        for user in User.users:
            if user.get_details()['Имя'] == username:
                user_info = user.__str__()
                return user_info
        return 'Wrong username'





