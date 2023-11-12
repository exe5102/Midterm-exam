total = 0
dict = {}
list = []
Line = "----------------------------"
Endline = "============================"

# 置中對齊
print(f"{Line}\n{"員工薪資輸入":^19}\n{"若姓名處未輸入則代表結束":^16}\n{Line}")

while True:
    eName = input("請輸入姓名:")  # 姓名輸入
    if eName == "":  # 若未輸入，跳出迴圈
        break
    eSalary = int(input("請輸入薪資:"))  # 薪資輸入
    total += eSalary  # 總額計算
    print()  # 換行
    dict.setdefault(eName, eSalary)  # 新增資料到字典
list.append(dict)  # 儲存成list
print(Line)

# 叫出字典每筆資料和對應的值
for key in dict:
    data = "{:,}".format(dict[key])  # 格式化處理將每千位元插入逗號
    print(f"員工{key:<6}的薪資為{data:>7}")  # 員工名字向左對齊為6，薪資向右對齊寬度為7

total_data = "{:,}".format(total)  # 格式化處理將每千位元插入逗號
print(f"{Line}\n合計薪資： {total_data:>13}")  # 向右對齊寬度為13


if len(dict) > 0:  # 有無資料判斷
    average_salary = total / len(dict)  # 平均計算
    print(f"平均薪資： {average_salary:>16.2f}\n{Endline}")  # 列印文字向右對齊寬度為16取小數點後2位
else:
    print(f"平均薪資： {"0.00":>16}")  # 列印文字向右對齊寬度為16取小數點後2位
