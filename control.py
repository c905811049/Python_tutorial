import pymysql

con = pymysql.Connect(host="localhost",port=3306,user="root",passwd="admin",db="db",charset="utf8")
print("check:",con)

cursor = con.cursor()

def add_employee(cursor):
    id = input("请输入员工ID: ")
    name = input("请输入员工姓名: ")
    sex = input("请输入员工性别 (男/女): ")
    age = input("请输入员工年龄: ")
    sal = input("请输入员工薪水: ")
    deptno = input("请输入员工部门编号: ")
    password = input("请输入员工密码: ")

    sql = f"INSERT INTO employee (id, name, sex, age, sal, deptno, password) VALUES ('{id}', '{name}', '{sex}', '{age}', '{sal}', '{deptno}', '{password}')"
    cursor.execute(sql)
    con.commit()

    print("员工添加成功！")



# def find_employee_by_id(id):
#     for employee in employees:
#         if employee['id'] == id:
#             return employee
#     return None


def query_employee(cursor):
    id = input("请输入要查询的员工ID: ")
    sql = f"SELECT * FROM employee WHERE id = '{id}'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        print("员工信息:", row)
    else:
        print("员工未找到!")


def modify_salary(cursor):
    id = input("请输入要修改薪水的员工ID: ")
    new_sal = input("请输入新的薪水: ")
    sql = f"UPDATE employee SET sal = '{new_sal}' WHERE id = '{id}'"
    cursor.execute(sql)
    con.commit()
    
    print("薪水修改成功!")


def delete_employee(cursor):
    id = input("请输入要删除的员工ID: ")
    sql = f"DELETE FROM employee WHERE id = '{id}'"
    cursor.execute(sql)
    con.commit()
    
    print("员工删除成功!")
        

def display_employees(cursor):
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)



def main():
    welcome = """
    ####################################
    #      欢迎使用员工系统V1.0         #
    #                                  #
    #####################################
    """
    
    main_menu = """
    #######################################
    #              主菜单                  #
    # 1.增加员工
    # 2.查询员工
    # 3.修改员工薪水
    # 4.删除员工
    # 5.公司员工列表
    # 6.退出系统
    #######################################
    """

    print(welcome)

    while True:
        print(main_menu)
        choice = input("请选择操作 (1-6): ")

        if choice == '1':
            add_employee(cursor)
        elif choice == '2':
            query_employee(cursor)
        elif choice == '3':
            modify_salary(cursor)
        elif choice == '4':
            delete_employee(cursor)
        elif choice == '5':
            display_employees(cursor)
        elif choice == '6':
            print("感谢使用员工系统！再见！")
            break
        else:
            print("无效选择，请重新输入！")
            
    con.close()

main()