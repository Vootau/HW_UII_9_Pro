import hashlib
import uuid
from datetime import datetime


class Session:

    def __init__(self, user):
        self.session_id = str(uuid.uuid4())
        self.session_start = datetime.now()
        self.session_stop = None
        self.user = user

    current_session = []


    def start_session(self):
        Session.current_session.append(Session(self))

    def end_session(self):
        for session in Session.current_session:
            if session.user.name == self.name:
                Session.current_session.remove(session)

    @classmethod
    def get_active_sessions_by_username(cls, username):
        active_sessions = []
        for session in Session.current_session:
            if session.user.name == username:
                active_sessions.append(session)
                print(active_sessions)
            else:
                print(f'У пользователя {username} нет активных сессий.')


    @classmethod
    def get_all_sessions(cls):
        return Session.current_session
