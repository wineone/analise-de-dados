from funcoes_capitulo_11 import *

x = [1,2,3,4,5,6,7,8,9,10]

y = [1,2,3,4,5,6,7,8,9,10]

print(train_test_split(x,y,0.3))

# teste de luke-leukemia

tp = 70

fp = 4930

fn = 13930

tn = 981070

print(accuracy(tp,fp,fn,tn))

print(precision(tp,fp,fn,tn))

print(recall(tp,fp,fn,tn))

print(f1_socre(tp,fp,fn,tn))