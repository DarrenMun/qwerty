from wsgi import db
from wsgi import Student
import os

db.create_all()

# Data to initialize database with
Data = [
	{'name'		: 'Darren'	,'physics': 80, 'maths': 60, 'chemistry':45},
	{'name'		: 'Jerry'	,'physics': 50, 'maths': 45, 'chemistry':45},
]

# Iterate over the PEOPLE structure and populate the database
for xData in Data:
	d = Student(name=xData['name'], physics=xData['physics'],maths=xData['maths'], chemistry=xData['chemistry'])
	db.session.add(d)

db.session.commit()