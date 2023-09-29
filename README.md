# TEST TASK SOLUTION
Hello, this is my solution to the 
test task for the position of 
**Backend(Python) Developer**
<br>[Test task](https://docs.google.com/document/d/1tLsE_zjQp25IaoE6cbeaZDp3qyn3EqRGcmAPZAgv2BU/edit)
<br>
### Let`s started

## REQUIREMENTS
1. Django 3.X;
2. Python 3.9+
3. PostgreSQL

## INSTALLATION
To install this project in your local machine, 
create a new Django project in ~~PyCharm~~ 
your favorite IDE.
To clone this repo:<br>
```commandline
git clone https://github.com/Dimaaap/Backend-dev-task
```
Ok, you did the first step to install it.
Then go to the project directory
```commandline
cd Backend-dev-task
cd test_project
```
Then it will be super 
to create virtual environment. To do this
writes the next command:
```commandline
python -m venv env
```
After the virtual environment is created,
it should be activated by writing the 
```commandline
cd env/Scripts/activate
```
Or, if this command doesn`t work, write the next commands
```commandline
cd env/Scripts
./activate
cd ..
cd ..
```
Ok, now our virtual environment is created and ready to work
You need to install all dependencies.
Just write the command in your command line:

```commandline
pip install -r requirements.txt
```
And migrate db
```commandline
python manage.py migrate
```

## USAGE
After this preparatory stage, there is one more important step
We need to load test data into our database. For this, there is a file [`create_test_data.py`](https://github.com/Dimaaap/Backend-dev-task/blob/master/test_project/create_test_data.py) in the project.
This is a script that loads this data into our database

To download data, you need to execute the command

```commandline
python create_test_data.py
```
This file is related to 
`test_data_storage.py.` 
Actually, `test_data_storage.py` is just a set of data 
classes for `create_test_data.py`
After that, you can safely run the command
```commandline
python manage.py runserver
```
In order to check the work. 
You need to enter `/spend` in the URL line. 
In order to see the aggregated data from the `SpendStatistic`
model And `/revenue` to see data from the 
`RevenueStatistic` table

## Contacts
1. <a href="mailto:procdima49@gmail.com">My email</a>
2. [My LinkedIn](https://www.linkedin.com/in/dproc/)
3. Telegram - @dimaapp25


