from typing import Any, List, Union
from typing import Union
import math
import os
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import matplotlib.pyplot as plt

# pip install matplotlib -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

#git commit -m "первая лаборатерная работа"




class Aircraft:
    """
    Класс описывает парамерты летательного аппарата при полёте по определённому закону
    """

    def __init__(
            self,
    ) -> None:
        """

        """
        # берём данные из эксель таблицы
        self.df = pd.read_excel('1_data.xlsx', sheet_name='Лист1')
        # настройка индекса
        self.df.set_index('name', inplace=True)

        # инициализация основных параметров
        # дальность полёта, м
        self.x_c = self.gl('x_0')
        # высота полёта, м
        self.y_c = self.gl('y_0')
        # скорость полёта, м/с
        self.v = self.gl('V_d')
        # тангаж, радианы
        self.tetha = self.gl('tetha_n')
        # скорость звука (для первого шага)
        self._a = 0.01
        # мах (для первого шага)
        self.m = 0.01
        # коэффициент лобового сопротивления (для первого шага)
        self.c_x = 0.01
        # давление на уровне моря
        self.p = self.gl('p_0')
        # плотность воздуха на уровне моря
        self.ro = self.gl('ro_0')
        # время отсчёта -> время схода с направляющих
        self.t = self.gl('t_d')
        # шаг интергрирования, с
        self.h = 0.1
        # отметка активного участка (True -> активный)
        self.flag = True
        # количество уравнений движения
        self.n = 4
        # матрица для вывода данных
        self.var_list = [
        ]

    def equals(
            self
    ) -> list[float]:
        """
        Уравнения движения
        :return: [dx/dt, dy/dt, dv/dt, dtethe/dt]
        """
        #углы в стартовой систему координат
        sin = math.sin(self.tetha)
        cos = math.cos(self.tetha)
        #активный участок
        if self.flag:
            # масса летательного аппарата
            mass = self.gl('m_0') - self.gl('Q') * self.t
            return [
                self.v * cos, # x
                self.v * sin, # y
                (self.gl('R') - mass * self.gl('g') * sin - self.x) / mass, # v
                -self.gl('g') * cos / self.v # tetha
            ]
        #пассивный участок
        else:
            # масса летательного аппарата
            mass = self.gl('m_0') - self.gl('m_t')
            return [
                self.v * cos, # x
                self.v * sin, # y
                (-mass * self.gl('g') * sin - self.x) / mass, # v
                -self.gl('g') * cos / self.v # tetha
            ]

    def update(
            self,
            value: list[float]
    ) -> None:
        """
        Задание параметрам движения новых значений
        :return: None
        """
        self.x_c, self.y_c, self.v, self.tetha = value

    def runge(
            self
    ) -> None:
        """
        Расчёт траектории по методу Рунге-Кутты
        :return: None
        """
        # задание начальных значений
        self.t = self.gl('t_d')
        self.x_c = self.gl('L_n') * math.cos(self.tetha)
        self.y_c = self.gl('L_n') * math.sin(self.tetha)
        self.v = self.gl('V_d')
        self.tetha = self.gl('tetha_n')

        # матрица значений строки - шаги, столбцы - параметры
        # движения. Задание по типу
        # arr[[y_a],[y_b],[y_c],[y_d]]
        arr = [[
                self.x_c,
                self.y_c,
                self.v,
                self.tetha
        ]] + [[0] * 4] + [[0] * 4] + [[0] * 4]

        # пока высота положительна
        while self.y_c > 0:
            # сброс флага при пассивном участке
            if self.t > self.gl('t_a'):
                self.flag = False

            # расчёт точки
            q_a = self.equals()
            for j in range(self.n):
                arr[1][j] = arr[0][j] + q_a[j] * self.h / 2

            # расчёт точки
            self.t += self.h / 2
            self.update(arr[1])
            q_b = self.equals()
            for j in range(self.n):
                arr[2][j] = arr[0][j] + q_b[j] * self.h / 2

            # расчёт точки
            self.update(arr[2])
            q_c = self.equals()
            for j in range(self.n):
                arr[3][j] = arr[0][j] + q_c[j] * self.h

            # расчёт точки
            self.t += self.h / 2
            self.update(arr[3])
            q_d = self.equals()

            # задание приращения
            delta_y = [0] * self.n
            for j in range(self.n):
                delta_y[j] = (self.h / 6) * (q_a[j] + 2 * (q_b[j] + q_c[j]) + q_d[j])
                # обновление первой строки матрицы (начальные значения для следующего шага)
                arr[0][j] += delta_y[j]
            # ввод данных в матрицу траектории
            self.var_list.append([self.t] + arr[0])

            # обновление параметров движения
            self.update(arr[0])

        #вывод графика
        # self.plot(self.var_list)





    def plot(
            self,
            value: list[float]
    ) -> None:
        """
        Метод вывода данных на экран
        :param value: список, разные столбцы параметры движения
        :return:
        """
        # задание размеров графиков
        plt.figure(figsize=(7, 8))
        # строки
        a = 2
        # ряды
        b = 3
        # numpy для перевоа в векторы
        matrix = np.array(value)
        # время
        t = matrix[:, 0]
        # дальность
        x = matrix[:, 1]
        # высота
        y = matrix[:, 2]
        # скорость
        v = matrix[:, 3]
        # угол
        tetha = matrix[:, 4]

        plt.subplot(a, b, 1)
        plt.plot(x, y)
        plt.title("Координата х")
        plt.xlabel('x')
        plt.ylabel('y')

        plt.subplot(a, b, 2)
        plt.plot(t, v)
        plt.title("Скорость")
        plt.xlabel('t')
        plt.ylabel('v')

        plt.subplot(a, b, 3)
        plt.plot(t, tetha)
        plt.title("Угол")
        plt.xlabel('t')
        plt.ylabel('tetha')

        # задание отступов
        plt.subplots_adjust(wspace=0.8, hspace=0.5)
        # вывод графика
        plt.show()

    def gl(
        self,
        name: str
    ) -> Any:
        """
        Выводит преобразованные значения из exel файла по имени
        :param name: имя переменной, как в файле exel
        :return: преобразованное значение
        """
        return float(self.df.loc[name]['value'])

    @property
    def x(self) -> float:
        """
        :return: Сила лобового сопротивления
        """
        return (self.c_x * self.ro * self.gl('S') * self.v ** 2) / 2

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def ro(self) -> float:
        """
        :return: Плотность, зависящую от высоты полёта
        """
        return self.gl('ro_0') * math.exp(-self.y_c / 10000)

    @ro.setter
    def ro(self, value):
        self._ro = value

    @property
    def p(self) -> float:
        """
        :return: Давление, зависящее от высоты полёта
        """
        return self.gl('p_0') * math.exp((-self.gl('miu')*self.gl('g')*self.y_c) /
                                         (self.gl('R_t')*self.gl('T')))

    @p.setter
    def p(self, value):
        self._p = value

    @property
    def a(self) -> float:
        return math.sqrt(self.gl('gamma') * self.p / self.ro)


    @a.setter
    def a(self, value):
        self._a = value

    @property
    def m(self) -> float:
        """
        :return: Значение числа Маха
        """
        return self.v / self.a

    @m.setter
    def m(self, value):
        self._m = value

    @property
    def c_x(self) -> float:
        """
        :return: Значение лобового сопротивления по формуле Демога
        """
        if self.m < 0.73:
            return 0.157
        elif self.m < 0.82:
            return 0.033 * self.m + 0.133
        elif self.m < 0.91:
            return 0.161 + 3.9 * ((self.m - 0.823) ** 2)
        elif self.m < 1:
            return 1.5 * self.m - 1.176
        elif self.m < 1.18:
            return 0.384 - 1.6 * ((self.m - 1.176) ** 2)
        elif self.m < 1.62:
            return 0.384 * math.sin(1.85 / self.m)
        elif self.m < 3.06:
            return 0.29 / self.m + 0.172
        elif self.m < 3.53:
            return 0.316 - 0.016 * self.m
        else:
            return 0.259

    @c_x.setter
    def c_x(self, value):
        self._c_x = value



def to_radian(value:float) -> float:
    """
    :param value: Значение в градусах
    :return: Значение в радианах
    """
    return round(value * math.pi / 180, 7)


def to_degree(value:float) -> float:
    """
    :param value: Значение в радианах
    :return: Значение в градусах
    """
    return round(value * 180 / math.pi, 7)


def search(a, b, h, n=1):
    """
    Поиск наибольшей дальность при изменении угла наклона
    :param a: нижняя граница
    :param b: верхняя граница
    :param h: шаг поиска
    :return: угол схода с направляющих
    """
    # начальные параметры
    # дальность
    val_max = 0
    #угол
    tetha_max = 0

    # при трёх уточнениях прекратить
    if n >= 3:
        return tetha_max

    # организация шага
    i = a
    while i < b:
        t = Aircraft()
        t.tetha = i
        t.runge()
        # последний шаг интегрирования и параметр дальности
        val = t.var_list[-1][1]
        if val > val_max:
            val_max = val
            tetha_max = i
        i += h
        #удаление экземпляра класса
        del t

    # вывод
    print(to_degree(tetha_max), " при шаге ", to_degree(h))
    search(tetha_max - h, tetha_max + h, h / 10, n + 1)

# начальные параметры
low = 10
high = 80
step = 10

# вывод
print("Самое лучшее: ", to_degree(search(a = to_radian(low), b = to_radian(high), h = to_radian(step)), 'метров'))


