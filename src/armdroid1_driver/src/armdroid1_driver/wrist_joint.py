from .joint import Joint


class WristJoint(object):
    def __init__(self, stepper_left, stepper_right):
        self._stepper_left = stepper_left
        self._stepper_right = stepper_right

    def stop(self):
        self._stepper_left.stop()
        self._stepper_right.stop()

STEPS_PER_RADIAN = 495.894971686
class Wrist1Joint(WristJoint):
    def __init__(self, stepper_left, stepper_right, elbow_joint):
        WristJoint.__init__(self, stepper_left, stepper_right)
        self._elbow_joint = elbow_joint

    def get_current_angle(self):
        offset = self._elbow_joint.get_current_angle()

        left_pos = self._stepper_left.get_current_position()
        right_pos = self._stepper_right.get_current_position()

        center_pose = (left_pos + right_pos) / 2

        right_angle = (right_pos - center_pose) / STEPS_PER_RADIAN

        return right_angle - offset

    def set_desired_angle(self, angle):
        angle += self._elbow_joint.get_desired_angle()

        desired_position = STEPS_PER_RADIAN * angle

        self._stepper_left.set_desired_position(-desired_position)
        self._stepper_right.set_desired_position(desired_position)

class Wrist2Joint(WristJoint):
    def get_current_angle(self):
        return (self._stepper_right.get_current_position() + self._stepper_left.get_current_position()) / STEPS_PER_RADIAN

    def get_desired_angle(self):
        return (self._stepper_right.get_desired_position() + self._stepper_left.get_desired_position()) / STEPS_PER_RADIAN

    def set_desired_angle(self, angle):
        pass
        desired_offset = STEPS_PER_RADIAN * angle
        current_offset = self._stepper_right.get_desired_position() + self._stepper_left.get_desired_position()

        diff = desired_offset - current_offset

        self._stepper_left.set_desired_position(self._stepper_left.get_desired_position() + diff)
        self._stepper_right.set_desired_position(self._stepper_right.get_desired_position() + diff)
