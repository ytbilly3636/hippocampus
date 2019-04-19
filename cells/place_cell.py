# -*- coding:utf-8 -*-

import sys
import numpy as np


class PlaceCell(object):
    def __init__(self, size=(10, 10)):
        if not len(size) == 2:
            sys.exit('size must be 2-dim tuple')

        self._size = size
        self._status = np.zeros(size, dtype=np.float32)

    def __call__(self, position, var=1.0):
        if not len(position) == 2:
            sys.exit('position must be 2-dim tuple')
        
        # saturation
        sat_position = [position[0], position[1]]
        if position[0] < 0:
            sat_position[0] = 0
        elif position[0] >= self._size[0]:
            sat_position[0] = self._size[0] - 1
        if position[1] < 0:
            sat_position[1] = 0
        elif position[1] >= self._size[1]:
            sat_position[1] = self._size[1] - 1

        # gaussian
        indices = np.arange(self._size[0]*self._size[1]).reshape(self._size[0], self._size[1])
        y = indices // self._size[1]
        x = indices %  self._size[1]
        dy = np.abs(y - sat_position[0])
        dx = np.abs(x - sat_position[1])
        self._status = np.exp(-(dy**2 + dx**2) / (var**2*2))

        return self._status


if __name__ == '__main__':
    pcell = PlaceCell()
    pcell((5, 5))

    import cv2

    img = cv2.resize(pcell._status, (300, 300), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('window', pcell._status)
    cv2.waitKey(0)