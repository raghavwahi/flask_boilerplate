# Flask Boilerplate

This is flask boilerplate code which can be used to set up a flask application.

This boilerplate code consists of the following features:

* Multi user application setup
* Logging (Date named file based per user)
* Config reader(.ini based)
* Basic application folder structure

<hr/>
To run the application, follow below steps:

* Upgrade pip by running the command `python -m pip install --upgrade pip`.
* Install required modules by running the command `pip install -r requirements.txt`.
* To start the application, run the command `python app.py`.

<hr/>
To generate lint report, follow below steps:

* Install pylint by running the command `pip install pylint --upgrade`.
* Run the command `pylint src app.py > lint_report.txt`.

<hr/>
To run unit tests and generate code coverage report, follow below steps:

* Install pytest and coverage by running the command `pip install pytest coverage --upgrade`.
* To execute test cases, run the command `py.test src\test -cov=src`.
* To generate coverage report run the command `coverage html`.
