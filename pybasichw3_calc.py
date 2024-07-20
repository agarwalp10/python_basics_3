def homeArea(room_numbers):
    '''
        Function requires the number of room in the house passed as a parameter
        and will calculate and return the square footage of the house
    '''
    home_area = 0
    for i in range(room_numbers):
        room_len = int(input("room length: "))
        room_wid = int(input("room width: "))
        room_square = room_len*room_wid
        home_area += room_square
    return home_area

def circ_circle(rad): 
    '''
        Function requires the radius of the circule passed as a parameter
        and will calculate and return the circumference of a circle
    '''
    circ = 2*3.14159*rad
    return circ