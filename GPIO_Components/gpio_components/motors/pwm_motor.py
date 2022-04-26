#!/usr/bin/python
# -*- coding: utf-8 -*-

class PWMMotor(object):
    def __init__(self, pin_pwm, pin_direction, reverse_default_rotation=False):
        self.pin_pwm = pin_pwm
        self.pin_direction = pin_direction
        self.direction = reverse_default_rotation
    
    
    def start(self):
        return
    
    
    def stop(self):
        return
    
    
    def reverse_direction(self):
        self.direction = not self.direction
