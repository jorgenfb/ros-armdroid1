

class Joint(object):
    def __init__(self, stepper, ratio):
        self._stepper = stepper
        self._ratio = ratio

    def set_desired_angle(self, angle):
        desired_position = self._angle_to_position(angle)
        self._stepper.set_desired_position(desired_position)

    def stop(self):
        self._stepper.stop()

    def get_current_angle(self):
        return self._position_to_angle(self._stepper.get_current_position())

    def get_desired_angle(self):
        return self._position_to_angle(self._stepper.get_desired_position())

    def is_moving(self):
        return self._stepper.has_desired_position()

    def _angle_to_position(self, angle):
        return angle * self._ratio

    def _position_to_angle(self, position):
        return position / self._ratio
