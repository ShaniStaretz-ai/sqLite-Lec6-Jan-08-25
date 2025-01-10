--1.
CREATE TABLE if not exists courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    hours INTEGER NOT NULL
);

CREATE TABLE if not exists students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NULL
);

CREATE TABLE if not exists course_student (
       course_id INTEGER NOT NULL,
       student_id INTEGER NOT NULL,
       grade INTEGER NOT NULL,
	                 PRIMARY KEY(course_id, student_id)
	      FOREIGN KEY (course_id) REFERENCES courses(course_id)
	      FOREIGN KEY (student_id) REFERENCES students(student_id)
	);
 --2.
INSERT INTO courses (topic, hours) VALUES ('Math', 8);
INSERT INTO courses (topic, hours) VALUES ('Python', 4);

INSERT INTO students (name, email) VALUES ('Shani Staretz', 'shani.s@f.u');
INSERT INTO students (name, email) VALUES ('Itai G', 'itai.g@t.q');

INSERT INTO course_student (course_id, student_id,grade) VALUES (1, 1, 100);
INSERT INTO course_student (course_id, student_id,grade) VALUES (2, 1, 101);

INSERT INTO course_student (course_id, student_id,grade) VALUES (1, 2, 50);
INSERT INTO course_student (course_id, student_id,grade) VALUES (2, 2, 20);