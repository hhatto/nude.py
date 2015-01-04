import os
import nude
from nude import Nude

ROOT = os.path.dirname(os.path.abspath(__file__))

n = Nude(os.path.join(ROOT, 'images/damita.jpg'))
n.parse()
print(n.result, n.inspect())

n = Nude(os.path.join(ROOT, 'images/damita2.jpg'))
n.parse()
print(n.result, n.inspect())

n = Nude(os.path.join(ROOT, 'images/test6.jpg'))
n.parse()
print(n.result, n.inspect())

n = Nude(os.path.join(ROOT, 'images/test2.jpg'))
n.parse()
print(n.result, n.inspect())
