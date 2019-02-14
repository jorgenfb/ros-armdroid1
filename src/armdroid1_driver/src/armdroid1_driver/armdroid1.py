import importlib
import rospy
from .stepper import Stepper
from .base_joint import BaseJoint
from .shoulder_joint import ShoulderJoint
from .elbow_joint import ElbowJoint
from .wrist_joint import Wrist1Joint, Wrist2Joint

from sensor_msgs.msg import JointState


class Armdroid(object):
    def __init__(self, io_adapter):

        self._io_adapter = io_adapter

        steppers = [Stepper() for i in range(6)]


        base_joint = BaseJoint(steppers[0])
        shoulder_joint = ShoulderJoint(steppers[1])
        elbow_joint = ElbowJoint(steppers[2], shoulder_joint)
        wrist1_joint = Wrist1Joint(steppers[3], steppers[4], elbow_joint)
        wrist2_joint = Wrist2Joint(steppers[3], steppers[4])

        joints = [base_joint, shoulder_joint, elbow_joint, wrist1_joint, wrist2_joint]

        self._steppers = steppers
        self._joints = joints

        self._state_pub = rospy.Publisher(
            'joint_states', JointState, queue_size=10)
        self._set_state_sub = rospy.Subscriber(
            'set_joint_states', JointState, self._set_joint_states)

        rospy.Timer(rospy.Duration(0.01), self._tick)

    def _set_joint_states(self, joint_states):
        for i in range(len(self._joints)):
            self._joints[i].set_desired_angle(joint_states.position[i])

    def _tick(self, timer_event):
        commands = []

        sleep_duration = rospy.Duration(0.001)

        for i in range(6):
            stepper = self._steppers[i]

            if not stepper.has_desired_position():
                motor_command = stepper.next()
                self._io_adapter.write_output(False, i + 1, motor_command)
                rospy.sleep(sleep_duration)

                self._io_adapter.write_output(True, i + 1, motor_command)
                rospy.sleep(sleep_duration)

        joint_state = JointState()
        joint_state.header.stamp = rospy.Time.now()
        joint_state.name = ['base_joint', 'lowerarm_joint', 'upperarm_joint',
        'wrist1_joint', 'wrist2_joint']
        joint_state.position = [joint.get_current_angle()
                                for joint in self._joints]
        self._state_pub.publish(joint_state)


if __name__ == '__main__':
    rospy.init_node('armdroid')
    use_mock = rospy.get_param('~use_mock', False)

    if use_mock:
        io_adapter = importlib.import_module('.io_adapter').IOAdapter()
    else:
        io_adapter = importlib.import_module('.io_adapter_real').IOAdapter()

    Armdroid(io_adapter)

    rospy.spin()
