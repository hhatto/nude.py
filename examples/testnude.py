import nude
from nude import Nude

#print("damita :", nude.is_nude('./images/damita.jpg'))
#print("damita2:", nude.is_nude('./images/damita2.jpg'))
#print("test6  :", nude.is_nude('./images/test6.jpg'))
#print("test2  :", nude.is_nude('./images/test2.jpg'))

n = Nude('./images/damita.jpg')
n.parse()
print(n.result, n.inspect())

n = Nude('./images/damita2.jpg')
n.parse()
print(n.result, n.inspect())

n = Nude('./images/test6.jpg')
n.parse()
print(n.result, n.inspect())

n = Nude('./images/test2.jpg')
n.parse()
print(n.result, n.inspect())
