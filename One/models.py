from Py_Flask.ext import dbs


class User(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    username = dbs.Column(dbs.String(16))

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()


class Student(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    s_name = dbs.Column(dbs.String(20))
    s_password = dbs.Column(dbs.String(256))