import pyautogui as pag
import time
import win32api, win32con
import random
import os


DEFAULT_DIR = os.getcwd()
MANIFOLD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "assets\\Unlock-manifold")
)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def upload_download():
    pag.moveTo(975, 689, 0.1)
    click()


def empty_garbage():
    pag.moveTo(1281, 448, 0.1)
    pag.mouseDown()
    pag.moveTo(1281, 823, 0.2)
    time.sleep(1.5)
    pag.mouseUp()


def stabilize_steering():
    pag.moveTo(967, 569, 0.1)
    click()


def fuel_engines():
    pag.moveTo(1473, 908, 0.2)
    pag.mouseDown()
    time.sleep(3.5)
    pag.mouseUp()


def divert_power():
    pag.moveTo(968, 570, 0.2)
    click()


def admin_swipe():
    pag.moveTo(774, 842, 0.25)
    click()
    time.sleep(0.5)
    pag.moveTo(565, 438, 0.1)
    pag.drag(900, 0, 1.2, button="left")


def diverted_power_electrical():
    switches = [
        (621, 800),
        (711, 801),
        (808, 800),
        (907, 802),
        (1006, 800),
        (1097, 800),
        (1196, 800),
        (1293, 800),
    ]

    for switch in switches:
        if pag.pixel(switch[0], switch[1])[0] in range(200, 256):
            pag.moveTo(switch[0], switch[1], 0.2)
            pag.drag(0, -150, 0.2, button="left")


def fix_wiring():
    left_wires = [(579, 295), (572, 478), (577, 661), (576, 843)]
    right_wires = [(1364, 296), (1361, 480), (1360, 663), (1356, 842)]

    for lw in left_wires:
        for rw in right_wires:
            if pag.pixel(lw[0], lw[1]) == pag.pixel(rw[0], rw[1]):
                pag.moveTo(lw[0], lw[1], 0.2)
                pag.mouseDown()
                pag.moveTo(rw[0], rw[1], 0.2)
                time.sleep(0.1)
                pag.mouseUp()
                break


def prime_shields():
    shields = [
        (951, 557),
        (955, 356),
        (1154, 432),
        (1153, 627),
        (925, 725),
        (795, 670),
        (801, 490),
    ]

    for shield in shields:
        if pag.pixel(shield[0], shield[1])[0] >= 230:
            win32api.SetCursorPos((shield[0], shield[1]))
            click()
            time.sleep(0.5)


def start_reactor():
    left_squares = [
        (534, 483),
        (665, 485),
        (794, 482),
        (533, 606),
        (662, 611),
        (809, 612),
        (530, 744),
        (665, 746),
        (796, 747),
    ]
    right_squares = [
        (1140, 493),
        (1265, 491),
        (1383, 488),
        (1141, 606),
        (1261, 611),
        (1384, 613),
        (1138, 732),
        (1264, 734),
        (1382, 734),
    ]

    green_led_color = (0, 192, 36)
    green_leds = ((500, 344), (577, 345), (661, 344), (743, 345), (822, 345))

    for i, led in enumerate(green_leds):
        if pag.pixel(led[0], led[1]) == green_led_color:
            stage = i + 1

    pag.press("escape")
    time.sleep(0.2)
    pag.press("e")

    while stage <= 5:
        counter = 0
        activated = list()
        while counter < stage:
            for square in left_squares:
                if pag.pixel(square[0], square[1])[2] == 255:
                    activated.append(square)
                    counter += 1
                    time.sleep(0.2)

        time.sleep(0.5)

        for square in activated:
            i = left_squares.index(square)
            win32api.SetCursorPos(right_squares[i])
            pag.mouseDown()
            time.sleep(0.1)
            pag.mouseUp()

        stage += 1


def unlock_manifold():
    os.chdir(MANIFOLD_DIR)

    numbers = (
        "one.png",
        "two.png",
        "three.png",
        "four.png",
        "five.png",
        "six.png",
        "seven.png",
        "eight.png",
        "nine.png",
        "ten.png",
    )

    cords = []
    for number in numbers:
        while True:
            if pag.locateOnScreen(number, grayscale=True, confidence=0.8):
                region = pag.locateOnScreen(number, grayscale=True, confidence=0.8)
                cords.append((region[0] + region[2] // 2, region[1] + region[3] // 2))
                break

    for cord in cords:
        win32api.SetCursorPos(cord)
        click()
        time.sleep(random.uniform(0.2, 0.3))

    os.chdir(DEFAULT_DIR)


def calibrate_distributior():
    # colors:
    # 1st: 223, 227, 0
    # 2nd: 107, 98, 255
    # 3rd: 52, 249, 255

    tiles = [(1237, 257), (1238, 517), (1236, 779)]
    buttons = [(1239, 335), (1236, 601), (1239, 849)]
    redvalues = (223, 107, 52)

    for i in range(3):
        while True:
            if pag.pixel(tiles[i][0], tiles[i][1])[0] == redvalues[i]:
                win32api.SetCursorPos(buttons[i])
                click()
                break


def clear_asteroids():
    asteroid_color = (21, 112, 76)
    crosshair_color = (0, 73, 55)
    crosshair_start_pos = (969, 560)
    region = (574, 167, 786, 784)

    win32api.SetCursorPos(crosshair_start_pos)
    cursor_pos = pag.position()

    # loop though screenshot area
    while pag.pixel(cursor_pos[0], cursor_pos[1]) == crosshair_color:
        screenshot = pag.screenshot(region=region)
        for x in range(0, screenshot.width, 5):
            for y in range(0, screenshot.height, 5):
                if screenshot.getpixel((x, y)) == asteroid_color:
                    win32api.SetCursorPos((574 + x, 167 + y))
                    click()
                    cursor_pos = pag.position()
                    screenshot = pag.screenshot(region=region)

            screenshot = pag.screenshot(region=region)


def clean_vent():
    region = (630, 252, 702, 595)

    win32api.SetCursorPos((980, 480))
    click()

    time.sleep(1)

    screenshot = pag.screenshot(region=region)
    for x in range(0, screenshot.width, 5):
        for y in range(0, screenshot.height, 5):
            r, g, b = screenshot.getpixel((x, y))

            if g in range(170, 220):
                win32api.SetCursorPos((630 + x, 252 + y))
                click()
                screenshot = pag.screenshot(region=region)
            if g == 255:
                return

        screenshot = pag.screenshot(region=region)


def clean_filter():
    starting_point = (random.randint(720, 730), random.randint(450, 650))
    bg_color = (122, 151, 213)
    leaf_colors = ((206, 149, 55), (174, 43, 5), (57, 77, 19))
    region = (532, 115, 875, 870)

    win32api.SetCursorPos(starting_point)
    cursor_pos = pag.position()

    while pag.pixel(cursor_pos[0], cursor_pos[1]) == bg_color:
        screenshot = pag.screenshot(region=region)
        for x in range(0, screenshot.width, 5):
            for y in range(0, screenshot.height, 5):
                if screenshot.getpixel((x, y)) in leaf_colors:
                    win32api.SetCursorPos((532 + x, 115 + y))
                    pag.mouseDown()
                    pag.moveTo(
                        random.randint(620, 630),
                        random.randint(500, 600),
                        random.uniform(0.8, 1.2),
                    )
                    pag.mouseUp()
                    win32api.SetCursorPos(
                        (random.randint(720, 730), random.randint(450, 650))
                    )
                    cursor_pos = pag.position()
                    screenshot = pag.screenshot(region=region)
            screenshot = pag.screenshot(region=region)


def inspect_sample():
    samples = ((750, 510), (859, 510), (970, 510), (1002, 510), (1193, 510))
    red_value = 189
    btn = (1259, 945)

    def choose_sample():
        for sample in samples:
            x = sample[0]
            if pag.pixel(sample[0], sample[1])[0] == 255:
                win32api.SetCursorPos((x, 860))
                click()

    if pag.pixel(btn[0], btn[1])[0] != red_value:
        win32api.SetCursorPos((1259, 945))
        click()
        time.sleep(62)
        choose_sample()
    else:
        choose_sample()


def align_engine():
    arrow_color = (205, 202, 214)
    region = (1175, 150, 175, 800)

    screenshot = pag.screenshot(region=region)
    for x in range(0, screenshot.width, 5):
        for y in range(0, screenshot.height, 5):
            if screenshot.getpixel((x, y)) == arrow_color:
                win32api.SetCursorPos((1175 + x, 150 + y))
                pag.mouseDown()
                pag.moveTo(1255, 558, 0.2)
                pag.mouseUp()
                return


def chart_course():
    # task area
    region = (486, 290, 964, 537)

    # locate ship
    ship_color = (13, 111, 172)
    area = pag.screenshot(region=region)

    def locate_ship():
        for x in range(0, area.width, 5):
            for y in range(0, area.height, 5):
                if area.getpixel((x, y)) == ship_color:
                    return (486 + x, 290 + y)

    win32api.SetCursorPos(locate_ship())


def scan():
    time.sleep(9)
