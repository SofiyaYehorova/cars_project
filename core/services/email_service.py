import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclass.user_dataclass import ProfileDataClass, UserDataClass
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject: ''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    # @classmethod
    # def test_email(cls):
    #     cls.__send_email('yehorova66@gmail.com', 'test_email.html', {}, 'Hello')
    @classmethod
    def test_email(cls):
        cls.__send_email('yehorova66@gmail.com', 'test_email.html', {}, 'Hello')

    @classmethod
    def register_email(cls, user: UserDataClass):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'  # FOR FRONTEND REACT
        cls.__send_email(user.email, 'register.html', {'name': user.profile.name, 'url': url}, 'Register')


    @classmethod
    def recovery_password(cls, user: UserDataClass):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost:3000/recovery_password/{token}'
        cls.__send_email(user.email, 'recovery_password.html', {'name': user.profile.name, 'url': url},
                         'Recovery password')

    @classmethod
    def created_car_by_seller(cls, user: UserDataClass, car):
        cls.__send_email(user.email, 'created_car.html', {'name': user.profile.name},
                         'Created car')
