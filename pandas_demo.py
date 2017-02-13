#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/13 11:02
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : pandas_demo.py
# @Software: PyCharm Community Edition


# pandas库学习笔记


import pandas as pd

def demo_01():
    '''
    数据读取与显示
    :return:
    '''

    # csv数据读取
    food_info = pd.read_csv("food_info.csv")
    print(type(food_info))
    # 数据前5行
    print(food_info.head())
    # 数据前3行
    print(food_info.head(3))
    # 数据的列名
    print(food_info.columns)
    # 数据的形状（尺寸）
    print(food_info.shape)
    # 查看数据每一列对应的数据类型
    print(food_info.dtypes) # object类型对应str类型

    # 查看数据某些行
    print(food_info.loc[0]) # 查看数据第1行（index=0）
    print(food_info.loc[3:6]) # 查看数据第3,4,5,6行
    print(food_info.loc[[2,5,10]]) # 查看数据第2,5,10行

    # 查看数据某些列
    print(food_info["NDB_No"]) # 查看数据NDB_No列
    print(food_info[["Shrt_Desc","Energ_Kcal"]]) # 查看数据"Shrt_Desc","Energ_Kcal"列


    # 获取所有以g（克）为单位的数据
    col_names = food_info.columns.tolist() # 数据列名，转换为list类型
    print(col_names)
    gram_columns = [] # 克为单位的列名list
    # 筛选以克(g)为单位的列名
    for item in col_names:
        if item.endswith("(g)"):
            gram_columns.append(item)
    gram_data = food_info[gram_columns] # 查看数据gram_columns（list）中的列
    print(gram_data.head(3)) # 查看前3行


def demo_02():
    '''
    数据计算与排序
    :return:
    '''
    # csv数据读取
    food_info = pd.read_csv("food_info.csv")

    # 对某列数据加减乘除操作
    print(food_info["Iron_(mg)"])
    div_1000 = food_info["Iron_(mg)"] / 1000
    print(div_1000)
    add_100 = food_info["Iron_(mg)"] + 100
    print(add_100)
    sub_100 = food_info["Iron_(mg)"] - 100
    print(sub_100)
    mult_2 = food_info["Iron_(mg)"] * 2
    print(mult_2)

    # 保存计算好的新列（列名：Iron_(g)）
    food_info["Iron_(g)"] = div_1000
    print(food_info["Iron_(g)"])

    # 两列数据对应加减乘除
    water_energy_add = 2 * food_info["Water_(g)"] + food_info["Energ_Kcal"] / 0.75
    print(water_energy_add)
    water_energy_sub = 2 * food_info["Water_(g)"] - food_info["Energ_Kcal"] + 20
    print(water_energy_sub)
    water_energy_mult = food_info["Water_(g)"] * food_info["Energ_Kcal"]
    print(water_energy_mult)
    water_energy_div = food_info["Water_(g)"] / food_info["Energ_Kcal"]
    print(water_energy_div)

    # 某列数据归一化（归一化的一种）并保存
    food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
    print(food_info["Normalized_Protein"])

    # 数据排序
    print(food_info["Sodium_(mg)"])
    # 按某列列值排序，ascending=False降序排列，默认为升序，inplace=True覆盖原dataFrame
    food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
    print(food_info["Sodium_(mg)"])





if __name__ == "__main__":
    # demo_01()
    demo_02()