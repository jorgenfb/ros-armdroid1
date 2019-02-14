from .joint import Joint

STEPS_PER_RADIAN = 495.264718111

class BaseJoint(Joint):
    def __init__(self, stepper):
        Joint.__init__(self, stepper, STEPS_PER_RADIAN);

