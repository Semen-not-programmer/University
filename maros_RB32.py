import pyautogui
import keyboard
import time
import math


def to_radian(value: float) -> float:
    """
    :param value: Значение в градусах
    :return: Значение в радианах
    """
    return round(value * math.pi / 180, 2)


def br_twin_tandem_rdtt():
    br_twin_tandem_rdtt = [
        [679, 417],
        [940, 418],
        [892, 452],
        [974, 416],
        [888, 500],
        [890, 512],
        [888, 524],
        [889, 538],
        [891, 643],
        [888, 657],
        [889, 669],
        [1081, 563],
        [1082, 645],
        [1080, 657],
        [1082, 668]]
    for xy in br_twin_tandem_rdtt:
        pyautogui.moveTo(xy[0], xy[1])
        pyautogui.leftClick()

def br_solo_tandem_rdtt():
    br_solo_tandem_rdtt = [
        [682, 419],
        [1082, 500],
        [1081, 512],
        [1079, 525],
        [1083, 538],
        [1080, 642],
        [1079, 655],
        [1081, 671],
    ]
    for xy in br_solo_tandem_rdtt:
        pyautogui.moveTo(xy[0], xy[1])
        pyautogui.leftClick()

    next()


    # Окно оптимизации
    for_lab_1 = [
        [873, 470],
        [696, 570],
        [1072, 613],
    ]
    for xy in for_lab_1:
        pyautogui.moveTo(xy[0], xy[1])
        pyautogui.leftClick()
    keyboard.write("13718")

    next()

    # Окно начальных параметров
    #скорость
    move_and_text(1084, 425, str(v))
    #высота
    move_and_text(1078, 460, str(h))
    #угол
    move_and_text(1085, 490, str(tetha))

    next()

    # Окно цели
    # нет цели
    pyautogui.moveTo(681, 386)
    pyautogui.leftClick()

    next()

    # Окно программы АУ
    # по умолчанию
    pyautogui.moveTo(896, 486)
    pyautogui.leftClick()

    next()
    next()

    # Окно конструкционные схемы и материалы

    # головной отсек
    pyautogui.moveTo(763, 370)
    pyautogui.leftClick()
    pyautogui.moveTo(904, 402)
    pyautogui.leftClick()
    # масса ГО
    move_and_text(1350, 372, str(m_go))
    # калибр ГО
    move_and_text(1351, 396, str(D_go))
    # длина ГО
    move_and_text(1347, 417, str(l_go))
    # притупление
    move_and_text(1357, 442, str(x_go))
    accept()

    # устройство отделения
    pyautogui.moveTo(766, 384)
    pyautogui.leftClick()
    param = [
        [1049, 444],
        [1050, 469],
        [1049, 489],
        [1051, 514],
        [1050, 539],
    ]
    pyautogui.moveTo(param[i_param][0], param[i_param][1])
    pyautogui.leftClick()
    accept()

    # параметры ступени
    pyautogui.moveTo(744, 419)
    pyautogui.leftClick()
    # относительная масса топлива
    move_and_text(1216, 460, str(m_t))
    # тяговооруженность
    move_and_text(1220, 481, str(p_))
    # диаметр
    move_and_text(1222, 509, str(D))
    accept()




    # приборы управления
    pyautogui.moveTo(789, 434)
    pyautogui.leftClick()
    move_and_text(1238, 469, str(sko))
    accept()

    # приборный отсек
    pyautogui.moveTo(754, 448)
    pyautogui.leftClick()
    [754, 448]
    po_param = [
        [922, 396],
        [923, 420],
        [921, 442],
    ]
    pyautogui.moveTo(po_param[i_po_param][0], po_param[i_po_param][1])
    pyautogui.leftClick()

    mat_param = [
        [1154, 394],
        [1153, 415],
        [1152, 432],
        [1155, 451],
        [1154, 472],
        [1155, 488],
        [1152, 510],
        [1154, 526],
        [1152, 547],
    ]
    pyautogui.moveTo(mat_param[i_mat_param][0], mat_param[i_mat_param][1])
    pyautogui.leftClick()
    accept()


    # топливо РДТТ
    for_lab_2 = [
            [756, 463],
            [913, 376],
            [914, 554],
        ]
    for xy in for_lab_2:
        pyautogui.moveTo(xy[0], xy[1])
        pyautogui.leftClick()
    accept()

    # РДТТ
    for_lab_2 = [
        [742, 475],
        [913, 386],
    ]
    for xy in for_lab_2:
        pyautogui.moveTo(xy[0], xy[1])
        pyautogui.leftClick()

    move_and_text(1283, 516, str(p_kc))
    move_and_text(1282, 541, str(p_sr))
    accept()

    # хвостовой отсек
    pyautogui.moveTo(771, 499)
    pyautogui.leftClick()
    accept()


def move_and_text(x, y, text):
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()
    for i in range(5):
        pyautogui.press('backspace')
    keyboard.write(text)

def next():
    pyautogui.moveTo(1038, 746)
    pyautogui.leftClick()


def accept():
    pyautogui.moveTo(933, 739)
    pyautogui.leftClick()


# ----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!
# ----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!
# ----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!

# скорость старта
v = 300
# высота старта
h = 5000
# угол старта
tetha = to_radian(0)
# относительная масса топлива
m_t = 0.7
# тяговооруженность
p_ = 3.5
# диаметр
D = 1
# масса ГО
m_go = 590
# калибр ГО
D_go = 1
# длина ГО
l_go = 1.2
# притупление ГО
x_go = 0.2
# тип разделения
i_param = 3
    # 0 - расталкивающий
    # 1 - ускоряющий
    # 2 - тормозящий
    # 3 - противосопла РДТТ
    # 4 - противосопла бака

# среднее квадратичное рассеивание
sko = 200
#конструкция
i_po_param = 0
    # 0 - стрингерная
    # 1 - лонжеронная
    # 2 - шпангоутная
i_mat_param = 1
    # 0 - СП-43
    # 1 - Х18Н9Т
    # 2 - АМг6
    # 3 - Д16Т
    # 4 - ВТ15
    # 5 - стеклопластик
    # 6 - органопластик
    # 7 - углепластик
    # 8 - другой
# давление камеры сгорания
p_kc = 4000000
# давление на срезе
p_sr = 100000


# ----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!
# ----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!
# ----------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!

if __name__ == "__main__":
    X_CURSOR = 0,
    Y_CURSOR = 0
    while True:
        if keyboard.is_pressed('home'):
            # br_twin_tandem_rdtt()
            br_solo_tandem_rdtt()
        if keyboard.is_pressed('scrlk'):
            x, y = pyautogui.position()
            if x != X_CURSOR and y != Y_CURSOR:
                X_CURSOR, Y_CURSOR = x, y
                print([X_CURSOR, Y_CURSOR])