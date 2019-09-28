w, h = 800, 800

pfc = (252, 108, 133)
olc = (0, 0, 0)
bgc = (108, 252, 227)

pw = 7
rw = 7

def draw_planet(position, ps):
    # pushMatrix()
    
    # translate(position[0], position[1])
    starting_height = ps/3
    starting_width = ps*2)
    rotate()
    
    
    # Add colored circle
    fill(pfc[0], pfc[1], pfc[2])
    strokeWeight(pw)
    circle(0, 0, ps)
    
    # Settings for the rings
    noFill()
    strokeWeight(rw)
    for i in range(int(6)):
        ellipse(0, 0, starting_height + i * 10, starting_width + i * 30)
    
    # Cover up part of the rings
    strokeWeight(pw)
    fill(pfc[0], pfc[1], pfc[2])
    arc(0, 0, ps, ps, 1.5*PI, 2.5*PI);
    
    # popMatrix()

def setup():
    size(w, h)
    pixelDensity(2)
    frameRate(1)
    
    translate(w/2, h/2)
    
    stroke(olc[0], olc[1], olc[2])
    
    planet_size = 60
    total = 0
    
    for j in range(50):
        background(bgc[0], bgc[1], bgc[2])
    
        draw_planet((w/2, h/2), planet_size)
        
        save("Examples/Gif" + str(total) + ".png")
        
        planet_size += 2
        total += 1
    
    for j in range(5):
        background(bgc[0], bgc[1], bgc[2])
    
        draw_planet((w/2, h/2), planet_size)
        
        save("Examples/Gif" + str(total) + ".png")
        total += 1
    
    for j in range(50):
        background(bgc[0], bgc[1], bgc[2])
    
        draw_planet((w/2, h/2), planet_size)
        
        save("Examples/Gif" + str(total) + ".png")
        
        planet_size -= 2
        total += 1
    
    for j in range(5):
        background(bgc[0], bgc[1], bgc[2])
    
        draw_planet((w/2, h/2), planet_size)
        
        save("Examples/Gif" + str(total) + ".png")
        total += 1
    
        
