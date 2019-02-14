

class Stepper(object):
    def __init__(self, bit_sequence=[8, 12, 4, 6, 2, 3, 1, 9]):
        self._bit_sequence = bit_sequence
        self._seq_len = len(bit_sequence)
        self._current_position = 0
        self._desired_position = 0

    def set_desired_position(self, value):
        self._desired_position = int(value)

    def get_desired_position(self):
        return self._desired_position

    def get_current_position(self):
        return self._current_position

    def reset(self):
        self._current_position = 0
        self._desired_position = 0

    def stop(self):
        self._desired_position = self._current_position

    def next(self):
        if self._current_position < self._desired_position:
            self._current_position += 1
        elif self._current_position > self._desired_position:
            self._current_position -= 1

        return self._bit_sequence[self._current_position % self._seq_len]

    def has_desired_position(self):
        return self._current_position == self._desired_position
