'''import math  
x1=int(input("Enter number:"))  
''x2=int(input("Enter number:"))  
y1=int(input("Enter number:"))  
y2=int(input("Enter number:"))  
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)  
print("Distance between two points is : ",distance) 
'''


def swap_list_elements(my_list, index1, index2):
    """Swaps elements at two given indices in a list."""
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
# Example usage:
my_list = [10, 20]
print("Original list:", my_list)
swap_list_elements(my_list, 0, 1)  # Swap elements at indices 0 and 1
print("Modified list:", my_list)

