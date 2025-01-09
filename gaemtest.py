import random
import datetime
import os
#随机数生成两个，四则运算的随机生成
def random_operation():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    while True:
        operation=random.choice(['+','-','*','/'])
        if operation=='/' and num2==0:
            print("UN除数为0，不能计算，一亿分之一的概率，🥰🥰🥰恭喜你再来一份随机数😂🤣😂")
            num2=random.randint(1,100)
        else:
            break
    if operation=='+':
                result=num1+num2
    elif operation=='-':
                result=num1-num2
    elif operation=='*':
                result=num1*num2
    elif operation=='/':
                result=round(num1/num2,1)
    return operation,num1,num2,result
#获取用户输入的答案
def get_user_answer(prompt) :
    user_answer=input(prompt)
    try:
        return float(user_answer)
    except ValueError:
        print("请输入一个有效的数字！")
        return get_user_answer(prompt)
#检查用户输入的答案，并处理分数
def check(result,user_answer,score):
    if round(user_answer,1)==result:
        score+=10
        print("回答正确！！😎😊😎！！分数+10😘")
    else:
        score-=3
        print("回答错误！！😭😭😭！！分数-3😢")
    return score
#保存玩家分数到文件
def save_score_to_file(score,game_name,save_path=None):
    filepath_name = os.path.join(save_path, f"{game_name}_score.txt")
    try:
        with open(filepath_name, "a") as file:
            file.write(f'{now} \ngame_name:\n{game_name}\npassword:\n{check_password}\nscore:\n{score}')
    except IOError as e:
        print(f"保存分数时发生错误：{e}")
#主要框架，建议修改save_path如果你自己玩
if __name__ == "__main__":
    save_path =r"C:\Users\YUNDA\Desktop\Do"
    score=int(0)
    game_name="42"
    action = True
    action2=42
    action3="源码是史山，def定义用不来，但勉强跑起来了"
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    desktop_path = os.path.expanduser("~/Desktop/DO")
    print("hello欢迎来到❤❤🧡💛💚\n四则运算小游戏")
    print("Tip：整除无小数点💥")
    print("桌面路径：", desktop_path)
    action3=input("默认路径（储存游戏账户）：桌面/DO文件夹下\n左键点击长按拖动鼠标\ncrtl+c复制\ncrtl+v粘贴\n你的游戏数据路径:")
    save_path=action3.strip()
    while action== True:
        game_name = str(input("🕴(｡･∀･)ﾉﾞ输入角色名字："))
        filepath_name = os.path.join(save_path, f"{game_name}_score.txt")
        if os.path.exists(filepath_name):
            print(f"文件 {filepath_name} 存在。")
            with open(rf'{filepath_name}','r') as f:
                read_file = f.readlines()
                account = read_file[-5].strip()
                print(account)
                check_password = read_file[-3].strip()
                score = int(read_file[-1].strip())
                print("ok")
                if f"{game_name}" == account:
                    print(f"尊贵的VIP用户😎：{game_name}\n欢迎回来🎉🎉🎉🎉🎈\n🧠您的分数：{score}")
                    while action2==42:
                        password = str(input('输入密码:'))
                        check_password = read_file[-3].strip()
                        if password == check_password:
                            print("密码正确🍕💖🎉🎉🎉")
                            check_password = password
                            try:
                                with open(filepath_name, "a") as file:
                                    file.write(f'{now} \ngame_name:\n{game_name}\npassword:\n{check_password}\nscore:\n{score}\n')
                                    action2=False
                                    action=False
                            except IOError as e:
                                print(f"保存分数时发生错误：{e}")

                        elif password != check_password:
                            print("密码错误😥✨✨✨✨")
                            continue
        else:
            print(f"WelCOME,新用户😀：{game_name}")
            check_password = input('创建密码😙：')
            confirm_password = input('确认密码🎈：')
            if check_password == confirm_password:
                print("正确😊😎😎")
                try:
                    with open(fr"{save_path},{game_name}_score.txt",'w') as file:
                        file.write(f'{now} \ngame_name:\n{game_name}\npassword:\n{check_password}\nscore:\n{score}\n')
                        action=False
                        action2= False
                except FileNotFoundError:
                    print("未找到文件")
    while True:
        filepath_name = os.path.join(save_path, f"{game_name}_score.txt")
        print(f"hello，\n尊贵的VIP😎：{game_name}\n欢迎回来🌍,\n四则运算")
        print(f"您的分数：{score}")
        operation, num1, num2, result = random_operation()
        prompt = f"{game_name}，请计算：{num1} {operation} {num2} = "
        user_answer = get_user_answer(prompt)
        score = check(result, user_answer, score)
        print(f"当前分数：{score}")
        save_score_to_file(score, game_name,save_path)
        play_again = input("是否继续游戏？输入Y继续，任意键结束:")
        if play_again.lower() != 'y':
            print(f"游戏结束，最终得分为：{score}")
            action = False
            break