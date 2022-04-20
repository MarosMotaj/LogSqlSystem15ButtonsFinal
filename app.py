#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from led import Led
from lcd_display import LCD
from clock import Clock
from mysql_connection import SQL
from button import Button
from buzzer import Buzzer
import signal
import time


class App:

    def __init__(self, device_name):
        self.device_name = device_name
        self.line_name = None
        self.continue_reading = True
        self.button_login_function = True
        self.button_logoff_function = True
        GPIO.setwarnings(False)
        self.signal = signal.signal(signal.SIGINT, self.end_read)
        #self.MIFAREReader = MFRC522.MFRC522()
        self.sql = SQL("", "", "", "")
        self.lcd = LCD()
        self.green_led = Led(37)
        self.red_led = Led(31)
        self.clock = Clock()
        self.buzzer = Buzzer()
        self.login_button = Button(29)
        self.logoff_button = Button(16)

        self.button_name = None

        self.sql_buttons = self.sql.get_buttons_names()

        self.line_button_1 = Button(40)
        self.line_button_1_name = self.sql_buttons[1][0]

        self.line_button_2 = Button(38)
        self.line_button_2_name = self.sql_buttons[2][0]

        self.line_button_3 = Button(36)
        self.line_button_3_name = self.sql_buttons[3][0]

        self.line_button_4 = Button(32)
        self.line_button_4_name = self.sql_buttons[4][0]

        self.line_button_5 = Button(13)
        self.line_button_5_name = self.sql_buttons[5][0]

        self.line_button_6 = Button(26)
        self.line_button_6_name = self.sql_buttons[6][0]

        self.line_button_7 = Button(12)
        self.line_button_7_name = self.sql_buttons[7][0]

        self.line_button_8 = Button(10)
        self.line_button_8_name = self.sql_buttons[8][0]

        self.line_button_9 = Button(8)
        self.line_button_9_name = self.sql_buttons[9][0]

        self.line_button_10 = Button(35)
        self.line_button_10_name = self.sql_buttons[10][0]

        self.line_button_11 = Button(33)
        self.line_button_11_name = self.sql_buttons[11][0]

        self.line_button_12 = Button(15)
        self.line_button_12_name = self.sql_buttons[12][0]

        self.line_button_13 = Button(7)
        self.line_button_13_name = self.sql_buttons[13][0]

        self.line_button_14 = Button(11)
        self.line_button_14_name = self.sql_buttons[14][0]

        self.date, self.time, self.hour, self.minutes = self.clock.clock_time()

    def end_read(self):
        self.continue_reading = False
        GPIO.cleanup()

    def check_connection_error(self):
        while True:
            try:
                self.sql.connect_to_sql()
                break
            except:
                self.lcd.lcd_print_data("Pokus o pripojenie", 2, 2)
                self.lcd.clear()
                self.green_led.off()
                self.red_led.on()
                time.sleep(2)
                self.red_led.off()
        self.green_led.on()
        self.lcd.lcd_print_data("    Vyber linku", 0, 2)

    def check_if_somebody_is_logged(self, button_name):
        self.sql.connect_to_sql()
        self.line_name = self.sql.get_line_name(button_name)
        tag_to, ops_id, tag_since = self.sql.sql_check_if_somebody_is_logged(self.line_name)
        self.lcd.lcd_print_data(f"{self.date}       {self.device_name}", 0, 1)
        self.lcd.lcd_print_data(f"              {self.line_name}", 0, 2)
        self.lcd.lcd_print_data(f"AC:{ops_id}", 0, 3)
        self.lcd.lcd_print_data(f"FROM: {str(tag_since)[11:16]}  "
                                f"{str(tag_since)[2:4]}."
                                f"{str(tag_since)[8:11].strip()}.", 0, 4)
        self.sql.mysql_database.close()

    def line_button_pressed(self):
        while True:
            try:
                if self.line_button_1.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_1_name)
                    self.check_if_somebody_is_logged(self.line_button_1_name)
                    self.button_name = self.line_button_1_name
                    break

                if self.line_button_2.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_2_name)
                    self.check_if_somebody_is_logged(self.line_button_2_name)
                    self.button_name = self.line_button_2_name
                    break

                if self.line_button_3.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_3_name)
                    self.check_if_somebody_is_logged(self.line_button_3_name)
                    self.button_name = self.line_button_3_name
                    break

                if self.line_button_4.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_4_name)
                    self.check_if_somebody_is_logged(self.line_button_4_name)
                    self.button_name = self.line_button_4_name
                    break

                if self.line_button_5.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_5_name)
                    self.check_if_somebody_is_logged(self.line_button_5_name)
                    self.button_name = self.line_button_5_name
                    break

                if self.line_button_6.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_6_name)
                    self.check_if_somebody_is_logged(self.line_button_6_name)
                    self.button_name = self.line_button_6_name
                    break

                if self.line_button_7.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_7_name)
                    self.check_if_somebody_is_logged(self.line_button_7_name)
                    self.button_name = self.line_button_7_name
                    break

                if self.line_button_8.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_8_name)
                    self.check_if_somebody_is_logged(self.line_button_8_name)
                    self.button_name = self.line_button_8_name
                    break

                if self.line_button_9.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_9_name)
                    self.check_if_somebody_is_logged(self.line_button_9_name)
                    self.button_name = self.line_button_9_name
                    break

                if self.line_button_10.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_10_name)
                    self.check_if_somebody_is_logged(self.line_button_10_name)
                    self.button_name = self.line_button_10_name
                    break

                if self.line_button_11.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_11_name)
                    self.check_if_somebody_is_logged(self.line_button_11_name)
                    self.button_name = self.line_button_11_name
                    break

                if self.line_button_12.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_12_name)
                    self.check_if_somebody_is_logged(self.line_button_12_name)
                    self.button_name = self.line_button_12_name
                    break

                if self.line_button_13.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_13_name)
                    self.check_if_somebody_is_logged(self.line_button_13_name)
                    self.button_name = self.line_button_13_name
                    break

                if self.line_button_14.button_callback() is True:
                    self.line_name = self.sql.get_line_name(self.line_button_14_name)
                    self.check_if_somebody_is_logged(self.line_button_14_name)
                    self.button_name = self.line_button_14_name
                    break

            except Exception as e:
                print(e)
                self.check_connection_error()

    def run(self):
        self.check_connection_error()
        self.lcd.lcd_print_data("    Vyber linku", 0, 2)

        while True:
            self.line_button_pressed()

            abort_after = 4
            start = time.time()
            
            self.MIFAREReader = MFRC522.MFRC522()

            while self.continue_reading:
                print("priloz kartu")

                run_time = time.time() - start
                if run_time >= abort_after:
                    self.lcd.clear()
                    self.run()

                # Skenuj karty
                (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)

                # Ak sa nasla karta
                if status == self.MIFAREReader.MI_OK:
                    print("Karta bola detekovana")

                # Get the UID of the card
                (status, uid) = self.MIFAREReader.MFRC522_Anticoll()

                # Ak mas UID tak pokracuj
                if status == self.MIFAREReader.MI_OK:
                    self.lcd.clear()
                    try:
                        detected_chip_number = str(uid[0]) + "-" + str(uid[1]) + "-" + str(uid[2]) + "-" + str(
                            uid[3]) + "-" + str(uid[4])
                        if self.sql.check_chip_number(detected_chip_number)[1] is False:
                            self.lcd.lcd_print_data("Karta nerozpoznana", 0, 2)
                            self.lcd.lcd_print_data("ID:" + str(uid[0]) + "-" + str(uid[1]) + "-" + str(uid[2]) + "-" + str(
                                uid[3]) + '-' + str(
                                uid[4]), 1, 1)
                            self.buzzer.run_buzzer()
                            self.lcd.clear()
                            self.lcd.lcd_print_data("    Vyber linku", 0, 2)
                            break
                        else:
                            self.lcd.lcd_print_data("ID:" + str(uid[0]) + "-" + str(uid[1]) + "-" + str(uid[2]) + "-" + str(
                                uid[3]) + '-' + str(
                                uid[4]), 0, 1)
                            self.lcd.lcd_print_data("Stlac prichod/odchod", 0, 2)

                            abort_after = 5
                            start = time.time()

                            self.button_login_function = True
                            self.button_logoff_function = True

                            while True:
                                run_time = time.time() - start
                                if run_time >= abort_after:
                                    break

                                if self.login_button.button_callback() and self.button_login_function is True:
                                    print("tlacitko prihlasenie bolo stlacene")
                                    self.sql.login_operator(self.line_name, detected_chip_number)
                                    self.lcd.clear()
                                    self.check_if_somebody_is_logged(self.button_name)
                                    self.buzzer.run_buzzer()
                                    abort_after = 4
                                    start = time.time()
                                    self.button_logoff_function = False

                                if self.logoff_button.button_callback() and self.button_logoff_function is True:
                                    print("Tlacitko odhlasenie bolo stlacene")
                                    try:
                                        self.sql.logoff_operator(self.line_name, detected_chip_number)
                                        self.lcd.clear()
                                    except:
                                        print("Nik neni nalogovany nie je moznost odhlasenia")
                                        self.lcd.clear()
                                    self.check_if_somebody_is_logged(self.button_name)
                                    self.buzzer.run_buzzer()
                                    abort_after = 4
                                    start = time.time()
                                    self.button_login_function = False

                                if self.line_button_1.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_2.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_3.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_4.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_5.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_6.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_7.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_8.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_9.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_10.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_11.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_12.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_13.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()
                                if self.line_button_14.button_callback() is True:
                                    abort_after = 0
                                    start = time.time()

                            # print(self.sql.print_table_data())

                    except Exception as e:
                        print(e)
                        self.check_connection_error()


