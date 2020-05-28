import os
import unittest

from app import app, db
from app.models import User, Quiz, Qanswers

class UserQuizCase(unittest.TestCase): #to run test enter python unit_test.py -v into TERMINAL
    
    def setUp(self):
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
            self.app = app.test_client()
            db.create_all()
            user1 = User(id=0000000, username='username1', email='123@mail.com' )
            user2 = User(id=5555555, username='username2', email='456@mail.com' )
            quiz1 = Quiz(quizname='example_quiz', creator_id='0000000', q1='question1', q2='question2', q3='question3' )
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(quiz1)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        #test for checking password system
    def test_password_system(self):
        temp = User.query.get('0000000')
        temp.set_password('1234')
        self.assertFalse(temp.check_password('5678'))
        self.assertTrue(temp.check_password('1234'))


        #simple test to check if 404 errors work
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/index/asdqwe', content_type='html/text')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()