#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def repair(self):
        self.condition = "Like New"

    def __str__(self):
        return f"Shoe: {self.brand}, Size: {self.size}, Condition: {self.condition}"
