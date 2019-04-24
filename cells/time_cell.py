# -*- coding:utf-8 -*-

import sys
import numpy as np
import copy


class TimeCell(object):
    def __init__(self, cue_size, delay_time):
        self._cue_size = cue_size
        self._delay_time = delay_time
        self._status = np.zeros((len(self._delay_time), self._cue_size), dtype=np.float32)
        self.reset()

    def reset(self):
        self._time = 0
        self._queue = []

    def step(self):
        self._status = np.zeros((len(self._delay_time), self._cue_size), dtype=np.float32)

        for q in self._queue:
            if (self._time - q['time']) in self._delay_time:
                self._status[self._delay_time.index(self._time - q['time']), :] = q['data']

            if (self._time - q['time']) > (self._delay_time[-1] + 1):
                self._queue.remove(q)

        self._time += 1
        return self._status

    def cue_and_step(self, cue):
        if not len(cue) == self._cue_size:
            sys.exit('cue_size is differ from', self._cue_size)
        self._queue.append({'data':copy.deepcopy(cue.reshape(-1)), 'time':self._time})
        return self.step()


if __name__ == '__main__':
    tcell = TimeCell(cue_size=5, delay_time=[0, 5, 10])
    
    stimulus = np.random.rand(5)

    print('0', tcell.cue_and_step(stimulus))
    print('1', tcell.cue_and_step(stimulus))
    print('2', tcell.step())
    print('3', tcell.step())
    print('4', tcell.step())
    print('5', tcell.step())
    print('6', tcell.step())
    print('7', tcell.step())
    print('8', tcell.step())
    print('9', tcell.step())
    print('9', tcell.step())
    print('9', tcell.step())