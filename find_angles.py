import math

'''
    Angles of the triangle can be found by calculating slopes and using formula:
            tan(angle) = (m1-m2)/(1+m1*m2)
    This can be undefined and gives error when the given triangle is right-angled

    Hence, using the coisne formula seems to be more robust and reliable:
            a**2 = b**2 + c**2 - 2*b*c*cos(angle between b and c)
'''

def get_angles(a, b, c):
    
    # # Given side lengths of the triangle
    # a = 3  
    # b = 4  
    # c = 5  

    # Calculate angle 'C' using the Law of Cosines
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    angle_C_rad = math.acos(cos_C)
    angle_C_deg = math.degrees(angle_C_rad)

    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    angle_A_rad = math.acos(cos_A)
    angle_A_deg = math.degrees(angle_A_rad)

    angle_B_deg = 180 - angle_A_deg - angle_C_deg
    return [angle_A_deg, angle_B_deg, angle_C_deg]

    

get_angles(5,4,3)