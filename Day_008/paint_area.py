height=float(input("What is the height?\n"))
width=float(input("What is the Width?\n"))
def paint_area(h, w):
    #coverage per can is 5sqm
    result=(h*w)/5
    return round(result)
print(f"The number of cans required are {paint_area(height,width)}")