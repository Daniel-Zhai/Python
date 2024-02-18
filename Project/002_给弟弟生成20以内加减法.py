# 生成20以内加减法数学题
import random
import openpyxl
import os

operators = ["-",  "+"]
dir = "D:/资料/学习/计算机/Python/Python/Project/算术题.xlsx"
res = []

# 打印一页26行4列，打印10页，很神奇的多了20个
for i in range(26*4*10 - 20):
    # 生成x,y
    x = random.randint(0,20)
    y = random.randint(0,20)

    # 避免出现结果为负数的情况
    if x < y:
        x, y = y, x

    # 加减交替
    if i % 2 == 0:
        operator = operators[0]
    else:
        operator = operators[1]
    
    element = str(x).rjust(2) + ' ' + operator + ' ' + str(y).ljust(2) + ' ='.ljust(12) # ljust和rjust用于字符串对齐，参数为占位数
    
    res.append(element)

# 使用openpyxl模块操作excel
if os.path.exists(dir):
    # 若存在则加载
    file = openpyxl.load_workbook(dir)
else:
    # 不存在创建excel
    file = openpyxl.Workbook()

# 获取活动表
sheet = file.active
# 生成四列
cols = ['A', 'B', 'C', 'D']

for i in range(len(res)):
    # 获取单元格ID，格式为列+行 如 ‘A1’
    block_id = cols[i%len(cols)-1] + str(2 * (i//len(cols)) + 1) # 四列，行起始为1，间隔一行；//操作符可得整数，/会带一位小数，当然也可以通过其它方法去掉
    sheet[block_id] = res[i] # 填充单元格

# 保存excel
file.save(dir)