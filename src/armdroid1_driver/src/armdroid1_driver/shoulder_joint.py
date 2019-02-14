from .joint import Joint

STEPS_PER_RADIAN = 697.69070711

class ShoulderJoint(Joint):
    def __init__(self, stepper):
        Joint.__init__(self, stepper, STEPS_PER_RADIAN);

