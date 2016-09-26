

cdef class Skin:
    cdef public int id
    cdef public int skin
    cdef public int region
    cdef public int x
    cdef public int y
    cdef public int checked

    def __cinit__(self, int skin_id, int skin, int region, int x, int y,
                  int checked):
        self.id = skin_id
        self.skin = skin
        self.region = region
        self.x = x
        self.y = y
        self.checked = checked


    def __init__(self, int skin_id, int skin, int region, int x, int y,
                  int checked):
        self.id = skin_id
        self.skin = skin
        self.region = region
        self.x = x
        self.y = y
        self.checked = checked

    def _replace(self, int region):
        self.region = region
        return self

def skin_classifier(double r, double g, double b):
    if _rgb_classifier(r, g, b):
        return True
    if _norm_rgb_classifier(r, g, b):
        return True
    if _hsv_classifier(r, g, b):
        return True
    if _ycbcr_classifier(r, g, b):
        return True
    return False

cdef bint _rgb_classifier(double r, double g, double b):
    classifier = r > 95 and g > 40 and g < 100 and b > 20 and max([r, g, b]) - min([r, g, b]) > 15 and abs(r - g) > 15 and r > g and r > b
    return classifier

cdef bint _norm_rgb_classifier(double r, double g, double b):
    if r == 0:
        r = 0.0001
    if g == 0:
        g = 0.0001
    if b == 0:
        b = 0.0001
    cdef double _sum = r + g + b
    cdef double nr = r/_sum, ng = g/_sum, nb = b/_sum;
    return nr / ng > 1.185 and float(r * b) / ((r + g + b) ** 2) > 0.107 and float(r * g) / ((r + g + b) ** 2) > 0.112

cdef bint _hsv_classifier(double r, double g, double b):
    cdef double h = 0, _sum = r + g + b, _max = max([r, g, b]), _min = min([r, g, b]), diff = _max - _min,
    if _sum == 0:
        _sum = 0.0001
    if _max == r:
        if diff == 0:
            h = 9223372036854775807
        else:
            h = (g - b) / diff
    elif _max == g:
        h = 2 + ((g - r) / diff)
    else:
        h = 4 + ((r - g) / diff)

    h *= 60
    if h < 0:
        h += 360

    cdef double s = 1.0 - (3.0 * (_min / _sum)), v = (1.0 / 3.0) * _max
    return h > 0 and h < 35 and s > 0.23 and s < 0.68

cdef bint _ycbcr_classifier(double r, double g, double b):
    cdef double y = .299*r + .587*g + .114*b, cb = 128 - 0.168736*r - 0.331364*g + 0.5*b, cr = 128 + 0.5*r - 0.418688*g - 0.081312*b
    return 97.5 <= cb <= 142.5 and 134 <= cr <= 176




