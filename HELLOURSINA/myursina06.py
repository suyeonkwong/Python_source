from ursina import *

app = Ursina()
# camera.orthographic = True
camera.z = -50

def myclick(i,j):
    print("myclick",i,j)
        
for i in range(10):
    for j in range(10):
        pb = Entity(model='cube', texture='0',collider='box', on_click=Func(myclick, i,j))
        pb.x = j - 4.5
        pb.y = -i + 4.5
    


def update():   # update gets automatically called.
    camera.rotation_z += held_keys['d'] * 1
    camera.rotation_z -= held_keys['a'] * 1
    
    

app.run()   # opens a window and starts the game.