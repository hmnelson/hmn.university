from zope.publisher.browser import BrowserView
from hmn.university.database import get_connection
from plone import api
import logging
# import transaction
logger = logging.getLogger('export')


class ExportStudentToMySQL(BrowserView):
    def __call__(self):
        students = api.content.find(portal_type='Student', sort_on='created')
        connection = get_connection()
        results = ['Done:']
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('drop table if exists students')
                create_table_sql = """CREATE TABLE `students` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `student_name` varchar(255) COLLATE utf8_bin NULL,
                    `age` varchar(255) COLLATE utf8_bin NULL,
                    `gender` varchar(255) COLLATE utf8_bin NULL,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;
                """
                cursor.execute(create_table_sql)
                connection.commit()
                for student in students:
                    obj = student.getObject()
                    obj_values = (
                        obj.Title(),
                        str(obj.age),
                        obj.gender
                    )
                    sql = """INSERT INTO `students` (
                        `student_name`,
                        `age`,
                        `gender`
                    ) VALUES (
                        '%s',
                        '%s',
                        '%s'
                    )""" % obj_values
                    logger.info(sql)
                    logger.info(obj_values)
                    results.append('%s  %s  %s' % obj_values)
                    cursor.execute(sql)
                    connection.commit()
        return '\n'.join(results)


class ExportDepartmentToMySQL(BrowserView):
    def __call__(self):
        departments = api.content.find(portal_type='Department',
                                       sort_on='sortable_title')
        connection = get_connection()
        results = ['Done:']
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('drop table if exists departments')
                create_table_sql = """CREATE TABLE `departments` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `department_name` varchar(255) COLLATE utf8_bin NULL,
                    `college` varchar(255) COLLATE utf8_bin NULL,
                    `accredited` varchar(16) COLLATE utf8_bin NULL,
                    `department_created_date` DATE NULL,
                    `total_students` INT,
                    `total_teachers` INT,
                    `total_courses` INT,
                    PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;
                """
                cursor.execute(create_table_sql)
                connection.commit()
                for department in departments:
                    obj = department.getObject()
                    obj_values = (
                        obj.Title(),
                        obj.college,
                        obj.accredited,
                        obj.department_created_date,
                        obj.totalStudents(),
                        obj.totalTeachers(),
                        obj.totalCourses()
                    )
                    sql = """INSERT INTO `departments` (
                        `department_name`,
                        `college`,
                        `accredited`,
                        `department_created_date`,
                        `total_students`,
                        `total_teachers`,
                        `total_courses`
                    ) VALUES (
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s'
                    )""" % obj_values
                    logger.info(sql)
                    logger.info(obj_values)
                    results.append('%s  %s  %s %s %s %s %s' % obj_values)
                    cursor.execute(sql)
                    connection.commit()
        return '\n'.join(results)
