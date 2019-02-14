TEMPLATE = 'Output: [sync={}, motor={}{}{}, command={}{}{}{}]'


class IOAdapter(object):
    def __init__(self):
        pass

    def write_output(self, syncBit, motorId, motorCode):
        b0 = (motorCode >> 0) & 1
        b1 = (motorCode >> 1) & 1
        b2 = (motorCode >> 2) & 1
        b3 = (motorCode >> 3) & 1

        m0 = (motorId >> 0) & 1
        m1 = (motorId >> 1) & 1
        m2 = (motorId >> 2) & 1

        #print TEMPLATE.format(syncBit, m2, m1, m0, b3, b2, b1, b0)
