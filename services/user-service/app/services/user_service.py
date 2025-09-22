# services/user-service/app/services/user_service.py

from app.models.user import Role, User
from app.utils.db import db
from app.utils.password_hasher import PasswordHasher


class UserService:
    def register_new_user(self, data):
        # Kiểm tra username hoặc email đã tồn tại chưa
        if (
            User.query.filter_by(username=data["username"]).first()
            or User.query.filter_by(email=data["email"]).first()
        ):
            return None  # Trả về None nếu đã tồn tại

        hashed_password = PasswordHasher.hash(data["password"])

        new_user = User(
            username=data["username"],
            email=data["email"],
            full_name=data["fullName"],
            password_hash=hashed_password,
        )

        # Gán vai trò mặc định (ví dụ: 'reporter')
        reporter_role = Role.query.filter_by(name="reporter").first()
        if not reporter_role:
            reporter_role = Role(name="reporter")
            db.session.add(reporter_role)

        new_user.roles.append(reporter_role)

        db.session.add(new_user)
        db.session.commit()

        return new_user
