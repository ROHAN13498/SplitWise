import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk

tot_exp = []
cur_balance = []
members = []
description = []
s_b = []
s_f = []
money = []
final_balance = pd.Series(members)

win = Tk()
win.geometry("750x250")
Label(win, text="Split Generated", font=('Helvetica 17 bold')).pack(pady=30)


def open_win():
    global tot_exp
    global members
    global final_balance
    y = np.array(tot_exp)
    mylabels = members
    plt.pie(y, labels=mylabels, shadow=True)
    plt.legend(title="Total Expenditure:")
    plt.show()


def open_win1():
    xbar = np.array(members)
    ybar = np.array(tot_exp)
    plt.bar(xbar, ybar, width=0.1)
    plt.show()


def open_win3():
    for i in range(len(members)):
        xpoints = np.array([x for x in range(len(cur_balance[i]))])
        ypoints = np.array(cur_balance[i])
        plt.plot(xpoints, ypoints, label=members[i])
    plt.legend()
    plt.show()


def open_win2():
    new = Toplevel(win)
    new.geometry("750x250")
    new.title("SPLIT GENERATED")
    global tot_exp
    global members
    global final_balance
    pos_pointer = 0
    neg_pointer = 0
    i = 1
    while (pos_pointer < len(members) and neg_pointer < len(members)):
        while final_balance[pos_pointer] < 0:
            pos_pointer = pos_pointer + 1
            if pos_pointer == len(members):
                break
        while final_balance[neg_pointer] > 0:
            neg_pointer = neg_pointer + 1
            if neg_pointer == len(members):
                break
        if abs(final_balance[neg_pointer]) - final_balance[pos_pointer] >= 0:
            Label(
                new,
                text=f"{i}.{members[neg_pointer]} owes {members[pos_pointer]} an amount of {final_balance[pos_pointer]}",
                font=("Helvetica 17 bold"),
            ).pack(pady=30)
            final_balance[neg_pointer] += final_balance[pos_pointer]
            final_balance[pos_pointer] = 0
            pos_pointer = pos_pointer + 1
            if pos_pointer == len(members):
                break
        if abs(final_balance[neg_pointer]) - final_balance[pos_pointer] < 0:
            Label(
                new,
                text=f"{i}.{members[neg_pointer]} owes {members[pos_pointer]} an amount of rupees {abs(final_balance[neg_pointer])}",
                font=("Helvetica 17 bold"),
            ).pack(pady=30)
            final_balance[pos_pointer] += final_balance[neg_pointer]
            final_balance[neg_pointer] = 0
            neg_pointer = neg_pointer + 1
            if neg_pointer == len(members):
                break
        if final_balance[neg_pointer] == 0 and final_balance[pos_pointer] == 0:
            break
        i = i + 1


def add_member():
    global tot_exp
    global members
    global final_balance
    new_member = [0]
    cur_balance.append(new_member)
    tot_exp.append(0)
    print("Name:", end="")
    members.append(input())
    print("-" * 40)
    add_member = pd.Series([0])
    final_balance = pd.concat([final_balance, add_member], ignore_index=True)


def add_expense():
    global tot_exp
    global members
    global s_b
    global s_f
    global description
    global final_balance
    global money
    desc = input("Description:")
    description.append(desc)
    print("-" * 40)
    money_spent = int(input("Money_spent:"))
    money.append(money_spent)
    print("-" * 40)
    print("Spent By")
    mem = pd.Series(members)
    for i, r in mem.items():
        print(i + 1, r)
    print("-" * 40)
    spent_by = int(input())
    s_b.append(members[spent_by - 1])
    print("-" * 40)
    print("For:")
    for i, r in mem.items():
        print(i + 1, r)
    print("-" * 40)
    for_array = list(map(int, input().split()))
    row = []
    for i in for_array:
        row.append(members[i - 1])
    s_f.append(row)
    print("-" * 40)
    tot_exp[spent_by - 1] += money_spent
    final_balance[spent_by - 1] += money_spent
    quotient = money_spent / len(for_array)
    for i in for_array:
        final_balance[i - 1] -= quotient
    for i in range(len(members)):
        print(members[i], " ", final_balance[i])
    print("-" * 40)
    for i in range(len(members)):
        cur_balance[i].append(final_balance[i])


def excel():
    global s_b
    global s_f
    global description
    global money
    df = pd.DataFrame(
        list(zip(description, s_b, s_f, money)),
        columns=["description", "spent by", "spent for", "money spent"],
    )
    df.to_excel(
        r"C:\Users\vaj_2\OneDrive\Desktop\pp project\excel_data\expenditures.xlsx",
        index=False,
    )  # here u should mention the path where u want to store the excel file


def settle_up():
    global tot_exp
    global members
    global final_balance
    global s_b
    global s_f
    global description
    global money
    global win
    ttk.Button(win, text="Pie Chart", command=open_win).pack()
    ttk.Button(win, text="Bar Graph", command=open_win1).pack()
    ttk.Button(win, text="Suggested Payments", command=open_win2).pack()
    ttk.Button(win, text="Expenditure Graph", command=open_win3).pack()
    win.mainloop()
    return


while True:
    flag = 0
    initial_choice = 0
    while flag == 0:
        print("1.Add member")
        print("2.Add expense")
        print("3.Settle up")
        print("4.Expenditures sheet")
        print("-" * 40)
        initial_choice = int(input())
        print("-" * 40)
        if initial_choice != 1 and initial_choice != 2 and initial_choice != 3:
            print("Press the valid option")
        else:
            flag = 1
    if initial_choice == 1:
        add_member()
    if initial_choice == 2:
        add_expense()
    if initial_choice == 3:
        settle_up()
    if initial_choice == 4:
        excel()
