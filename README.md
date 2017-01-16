# Install 

To install this program you need python 2 (tested with python 2.7)


	$ git clone https://github.com/solvo/ECSL.git
	$ cd ECSL/
	$ pip install -r requirements.txt


Configure the database

	$ python manage.py migrate
	$ python manage.py createsuperuser