import tkinter as tk

class calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # 创建文本框用于显示用户输入内容
        self.Entry = tk.Entry(root, width=30)
        # Tkinter公开的几何管理类：包（pack）、网格（grid）、位置（place），好像差不多
        self.Entry.grid(row=0, column=0, columnspan=4)

        # 创建operator buttons
        # tk button控件，参数首先是tk object，然后是显示的文本，然后是绑定的函数
        operators = ["+","-","*","/"]
        for i in range(len(operators)):
            # 这里如果不用lambda，而是直接command=self.Click(operators[i])，会不起作用，推测为调用需要传参的函数要使用lambda
            self.operator = tk.Button(root, text=operators[i], command=lambda i=i: self.Click(operators[i]))
            self.operator.grid(row=i+1, column=4)
        
        # 创建数字表
        for i in range(9):
            self.num_button = tk.Button(root, text=str(i+1), command=lambda i=i: self.Click(i+1))
            # 第一行是7，8，9
            # 第二行是4，5，6
            # 第三行是1，2，3
            self.num_button.grid(row=3-i//3, column=i%3)
        # 添加0
        self.zero = tk.Button(root, text="0", command=lambda i=i: self.Click(0))
        self.zero.grid(row=4, column=1)

        # 创建clear button
        self.clear = tk.Button(root, text="C", command=self.Clear)
        self.clear.grid(row=4, column=0)

        # 创建等于，点击等于后计算公式输出结果
        self.equal = tk.Button(root, text="=", command=self.Equal)
        self.equal.grid(row=6, column=4)

        # 运行后先清屏
        self.Clear()

    def Click(self, input):
        # 获取当前文本框内的内容
        current = self.Entry.get()
        # 删除当前显示
        self.Entry.delete(0, tk.END)
        # 合并后重新显示
        self.Entry.insert(0, str(current) + str(input))

    def Clear(self):
        self.Entry.delete(0, tk.END)

    def Equal(self):
        expression = self.Entry.get()
        try:
            # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
            res = eval(expression)
            self.Entry.delete(0, tk.END)
            self.Entry.insert(0, str(res))
        except:
            self.Entry.delete(0, tk.END)
            self.Entry.insert(0, "Error")

    def add(x,y):
        return x + y
    
    def sub(x,y):
        return x - y
    
    def divide(x,y):
        return x / y
    
    def multiple(x,y):
        return x * y

if __name__ == "__main__":
    root = tk.Tk()
    editor = calculator(root)
    root.mainloop()