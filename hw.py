#Queries:
#--1.
# CREATE TABLE if not exists courses (
#     course_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     topic TEXT NOT NULL,
#     hours INTEGER NOT NULL
# );
#
# CREATE TABLE if not exists students (
#     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NULL
# );
#
# CREATE TABLE if not exists course_student (
#        course_id INTEGER NOT NULL,
#        student_id INTEGER NOT NULL,
#        grade INTEGER NOT NULL,
# 	                 PRIMARY KEY(course_id, student_id)
# 	      FOREIGN KEY (course_id) REFERENCES courses(course_id)
# 	      FOREIGN KEY (student_id) REFERENCES students(student_id)
# 	);
#  --2.
# INSERT INTO courses (topic, hours) VALUES ('Math', 8);
# INSERT INTO courses (topic, hours) VALUES ('Python', 4);
#
# INSERT INTO students (name, email) VALUES ('Shani Staretz', 'shani.s@f.u');
# INSERT INTO students (name, email) VALUES ('Itai G', 'itai.g@t.q');
#
# INSERT INTO course_student (course_id, student_id,grade) VALUES (1, 1, 100);
# INSERT INTO course_student (course_id, student_id,grade) VALUES (2, 1, 101);
#
# INSERT INTO course_student (course_id, student_id,grade) VALUES (1, 2, 50);
# INSERT INTO course_student (course_id, student_id,grade) VALUES (2, 2, 20);

import sqlite3


def connect_to_db():
    db_name: str = "Jan-8-25.db"
    connector = sqlite3.connect(db_name)
    connector.row_factory = sqlite3.Row  # allow to address the values by column name
    return connector


def execute_read_query(connector, query, parameters=None):
    """
    will execute select queries.
    if requires input dynamic parameters
    will add the parameters to the query.
    the function returns the result of the
    query as a list of sql_objects
    """
    try:
        cursor = connector.cursor()  # pointer where you are now,to read and write
        print("execute query:", query)
        if parameters is not None:
            return cursor.execute(query, parameters)
        return cursor.execute(query)
    except sqlite3.Error as e:
        raise e


def execute_change_query(connector, query, parameters=None):
    """
    the function receive the connection to the DB,
    a query that change the DB like: Insert,Drop,Create...
    a dynamic parameters that the query required.
    """
    cursor = connector.cursor()  # pointer where you are now,to read and write
    if parameters is not None:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    connector.commit()  ## this will write the changes to the DB


def print_results(rows):
    """
    the function receive a list of sql_objs,
    prints the content objects as a tuple
    """
    rows_list = [tuple(row) for row in rows]
    for row in rows_list:
        print(row)


def insert_new_course(my_connector):
    query_courses_names = "SELECT c.topic from courses c"
    courses_names_sqls = execute_read_query(my_connector, query_courses_names)
    courses_names_dict = [dict(row) for row in courses_names_sqls]
    courses_names = list(map(lambda c: list(c.values())[0], courses_names_dict))
    print(courses_names)
    course_topic = input("please enter course's name:")
    course_hours = int(input("please enter course's hours:"))
    if course_topic in courses_names:
        print("this course is already in the DB")
    else :
        query_insert = "INSERT OR REPLACE INTO courses (topic, hours) VALUES (?, ?);"
        execute_change_query(my_connector,query_insert,(course_topic,course_hours))

def run_homework():
    my_connector = None
    try:
        my_connector = connect_to_db()
        # 4. display all courses:
        query_select_courses = "SELECT c.* from courses c"
        courses = execute_read_query(my_connector, query_select_courses)
        print_results(courses)
        # insert new course if not exist, by topic name
        insert_new_course(my_connector)
        query_select_courses = "SELECT c.* from courses c"
        courses = execute_read_query(my_connector, query_select_courses)
        print_results(courses)
    except sqlite3.Error as e:
        print(e)
    finally:
        if my_connector is not None:
            my_connector.close()


if __name__ == "__main__":
    run_homework()
