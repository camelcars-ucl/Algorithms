A = [i for i in range(4)]
B = []
C = []

def move(height, fromPole, auxillary, target):
    if height > 0:
        move(height-1, fromPole, target, auxillary)  # 1
        target.insert(0, fromPole.pop(0))
        print(A, B, C, '##############', sep = '\n')
        move(height-1, auxillary, fromPole, target)  # 2

move(4, A, B, C)


'''
Perhaps I should try explaining the theory
Say you had

1||
2||
3||
4||
ABC

The objective is to move all 4 disks from A to C. First we must ask, well how do I get
disk 4 to C? You do this by getting disk 1,2,3 to B. Well how do I do that? You
do that by getting disk 1,2 to C. Well how do I do that? You do that by getting
disk 1 to B, which is trivial. This is what line #1 is doing

Well say you now end up in a situation like this (which is correct):
|||
|||
||1
432

What should be the next move? Well now I need to get disk 3 to pole C, and to do
that I need to get disk 1,2 to pole A. Again how do I do that? I first need to get
disk 1 to pole B, which is trivial.

So we get 1->B, 2->A, 1->A and finally 3->C.
This is what #2 is trying to accomplish

'''
