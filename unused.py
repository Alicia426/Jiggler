mouse = {'left': '1', 'middle': '2',
                      'right': '3', 'scrollup': '4', 'scrolldown': '5'}

def moveTo(self, x, y):
        cmd(f'xdotool mousemove {x} {y}')


def genMouseAction(self, action):
    cmd(f'xdotool click {action}')