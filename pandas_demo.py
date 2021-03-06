#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/13 11:02
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : pandas_demo.py
# @Software: PyCharm Community Edition


# pandas库学习笔记


import pandas as pd
import numpy as np

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

    # 查看数据集的某一行某一列
    print(food_info.loc[3,"Shrt_Desc"])

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
    food_info_01 = food_info.reset_index(drop=True) # 重置排序索引
    print(food_info_01)


def demo_03():
    '''
    数据预处理
    :return:
    '''

    # 读取数据（泰坦尼克号乘客信息）
    titanic_survival = pd.read_csv("titanic_train.csv")
    print(titanic_survival.head())

    # 缺失值处理
    age = titanic_survival["Age"] # 获取Age列数据
    print(age.loc[0:10]) # 查看前10行数据
    age_is_null = pd.isnull(age) # 获得Age列数据是否为空的数组
    print(age_is_null)
    age_null_true = age[age_is_null] # 查看Age列对应为空的数据
    print(age_null_true)
    age_null_count = len(age_null_true) # 统计Age列数据为空的个数
    print(age_null_count)

    # 取出Age列中不为空的数据(忽略缺失值)
    real_ages = titanic_survival["Age"][age_is_null == False]
    print(real_ages)

    # 求平均年龄
    mean_age = sum(real_ages) / len(real_ages)
    print(mean_age)

    # 对Age列非缺失值（忽略缺失值）进行平均值计算(意义同上)
    correct_mean_age = titanic_survival["Age"].mean()
    print(correct_mean_age)


    # 对不同仓位等级（列名"Pclass"）的票价（列名"Fare"）计算均值
    passenger_class = [1,2,3] # 定义仓位等级
    fares_by_class = {} # 初始化不同仓位票价均值的存储容器——字典类型
    for this_class in passenger_class:
        # 获取符合当前仓位等级的所有数据集
        pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
        pclass_fares = pclass_rows["Fare"] # 获取数据集中的"Fare"列
        fare_for_class = pclass_fares.mean() # 计算"Fare"列中数据均值（自动忽略缺失值）
        fares_by_class[this_class] = fare_for_class # 将计算结果存储在字典中
    print(fares_by_class) # 打印各仓位等级对应的平均票价

    # 对不同仓位等级（列名"Pclass"）的票价（列名"Fare"）计算均值(同上)[aggfunc 默认为 np.mean]
    passenger_class_1 = titanic_survival.pivot_table(index="Pclass", values="Fare", aggfunc=np.mean)
    print(passenger_class_1)

    # 对不同仓位等级（列名"Pclass"）的乘客年龄（列名"Age"）计算均值[aggfunc 默认为 np.mean]
    passenger_age = titanic_survival.pivot_table(index="Pclass", values="Age")
    print(passenger_age)

    # 统计各个仓位等级的乘客的获救率
    # 索引定为"Pclass"列，值为索引对应的"Survived"列的均值
    passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
    print(passenger_survival)

    # 统计各个仓位等级的乘客的获救人数
    # 索引定为"Pclass"列，值为索引对应的"Survived"列的求和
    passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.sum)
    print(passenger_survival)

    # 统计男女的获救人数
    # 索引定为"Sex"列，值为索引对应的"Survived"列的求和
    passenger_survival = titanic_survival.pivot_table(index="Sex", values="Survived", aggfunc=np.sum)
    print(passenger_survival)

    # 统计各个上船地点（列名"Embarked"）票价总额和获救人数
    port_stats = titanic_survival.pivot_table(index="Embarked", values=["Fare", "Survived"], aggfunc=np.sum)
    print(port_stats)

    # 删除含有缺失值的数据行
    drop_na_columns = titanic_survival.dropna(axis=1)
    print(drop_na_columns)

    # 删除"Age", "Sex"列上含有缺失值的行
    new_titanic_survival = titanic_survival.dropna(axis=0, subset=["Age", "Sex"])
    print(new_titanic_survival)

def demo_04():
    '''
    自定义函数
    :return:
    '''

    # 读取数据（泰坦尼克号乘客信息）
    titanic_survival = pd.read_csv("titanic_train.csv")


    def get_100_row(data):
        '''
        取出数据集的第一百条数据
        :param data: 数据集
        :return:
        '''
        item = data.loc[99]
        return item
    print(titanic_survival.apply(get_100_row))


    def not_nul_count(data):
        '''
        统计缺失值数量
        :param data:
        :return:
        '''
        data_null_boolean = pd.isnull(data) # 获得缺失值布尔集
        data_null = data[data_null_boolean] # 获取布尔集为True的数据
        return len(data_null) # 返回数据长度
    print(titanic_survival.apply(not_nul_count)) # 二维数组，显示每列缺失值数量


    def which_class(data):
        '''
        "Pclass"列数据对应显示为其他值
        :param data:
        :return:
        '''
        pclass = data["Pclass"]
        if pd.isnull(pclass):
            return "Unknown"
        elif pclass == 1:
            return "First Class"
        elif pclass == 2:
            return "Second Class"
        elif pclass == 3:
            return "Third Class"
    print(titanic_survival.apply(which_class, axis=1)) # axis=1,按行迭代


def demo_05():
    '''
    pandas库数据结构Series
    :return:
    '''

    # 获取数据
    fandango = pd.read_csv("fandango_score_comparison.csv")
    print(fandango.head())

    # 获取电影名字列数据
    series_film = fandango["FILM"]
    print(series_film.head())

    # 获取电影评分列数据
    series_rt = fandango["RottenTomatoes"]
    print(series_rt.head())

    film_names = series_film.values # 取出电影名字值（一维数组）
    rt_scores = series_rt.values # 取出电影分值（一维数组）

    print(film_names)
    print(rt_scores)

    # 以电影名字为索引，电影分值为值，创建Series
    series_custom = pd.Series(rt_scores, index=film_names)
    print(series_custom)
    # 通过电影名字索引获取电影分值
    print(series_custom[["Cinderella (2015)","Unbroken (2014)"]])
    print(series_custom[5:10]) # 仍然可以通过行号取值

    # 按索引排序
    index = series_custom.index.tolist() # 获取索引列表
    print(index)
    sorted_index = sorted(index) # 排序
    sorted_by_index = series_custom.reindex(sorted_index) # 用排序好的索引列表从新定义索引
    print(sorted_by_index)

    # 按值排序，按索引排序（同上）
    sort_series_01 = series_custom.sort_values()
    sort_series_02 = series_custom.sort_index()
    print(sort_series_01)
    print(sort_series_02)

    # 支持numpy科学计算操作
    print(np.add(series_custom, series_custom))
    print(np.sin(series_custom))
    print(np.max(series_custom))

    # 筛选电影评分大于50的（同numpy数组操作）
    print(series_custom[series_custom > 50])
    # 筛选电影评分大于50小于75的（同numpy数组操作）
    print(series_custom[(series_custom > 50) & (series_custom < 75)])

    # 以电影名字为索引，分别以"RottenTomatoes"和"RottenTomatoes_User"为值，创建两个Series
    rt_critics = pd.Series(fandango["RottenTomatoes"].values, index=fandango["FILM"])
    rt_users = pd.Series(fandango["RottenTomatoes_User"].values, index=fandango["FILM"])
    rt_mean = (rt_critics + rt_users) / 2 # 两个Series进行值操作
    print(rt_mean)


def demo_06():
    '''
    pandas库数据结构DataFrame
    :return:
    '''
    # 获取数据
    fandango = pd.read_csv("fandango_score_comparison.csv")
    print(type(fandango))

    # 指定索引
    data = fandango.set_index("FILM", drop=False) # 指定电影名字为索引，drop=False表示不在值域中把“FILM”删掉
    print(data.index) # 返回一维数组

    # 通过索引取数据
    print(data.loc["Cinderella (2015)"]) # 指定取值
    print(data["Cinderella (2015)":"Unbroken (2014)"]) # 范围取值
    print(data.loc["Cinderella (2015)":"Unbroken (2014)"]) # 范围取值（同上）

    # 取出类型中为float64的数据
    types = data.dtypes
    print(types)
    float64_columns = types[types.values == "float64"]._index # 获得类型为float64的数据的索引
    data_float64 = data[float64_columns] # 获得类型中为float64的数据
    print(data_float64)

    # 求float64数据集中每一列的方差
    print(data_float64.apply(lambda x:np.std(x)))

    # float64数据集中指定列，横向求方差
    data_float64_h = data_float64[["RT_user_norm","Metacritic_user_nom"]]
    print(data_float64_h.apply(lambda x:np.std(x), axis=1))



if __name__ == "__main__":
    # demo_01()
    # demo_02()
    # demo_03()
    # demo_04()
    # demo_05()
    demo_06()