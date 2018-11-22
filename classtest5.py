#Exercise of 9-11


from classtest2 import User
import Privileges


class Admin(User):
    def __init__(self, firstname, lastname, sexuality='male', career='engineer'):
        super().__init__(firstname, lastname, sexuality='male', career='engineer')
        self.privilege = Privileges.Privileges()


admin1 = Admin('Mike', 'Carson')
admin1.privilege.describe_privileges()
admin1.increment_login_attempts()
admin1.show_login_attempts()


