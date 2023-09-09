import cv2 as cv
import numpy as np
from math import  sqrt, atan, degrees
import turtle 

from animate import draw_on_canvas, draw_sides
from find_angles import get_angles

def angles_of_triangle(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    m1 = (y3-y2)/(x3-x2)
    m2 = (y3-y1)/(x3-x1)
    m3 = (y2-y1)/(x2-x1)

    angle1 = degrees(atan((m3-m2)/(1+m3*m2)))
    angle2 = degrees(atan((m3-m1)/(1+m3*m1)))
    angle3 = degrees(atan((m2-m1)/(1+m2*m1)))
    print(angle1,angle2,angle3)

    ### angle can be negative so take the absolute value
    angle1 = round(abs(angle1),2)
    angle2 = round(abs(angle2), 2)
    angle3 = round(abs(angle3),2)

    ### representing these angles on the triangle
    # cv.putText(img,f'{angle1}',(start_point[0] + 30, start_point[1]-10), cv.FONT_HERSHEY_COMPLEX_SMALL,1,(207,140,50),1)
    # cv.putText(img,f'{angle2}',(end_point[0]-80, end_point[1]-10),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(207,140,50),1)
    # cv.putText(img,f'{angle3}',(intersecting_point[0]-20, intersecting_point[1]+30), cv.FONT_HERSHEY_COMPLEX_SMALL,1,(207,140,50),1)
    return angle1, angle2, angle3

def name_the_sides():
    pass


def main():
        
    input_ = input("Input sides sperated by space ")
    sides = input_.split()
    sides = [int(side) for side in sides]

    # sides = [4,5,5]
    # let longest side be a


    '''
    My Device 
    Dimensions: 32.4 x 22.5 x 1.8 cm
    Resolution: 1920 x 1080 Pixels

    pixels per cm is 60 (not accurate)
    '''

    scale = 60 ## pixels per cm
    sides = [scale*length for length in sides]
    # print(sides)
    sides.sort(reverse=True)
    print('Pixel count of sides: ',sides)

    ### if sides are out of bound of the pixels
    downscale = max(sides)// 500 +1
    print( 'Downscale applied: ', downscale)
    sides = [int(side/downscale)  for side in sides]
    print('Pixel count after donwscale: ',sides)
    a = sides[0] ### let a be the largest side and this will be the base
    b = sides[1]
    c = sides[2]

    window_width = 640
    window_height = 480

    base_center = (window_width/2, window_height - 50)
    img = np.zeros((480,640,3),np.uint8)


    start_point = (int(base_center[0]- a//2), base_center[1])
    end_point = (start_point[0]+a, start_point[1])
    print(start_point)
    cv.line(img,start_point,end_point,(200,200,200),2)

    angles = get_angles(a,b,c)
    angles = [round(angle,2) for angle in angles]
    draw_on_canvas(start_point, a,b,c, angles)
    # draw_sides(b, angles[1], direction="right")
    # draw_sides(c, angles[2], direction="left")

    '''
    height (or the altitude) is common for both the circles
    Hence,
    b**2 - x**2 = c**2 - (a-x)**2
    b**2 - c**2 = x**2 - (a-x)**2
                = a * (2x - a)
        x = (b^2-c^2+a^2)/2a
        
    h^2 = b^2 - x^2

    '''
    x = int((b**2 - c**2 + a**2)/(2*a))
    height  = int(sqrt(b**2 - x**2))

    ### coordinates of the intersecting point
    intersecting_point = (start_point[0]+x, start_point[1]-height)
    cv.circle(img, intersecting_point,2,(255,255,255), -1)
    cv.circle(img, intersecting_point, 8, (0,0,255),2)

    # a1, a2, a3  = angles_of_triangle(start_point, end_point, intersecting_point)
    # print(a1 + a2 +a3)

    #### drawing the remaining two sides
    cv.line(img,start_point,intersecting_point,(200,200,200),2)
    cv.line(img,end_point,intersecting_point,(200,200,200),2)

    # cv.imshow("Triangle",img)
    # cv.waitKey(0)
    turtle.mainloop()

if __name__ == "__main__":
    main()