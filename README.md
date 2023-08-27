# Flask Boilerplate Overview

Presented here is a Flask boilerplate code designed to facilitate the swift setup of Flask applications.

## Key Boilerplate Features:

1. **Versatile Configuration Setup:** This boilerplate enables the use of a single application for diverse configurations, determined by unique identifiers.

2. **Identifier-linked Logging:** Logging activities are stored in date-stamped files within folders labeled by the corresponding identifier, enhancing traceability.

3. **Config Reader (.ini based):** The code incorporates a configuration reader that interprets settings employed within the product, following the .ini configuration format.

4. **Structured Initial Application Setup:** A foundational application folder structure is prearranged to promote organized development.

5. **Docker File Included:** Inclusion of a Dockerfile streamlines containerization for efficient deployment.

6. **Linting Configuration (.pylintrc):** The boilerplate integrates a .pylintrc file, furnishing configuration specifications for linting and addressing related coding issues.

7. **Flask Application Test Suite:** A test setup for the Flask application is readily available, simplifying the process of quality assurance.

---

**Running the Application:**

1. Create a virtual environment using `python -m venv venv`.
2. Activate the virtual environment.
3. Enhance pip by executing `python -m pip install --upgrade pip`.
4. Install necessary modules with `pip install -r requirements.txt`.
5. Start the application using the command `python app.py`.

**Generating Lint Report:**

1. Generate the lint report with the command `pylint src app.py --output lint_report.txt`. (The file *lint_report.txt*  is omitted from Git inclusion.)

**Unit Testing and Code Coverage:**

1. Execute test cases with `coverage run -m pytest`.
2. Generate a code coverage report using `coverage html`.

---

Effortlessly set up Flask applications using this boilerplate, maximizing efficiency and maintainability in your development projects.