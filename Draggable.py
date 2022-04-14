import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as patches
print(matplotlib.__version__)

fig = plt.figure(figsize=(4, 4))
plt.xlim([-500, 500])
plt.ylim([-500, 500])
ax = fig.add_subplot(111)


class Draggable_Target:
    lock = None

    def __init__(self, point):
        self.point = point
        self.press = None
        self.background = None
        self.ID = None

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def connect(self):
        # 'connect to all the events we need'
        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        if event.inaxes != self.point.axes:
            return
        if Draggable_Target.lock is not None:
            return
        contains, attrd = self.point.contains(event)
        if not contains:
            return
        self.press = (self.point.center), event.xdata, event.ydata
        Draggable_Target.lock = self
        canvas = self.point.figure.canvas
        axes = self.point.axes
        self.point.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.point.axes.bbox)
        axes.draw_artist(self.point)
        canvas.blit(axes.bbox)

    def on_motion(self, event):
        if Draggable_Target.lock is not self:
            return
        if event.inaxes != self.point.axes:
            return
        self.point.center, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.point.center = (self.point.center[0] + dx, self.point.center[1] + dy)
        print(str(self.point.center[0]) + ',' + str(self.point.center[1]), file=open('target.csv', 'w'))
        canvas = self.point.figure.canvas
        axes = self.point.axes
        canvas.restore_region(self.background)
        axes.draw_artist(self.point)
        canvas.blit(axes.bbox)

    def on_release(self, event):
        # 'on release we reset the press data'
        if Draggable_Target.lock is not self:
            return

        self.press = None
        Draggable_Target.lock = None
        self.point.set_animated(False)
        self.background = None
        self.point.figure.canvas.draw()

    def disconnect(self):
        # 'disconnect all the stored connection ids'
        self.point.figure.canvas.mpl_disconnect(self.cidpress)
        self.point.figure.canvas.mpl_disconnect(self.cidrelease)
        self.point.figure.canvas.mpl_disconnect(self.cidmotion)


drs = []
circles = [patches.Circle((10, -10), 20, label='Click to drag the Target', fc='k', color='k', alpha=1)]
cnt = 0
for circ in circles:
    ax.add_patch(circ)
    dr = Draggable_Target(circ)
    dr.setID(cnt)
    dr.connect()
    drs.append(dr)
    cnt += 1
plt.legend()
plt.show()
