from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number, get_random_valid_phone_number


class UserLink:
    def __init__(self, self_link, edit, avatar):
        self.self_link = self_link
        self.edit = edit
        self.avatar = avatar

    def to_dict(self):
        return {"self": HrefLink(self.self_link).to_dict(), "edit": HrefLink(self.edit).to_dict(), "avatar": HrefLink(self.avatar).to_dict()}


class HrefLink:
    def __init__(self, href):
        self.href = href

    def to_dict(self):
        return {"href" : self.href}


class UserStatus:
    ACTIVE = "active"
    INACTIVE = "inative"
    IN_A_MEETING = "in_a_meeting"


class User:
    def __init__(self, id, first_name, last_name, gender, dob, email, phone, website, address, status, _links):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone
        self.website = website
        self.address = address
        self.status = status
        self._links = _links

    def to_dict(self):
        _links_dict = self._links.to_dict()
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name, 'gender': self.gender,
                'dob': self.dob,
                'email': self.email,
                'phone': self.phone, 'website': self.website, 'address': self.address, 'status': self.status, "_links": _links_dict}

    @staticmethod
    def generate_default_user_details(id, links=None):
        links = links or UserLink(self_link="https://gorest.co.in/public-api/users/1964", edit="https://gorest.co.in/public-api/users/1964",
                                  avatar="https://gorest.co.in/public-api/users/1964")
        return User(id=id, first_name="fadi" + str(get_rand_number_between_zero_to_max_number(100, 1)), last_name="zaboura", gender="male", dob="1992-12-10", email="fadi1012zaboura@gmail.com", website="test.com", address="test-address",
                    status=UserStatus.ACTIVE, _links=links, phone=get_random_valid_phone_number())
