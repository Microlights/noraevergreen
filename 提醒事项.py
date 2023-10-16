import datetime  
  
def add_task():  
    task = input("请输入你的任务: ")  
    date_str = input("请输入任务的日期 (格式: YYYY-MM-DD): ")  
    try:  
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()  
    except ValueError:  
        print("错误的日期格式, 请使用'YYYY-MM-DD'格式")  
        return  
  
    print("已添加任务: ", task)  
    print("任务日期: ", date_str)  
  
    if date.today() >= date:  
        print("今天是任务日期！请记得完成任务！")  
    else:  
        print("任务还有", (date.today() - date).days, "天")  
  
while True:  
    add_task()
