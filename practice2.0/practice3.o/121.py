# my_list = []

# for _ in range(10):
#     element = int(input("Enter an element: "))
#     my_list.append(element)

# print("List after insertion:", my_list)


# my_list = [int(input("enter number :")) for _ in range(10)]
# count = sum (1 for i in range(len(my_list)) if i % 2==1 and my_list[i] %2 ==1)
# print("total odd number with odd index are",count)


my_list = [int(input("enter element number:")) for _ in range(5)]
count = sum(1 for i in range(len(my_list)) if i%2==0 and my_list[i] %2 == 0)
print("total even numbers with even index",count)