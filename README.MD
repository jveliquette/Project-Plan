# Project Plan

[Video Demo](https://www.youtube.com/watch?v=_eWCL2WeTcQ)

## Description

 - Project Plan is a project management application designed to help users organize and track tasks efficiently across multiple projects. With a focus on enhancing productivity and meeting deadlines, the app features a dynamic task due date chart and a responsive user interface that adapts seamlessly to various devices and screen sizes.

## Technologies Used

 - **Backend:** Python, Django, SQL
 - **Frontend:** JavaScript, Bulma
 - **Database:** SQLite

## Features
 - **Project and Task Management:** Create, edit, and delete projects and associated tasks.
 - **Task Due Date Chart:** Visual representation of upcoming due dates to prioritize and manage tasks effectively.
 - **Responsive User Interface:** Implemented using JavaScript and Bulma for a user-friendly experience on desktops, tablets, and mobile devices.
 - **Authentication:** User sign-up, login, and logout functionality.

## Setup and Installation
 1.	Clone the Repository:
    ```
    git clone https://github.com/jveliquette/Project-Plan.git
    cd Project-Plan
    ```

 2. Create and Activate a Virtual Environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
 3. Install Dependencies:
    ```
    pip install -r requirements.txt
    ```

 4. Set Up the Database:
    ```
    python manage.py migrate
    ```

 5. Create a Superuser:
    ```
    python manage.py createsuperuser
    ```

 6. Run the Application:
    ```
    python manage.py runserver
    ```

 7.	Access the Application:
    Open your browser and go to http://127.0.0.1:8000/ to view the application.

## Usage
 1.	**Create an Account:** Sign up with a username and a password.
 2.	**Add Projects:** Create new projects and set descriptions.
 3.	**Add Tasks to Projects:** Assign tasks with due dates to different projects.
 4.	**View Task Chart:** Use the task chart to get an overview of task deadlines and priorities.


## Contact
 For any questions or feedback, feel free to reach out to me at juliaveliquette@gmail.com.
