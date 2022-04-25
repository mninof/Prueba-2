# -*- coding: utf-8 -*-
"""CodeAbbey 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kZmLTUVYYnrG58QvHGtdy0ElHhGhGKaQ
"""
#Hola
#Matching words

data = [i for i in input().split()]
data.sort()
ans = []

for i in data:
  if data.count(i) > 1:
    ans.append(i)
    j = data.count(i)
    while j > 1: #Se encarga de que un elemento que aparece más de una vez en data no aparezca más de una vez en ans.
      data.remove(i)
      j -= 1

print(*ans, sep=' ')

#Two printers

data=[int(i) for i in input().split()]
ans=[]
i=0

while i < len(data):
  n=data[i+2]
  x=data[i]
  y=data[i+1]
  sec=0
  while n > 0:
    if x < y:
      x,y = y,x
    if n > 
  ans.append(sec)
  i+=3

print(*ans, sep=' ')

#Bulls and cows (¿por qué se llama así? xd)

secret_value = input('Número secreto: ')
guesses = [str(i) for i in input().split()]
answer = []
i = 0

while i < len(guesses):
  attempt = str(guesses[i])
  x = 0
  y = 0
  j = 0
  while j < len(attempt):
    if attempt[j] == secret_value[j]:
      x += 1
    elif attempt[j] in secret_value:
      y += 1
    j += 1
  answer.append(str(x) + '-' + str(y))
  i += 1

print(*answer, sep=' ')

#Prime numbers generation

def is_prime(num): #Tomado de la actividad de funciones que el profe nos dejó para hacer en grupos.
  if num <= 1 or (num % 2 == 0 and num > 2): 
    return False

  return all(num % i for i in range(3, int((num)**(1/2)) + 1, 2))

def primos_menores_que(num):
  lista = [2]
  n = 3

  while n < num:
    if is_prime(n) == True:
      lista.append(n)
    n += 2

  return lista

def primeros_n_primos(num):
  lista = [2]
  n = 3
  i = 1

  while i < num:
    if is_prime(n) == True:
      lista.append(n)
      i += 1
    n += 2

  return lista

primos = primeros_n_primos(200000)
indices = [int(i)-1 for i in input().split()]
result = []

for i in indices:
  result.append(primos[i])

print(*result, sep=' ')

#Fool's Day 2014

cases = int(input('Digite el número de casos a evaluar: '))
i = 0
ans = []

while i < cases:
  case = [int(i) for i in input().split()]
  j = 0
  sum = 0
  while j < len(case):
    sum += case[j]*case[j]
    j += 1
  ans.append(sum)
  i += 1

print(*ans, sep=' ')

#Combinations counting

def factorial(n):
  factorial = 2
  i = 3

  while i <= n:
    factorial *= i
    i += 1

  return factorial

def Combinations(n, k):
  combinations = int(factorial(n) / (factorial(k) * factorial(n-k)))

  return combinations

cases = [int(i) for i in input().split()]
ans = []
i = 0

while i < len(cases):
  ans.append(Combinations(cases[i], cases[i+1]))
  i += 2

print(*ans, sep=' ')

#Blackjack counting

n = int(input('Digite el número de casos a evaluar: '))
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
tens = ['K', 'Q', 'J', 'T']
ans = []
i = 0

while i < n:
  caso = [i for i in input().split()]
  score = 0
  a = 0
  j = 0
  while j < len(caso):
    if caso[j] in nums:
      score += int(caso[j])
    elif caso[j] in tens:
      score += 10
    else:
      a += 1
    j += 1

  if score + (a*11) <= 21:
    score += a*11
  else:
    score += a*1

  if score <= 21:
    ans.append(score)
  else:
    ans.append('Bust')
  i += 1

print(*ans, sep=' ')

#Parity control

data = [int(i) for i in input().split()]

data = [bin(i) for i in data]

new_data = []

print(data)

for i in data:
  count = 0
  for j in i:
    if j == '1':
      count += 1
  if count % 2 == 0:
    new_data.append(i)

i = 0

print(new_data)

while i < len(new_data):
  if len(new_data[i]) == 10 and new_data[i][2] == '1':
    new_data[i] = '0b'+new_data[i][3:10]
  i += 1

print(new_data)

new_data = [int(i, 2) for i in new_data]

print(new_data)

string = ''

for i in new_data:
    string += chr(i)

print(string)

nums = [i for i in range(1, 101, 2)]

print(nums)

for i in nums:
  if i % 2 != 0:
    nums.remove(i)

print(nums)
