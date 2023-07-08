from modules import tasks
from modules import sorter
from threading import Thread
import pyautogui as pag
import keyboard
import os
import time


TASK_RECOGNITION_DIR = os.path.abspath("assets\\task-recognition")

# append all images from directory to a list
tasks_images = [
    os.path.join(TASK_RECOGNITION_DIR, filename)
    for filename in os.listdir(TASK_RECOGNITION_DIR)
]

tasks_images = sorter(tasks_images)

tasks_repr: dict = {
    tasks_images[0]: tasks.upload_download,
    tasks_images[1]: tasks.upload_download,
    tasks_images[2]: tasks.empty_garbage,
    tasks_images[3]: tasks.stabilize_steering,
    tasks_images[4]: tasks.fuel_engines,
    tasks_images[5]: tasks.admin_swipe,
    tasks_images[6]: tasks.diverted_power_electrical,
    tasks_images[7]: tasks.divert_power,
    tasks_images[8]: tasks.fix_wiring,
    tasks_images[9]: tasks.prime_shields,
    tasks_images[10]: tasks.start_reactor,
    tasks_images[11]: tasks.unlock_manifold,
    tasks_images[12]: tasks.clear_asteroids,
    tasks_images[13]: tasks.clean_vent,
    tasks_images[14]: tasks.calibrate_distributior,
    tasks_images[15]: tasks.chart_course,
    tasks_images[16]: tasks.inspect_sample,
    tasks_images[17]: tasks.clean_filter,
    tasks_images[18]: tasks.scan,
    tasks_images[19]: tasks.align_engine,
}


def main():
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("e"):
            time.sleep(0.5)
            for img in tasks_images:
                if pag.locateOnScreen(img, grayscale=True, confidence=0.8):
                    print(img.split("\\")[-1])
                    print(tasks_repr[img])
                    tasks_repr[img]()
                    break


if __name__ == "__main__":
    main()
