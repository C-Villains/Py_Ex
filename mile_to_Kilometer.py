import tkinter as tk




window = tk.Tk()
window.title("Mile To Km")
window.minsize(width=300,height=200)
window.resizable(False,False)
window.config(padx=50,pady=50)


def m_to_k():
    mile = float(input.get())
    km = round(mile * 1.609)
    value_label.config(text=f"{mile}")


def k_to_m():
    km = float(input.get())
    mile = round(km / 0.62)
    value_label2.config(text=f"{mile}")
    
button = tk.Button(text="킬로미터 계산",command=m_to_k)
button.grid(row=6,column=1)

button = tk.Button(text="마일 계산",command=k_to_m)
button.grid(row=7,column=1)

input = tk.Entry(width=10)
input.grid(row=2,column=1)


input_num =tk.Label(text="변환할 값")
input_num.grid(row=2,column=0) 








is_equal_to_label = tk.Label(text="결과1")
is_equal_to_label.grid(row=4,column=0)

miles_label = tk.Label(text="킬로미터")
miles_label.grid(row=4,column=2)


is_equal_to_label2 = tk.Label(text="결과2")
is_equal_to_label2.grid(row=5,column=0)


km_label = tk.Label(text="마일")
km_label.grid(row=5,column=2)

value_label = tk.Label(text=0)
value_label.grid(row=4,column=1)

value_label2 = tk.Label(text=0)
value_label2.grid(row=5,column=1)


window.mainloop()
