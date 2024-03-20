students = {}
professors = {}
courses = {}
take_courses = {}
course_grades = {}


def add_student(num, dep):
    int_num = int(num)
    if int_num in students:
        print(f'student {int_num} with this student already exists')
    else:
        students.update({int_num: dep})


# add student
add_student(9974262, 'shiraz')
# # print(students)
add_student(9974263, 'shiraz')
add_student(9974264, 'shiraz')
add_student(9974265, 'shiraz')


# std_4 = add_student('9974262', 'shiraz')
# print(students)


def add_professor(dep, id, name, age):
    int_id = int(id)
    if int_id in professors:
        print(f'professor with {int_id} this id already exists')
    else:
        courses = input('enter yout course: ').split()
        if len(courses) < 1:
            print('professor must have at least one course')
        else:
            professors.update({int_id: {'name': name, 'dep': dep, 'age': age, 'courses': courses}})


# add professor
# p1 = add_professor('shiraz', 5225555, 'zarei', 35)
# p2 = add_professor('shiraz', 5151155, 'naeimi', 40)
# print(professors)

# professors_courses = []
# for p_id, info in professors.items():
#     professors_courses.extend(info['courses'] + info['name'])


def add_course(dep, name, unit, day, start, end):
    int_unit = int(unit)
    if start < 6 and end > 18:
        print('range start and end between 6 to 18')

    if name in courses:
        print('course with name already exists')
    else:
        courses.update({name: {'unit': int_unit, 'day': day, 'start': start, 'end': end}})
        # professors_courses = []
        # for p_id, info in professors.items():
        #     professors_courses.extend(info['courses'])


add_course('shiraz', 'db', 3, 'sun', 12, 14)


def take_course(name, num):
    int_num = int(num)
    if name not in courses or int_num not in students:
        print('Invalid command')
    else:
        take_courses[int_num] = name


take_course('db', '9974262')
take_course('db', '9974263')
take_course('db', '9974264')
take_course('db', '9974265')
take_course('db', '9974265')
take_course('db', '9974261')
take_course('db', '9974265')
take_course('db', '9974265')


# print(take_courses)

# while True:
#     name = input('Enter your name: ')
#     num = int(input('Enter your num: '))
#     int_num = int(num)
#
#     if name in take_courses and int_num in take_courses.values():
#         print('invalid command')
#     else:
#         take_courses[int_num] = name
#         print(take_courses)


def course_grade(name):
    if name not in take_courses:
        print('there is no course with this name')
    else:
        list_grade = []
        new_list_grade = []
        grade = input('enter your grade: ')
        list_grade.append(grade)
        for i in list_grade:
            if 0 > float(i) > 20:
                print('invalid grade')
            else:
                new_list_grade.append(float(i))
        if len(take_courses) != len(new_list_grade):
            print('the number of grades and students are not equal')


def find_grade(name, num):
    pass


def find_gpa(num):
    pass


def find_rank(num):
    pass


def drop_course(name, num):
    pass


def show_report(num):
    pass


def top_score(name, avg):
    pass
