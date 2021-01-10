import math

def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint.")

print("Painting area calculator!")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("How many square meters of wall can one can cover? "))
paint_calc(height=test_h, width=test_w, cover=coverage)






