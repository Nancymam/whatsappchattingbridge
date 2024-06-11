# # a = """hello"""
# # print(a)
# # print(type(a))

# # set  of characters => "bdfhhfkg1234567890!@#%^&*" eg => "hello"

# # "",'',""""""

# # a = [12,34,"hello","34",5.5,6j]
# # a[1] = 35
# # print(a)
# # print(type(a))

# # a = (12,23,445,7,78)
# # a[1] = 24
# # print(a)


# # a = {12,24,46,56,567,8,8,8,8,8,8,8}
# # print(a)

# # a = {1:"neha",2:"nancy",1:"naina"}
# # print(a)

# # a = True
# # print(a)
# # print(type(a))


# # nested if else

# # condition in condition 


# # student num < 33 => + 3 marks grace => 33 pass

# # num = int(input("enter the number : "))
# # if num < 33:
# #     num += 3
# #     if num < 33:
# #         print("fail")
# #     else:
# #         print("pass with grace marks")    
# # else:
# #     print("pass")    

# # 1unit = 5rs

# # 125units * 5
# # 120 * 5

# # 126 > 125 => (125 * 5)  + (126-125)* 50

# # looping => block of code repeat 

# # youtube => playlist => 10 videos => 1-> 2 3 4 5 6  7 8 9 10


# # for , while loop

# # for loop => condition true execute => s,s,s => start,stop,step
# # i = 0
# # print(i)
# # i = 1  i = 0; i < 10; i++;
# # i = 2

# # for i in range(1,10,1):
# #     print(i)

# # task =>

# # output -:
# # enter the number : 2
# # 2 x 1 = 2

# # num = int(input("Enter the number : "))
# # for i in range(1,11,1):
# #     print(f"{num} x {i} = {num * i}")


# # import tensorflow as tf



# # a = tf.Variable([
# #     [1,2,4],
# #     [1,2,4],
# #     [5,4,3]
# # ])
# # b = tf.Variable(20)
# # a = tf.constant(5.0)
# # b = tf.constant(6.0)
# # c = a * b



# # sess = tf.compat.v1.Session()

# # print(sess.run(c))

# # print(tf.maximum(10,2))

# import numpy as np 
# import keras.backend as K
# import tensorflow as tf

# t1 = K.variable(np.array([ [[1, 2], [2, 3]], [[4, 4], [5, 3]]]))
# t2 = K.variable(np.array([[[7, 4], [8, 4]], [[2, 10], [15, 11]]]))

# d0 = K.concatenate([t1 , t2] , axis=-2)

# init = tf.global_variables_initializer()

# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(d0))

# import tensorflow as tf

# # Define the computational graph
# a = tf.constant(2)
# b = tf.constant(3)
# c = a + b

# # Create a session to run the graph
# with tf.Session() as sess:
#     result = sess.run(c)
#     print(result)  # Output: 5


# tensorflow => open source lib = numeric compu=> tensorflow=>detection
# tensor -> multidimentional array
# flow -> data flow
# date with time variable , constant

# import tensorflow as tf

# a = tf.constant([
#     [12,23,4,56],
#     [12,23,4,56],
#     [12,23,4,56],
# ])
# b = tf.constant([
#      [12,23,4,56],
#     [12,23,4,56],
#     [12,23,4,56],
# ])
# c = tf.add(a,b)

# print(c)
# session => perm 
# cookie => temp

# import tensorflow as tf

# tf.compat.v1.disable_eager_execution()

# a = tf.Variable([1,2,4])
# b = tf.Variable([1,2,4])

# c= a + b

# with tf.compat.v1.Session() as sess:
#     result = sess.run(c)
#     print(result)


# import keras

# ann => input , hidden, output

# exception handling

# a = int(input("enter number : "))
# print(b)
# try:
#     a = int(input("enter number : "))
#     print(a)
# except ValueError:
#     raise ValueError("value error")
# except NameError:
#     raise NameError("Name error")
# except:
#     print("default error")    
# else:
#     print("no error")
# finally:
#     print("finally")


# c = 10 ** 2
# print(c)

# a = 10
# a += 2
# print(a)

# a = 10
# b= 10
# c = a <= b
# print(c)


# while loop => condition true => execute
# i= 1
# while i < 20:
#     print(i)
#     i += 1
    
# for i in range(1):
#     print(i)

# task =>
# import random
# import webbrowser
# import pywhatkit
# import pyjokes
# while True:
#     name = input("Me : ").lower()
#     greeting = ["hello","hii","hye","good morning","good evening"]
#     greetingans = ["hello","hii","hye","good morning","good evening"]
#     if name in greeting:
#         print(f"Bot : {random.choice(greetingans)}")
#     elif "name" in name:
#         print("Bot : I am bot")
#         n = input("What is your good name : ")
#         print(f"{n}, nice name")
#     elif "bye" in  name:
#         print("bye")
#         exit()   
#     elif "open google" in name:
#         print("opening google...")
#         a = input("What should i search on google : ")
#         pywhatkit.search(a)
#     elif "open youtube" in name:
#         a = input("What should i search on google : ")
#         pywhatkit.playonyt(a)

#     elif "joke" in name:
#         print(pyjokes.get_joke())    
             

# CRUD => C => CREATE,READ,UPDATE,DELETE

# create => 

# mode => "w","r","a"

# f = open("newf.txt","a")
# # f.write(" Hii, I am there")
# # f.close()
# r = f.read()
# print(r)
# f.close()

# import os 

# os.unlink("newf.txt")


# r+
# w+
# a+
# rb


# class car():
#     def mi(self):
#         print("30km/h")

# i20 = car()
# i20.mi()

