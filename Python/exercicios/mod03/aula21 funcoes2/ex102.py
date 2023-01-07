
def fatorial(n,show=False):
    f=1
    if show==False:
        for c in range(n,0,-1):
            f*=c
        return f
    else:
        for c in range(n,0,-1):
            f*=c
            print(f'{c} ',end='')
            if c!=1:
                print('x ',end='')
        print(f'= {f}')

print('-'*20)
num = int(input())
fatorial(num,show=True)