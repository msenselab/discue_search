from psychopy import sound, gui, visual, core, data, event

win = visual.Window([400,400], 
                    allowGUI=False, 
                    fullscr=False, 
                    monitor='testMonitor', 
                    units='pix')

# create a polygon
polygon = visual.Polygon(win,
                         edges=6,
                         size = 50,
                         fillColor = [0,0.8,0.5])

# create a line
line = visual.Line(win,
                     start = [-100,0],
                        end = [100,0],
                        lineWidth = 5,
                        lineColor = [0,0,0])

# an array of edges from 3 to 6
edges = range(3,7)
# four x positions from -150 to 150
xpos = range(-150, 151, 100)

# create four polygons based on edges and xpos
# and draw them to the screen
for i in range(4):
    polygon.edges = edges[i]
    polygon.pos = [xpos[i], 0]
    polygon.draw()    

win.flip()

event.waitKeys()
win.close()

