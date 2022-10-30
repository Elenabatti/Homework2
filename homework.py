# Напишите программу, которая принимает на вход вещественные число и показывает сумму его цифр.
# Пример: 6782 -> 23; 0,56->11
# n = float(input())
# number_sum = 0
# while n != 0:
#     number_sum += n %10
#     n //= 10
# print(number_sum)


# №15
#Напишите программу, которая принимает число на вход и выдаёт набор произведений чисел от 1 до  N

# n = int(input())
# first_list = [1]
# factor = 1
# for i in range(2, n+1):
#     factor *= i
#     first_list.append(factor)
# print(first_list)    


# Task №16
# Задайте список из n последовательности (1+1/n)2  и выведите на экран их сумму
n = int(input())
set_the_list = []
for i in range(1, n + 1):
    set_the_list.append((1+1/i)** i)
print(sum(set_the_list))    
