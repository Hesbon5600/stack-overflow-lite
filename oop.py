

class AbstractModel(object):
    def __init__(self, id):
        self.id = id


class User(AbstractModel):
    users = []

    def __init__(self, user_id, username, password, email):
        super().__init__(user_id)
        self.username = username
        self.password = password
        self.email = email
        self.data = {'id': self.id, "username": self.username,
                     "password": self.password, "email": self.email}
        User.users.append(self.data)

    def update_user(self, data):
        accepted_values = ["id", "username", "password", "email"]
        for k in data.keys():
            if k not in accepted_values:
                return False
        for user in User.users:
            if data["id"] == user["id"]:
                user["username"] = data["username"]
                user["password"] = data["password"]
                user["email"] = data["email"]
                self.username = data["username"]
                self.password = data["password"]
                self.email = data["email"]

                return True
            
        return False

    def __repr__(self):
        return "User {}".format(self.username)


class Question(AbstractModel):

    def __init__(self, question_id, author_id, question_details, date_posted):
        super().__init__(question_id)
        self.author_id = author_id
        self.question_details = question_details
        self.date_posted = date_posted

    def update_question(self):
        pass

    def delete_question(self):
        pass

    def get_question(self):
        pass

    def __repr__(self):
        return "Question {}".format(self.question_details)


class Answer(AbstractModel):

    def __init__(self, answer_id, question_id,
                 author_id, answer_details, date_posted, accepted):
        super().__init__(answer_id)
        self.question_id = question_id
        self.author_id = author_id
        self.answer_details = answer_details
        self.date_posted = date_posted
        self.accepted = accepted

    def get_answer(self):
        pass

    def update_answer(self):
        pass

    def __repr__(self):
        return "Question {}".format(self.answer_details)
