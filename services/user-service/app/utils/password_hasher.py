# services/user-service/app/utils/password_hasher.py

import bcrypt


class PasswordHasher:
    @staticmethod
    def hash(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
