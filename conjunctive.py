# -*- coding: utf-8 -*-

import numpy as np
import cv2

from cells import TimeCell, PlaceCell


class HPC(object):
    def __init__(self):
        self.tcell = TimeCell(cue_size=3, delay_time=[0])
        self.pcell = PlaceCell(size=(20, 20))

        self.is_cue = False
        self.cue = None

    def set_cue(self, cue):
        self.is_cue = True
        self.cue = cue

    def conjunctive(self, position):
        t = self.tcell.cue_and_step(self.cue) if self.is_cue else self.tcell.step()
        p = self.pcell(position)

        self.is_cue = False
        self.cue = None

        c = p.reshape(-1, 1) * t.reshape(1, -1)
        return c


if __name__ == '__main__':
    hpc = HPC()

    objects = np.eye(3)

    hpc.set_cue(objects[0])
    print(hpc.conjunctive((0, 0)))

    print(hpc.conjunctive((0, 1)))
    print(hpc.conjunctive((0, 2)))
    print(hpc.conjunctive((0, 3)))