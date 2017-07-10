USB_KEY = "/home/simon/Code/sr/usbkey"

OUT_H0 = 0
OUT_H1 = 1
OUT_L0 = 2
OUT_L1 = 3
OUT_L2 = 4
OUT_L3 = 5

class Robot:
    def __init__(self, zone = 0):
        self.zone = zone
        self.mode = "dev"
        self.usbkey = USB_KEY
        self.power = Power()
        self.motors = [MotorBoard()]
        self.servos = []
        self.ruggeduinos = [Ruggeduino()]

    def index(self):
        return "robot"

    def see(self):
        return "This is what I can see..."

class Power:
    def __init__(self):
        self.output = []
        self.output[OUT_H0] = True
        self.output[OUT_H1] = True
        self.output[OUT_L0] = True
        self.output[OUT_L1] = True
        self.output[OUT_L2] = True
        self.output[OUT_L3] = True

    def index(self):
        return "power"

    def beep(self, time, note, frequency):
        return "beep"

class MotorBoard:
    def __init__(self, zone = 0):
        self.m0 = Motor()
        self.m1 = Motor()

    def index(self):
        return "motor_board"

class Motor:
    def __init__(self, zone = 0):
        self.use_brake = True

    def index(self):
        return "motor"

    def power(self, power):
        return "power"

class Ruggeduino:
    def index(self):
        return "ruggeduino"

    def pin_mode(self, pin, mode):
        return "pin_mode"

    def digital_read(self, pin):
        return "digital_read"

    def analogue_read(self, pin):
        return "anaolgoue_read"

    def digital_write(pin, value):
        return "digital_read"

class Marker:
    '''
    A Marker object contains information about a detected marker. It has the following attributes:

    info
        A MarkerInfo object containing information about the type of marker that was detected.
    centre
        A Point describing the position of the centre of the marker.
    vertices
        A list of 4 Point instances, each representing the position of the black corners of the marker.
    dist
        An alias for centre.polar.length
    rot_y
        An alias for centre.polar.rot_y
    orientation
        An Orientation instance describing the orientation of the marker.
    res
        The resolution of the image that was taken from the webcam. A 2-item tuple: (width, height).
    timestamp
        The timestamp at which the image was taken (a float).
    '''

    def index(self):
        return "marker"

class MarkerInfo:
    '''
    The MarkerInfo object contains information about a marker. It has the following attributes:

    code
        The numeric code of the marker.
    marker_type
        The type of object that this marker represents.
        One of:
        MARKER_ARENA
        MARKER_ROBOT
        MARKER_TOKEN_A
        MARKER_TOKEN_B
        MARKER_TOKEN_C
    offset
        The offset of the numeric code of the marker from the lowest numbered marker of its type. For example: markers 28 and 29, which are the lowest numbered markers that represent robots, have offsets of 0 and 1 respectively. Due to the arrangement of the ids for the token markers, this value is only defined for the MARKER_ARENA and MARKER_ROBOT type tokens.
    size
        The size of the marker in metres. This is the length of the side of the main black body of the marker.
    '''

    def index(self):
        return "marker_info"

class Point:
    '''
    A Point object describes a position in three different ways. These are accessed through the following attributes:

    image
        The pixel coordinates of the point in the image, with the origin (0,0) in the top-left of the image. This has two attributes: x and y.
    world
        The Cartesian coordinates of the point in 3D space. This has three attributes: x, y, and z, each of which specifies a distance in metres. Positions in front of, to the right, or above the camera are positive. Positions to the left or below are negative.
    polar
        The polar coordinates of the point in 3D space.
        This has three attributes:
        length
        The distance to the point.
    rot_x
        Rotation about the x-axis in degrees. Positions above the camera are positive.
    rot_y
        Rotation about the y-axis in degrees. Positions to the right of the camera are positive.
    '''

    def index(self):
        return "point"

class Orientation:
    '''
    An Orientation object describes the orientation of a marker. It has three attributes:

    rot_x
        Rotation of the marker about the x-axis.
        Leaning a marker away from the camera increases the value of rot_x, while leaning it towards the camera decreases it. A value of 0 indicates that the marker is upright.

    rot_y
        Rotation of the marker about the y-axis.
        Turning a marker clockwise (as viewed from above) increases the value of rot_y, while turning it anticlockwise decreases it. A value of 0 means that the marker is perpendicular to the line of sight of the camera.

    rot_z
        Rotation of the marker about the z-axis.
        Turning a marker anticlockwise (as viewed from the camera) increases the value of rot_z, while turning it clockwise decreases it. A value of 0 indicates that the marker is upright.
    '''

    def index(self):
        return "orientation"
