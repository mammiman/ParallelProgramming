def calculate_pyramid_height(number_of_blocks):
     height=0
     for i in range (0,number_of_blocks):
        if((height*(height+1)/2)>=number_of_blocks):
            return height
        else:
            height+=1
print(calculate_pyramid_height())


