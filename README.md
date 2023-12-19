# task-manager


## Description
In this site you can manage process developing different projects. 
Here you have possibility to add, update chose tasks and work on
the projects with comfort. Managers can add, change and remove
all workers, but other can change only yourself. You can join or
leave the task or update and delete it. Tasks have indicators for
you know what task have done and what is in progress and follow for the
deadlines with a special field. There is have page with all types of tasks,
page with akk workers and page with all positions in your company, if you
think there a little positions, add a new one, you can find them fast with
search form. Good luck to you with your work process.


## Guideline how to use

1) Open terminal and clone the repo (`git clone https://github.com/prochigor/task-manager.git`)

2) Open cloned folder

3) Activate venv on the project
- Open terminal and write: 
  - On Windows: (`python -m venv venv`) and (`venv\Scripts\activate`)
  - On Mac: (`python3 -m venv venv`) and (`source venv/bin/activate`)

4) Install needed requirements:
  Write in terminal (`pip install -r requirements.txt`)

5) Migrate
  Write in terminal (`python manage.py migrate`)

6) Add data to database:
  Write in terminal (`python manage.py loaddata task_manager_db_data.json`)

7) Run server
  Write in terminal `python manage.py runserver`

8) Open page with link in terminal

9) After loading data from fixture you can use following superuser (or create another one by yourself): 
- `Login: admin.user`
- `Password: 1qazcde3`

10) Feel free to add more data using admin panel, if needed.

11) (Data type format: `YYYY-mm-dd hh:mm`)
