from .joint import Joint

STEPS_PER_RADIAN = 697.690707131

class ElbowJoint(Joint):
    def __init__(self, stepper, shoulder_joint):
        Joint.__init__(self, stepper, STEPS_PER_RADIAN)

        self._shoulder_joint = shoulder_joint

    def get_current_angle(self):
        return Joint.get_current_angle(self) - self._shoulder_joint.get_current_angle()

    def set_desired_angle(self, angle):
        angle += self._shoulder_joint.get_desired_angle()
        Joint.set_desired_angle(self, angle)


