import sys

def read_input():
    f = sys.stdin
    r, b, y = map(int, f.readline().split())
    print(r ,b,y)
    return r, b, y

read_input()


def solve(r, b, y):
    answer = 0
    # code here
    if(max(r,b,y)==r):
        answer = r*3-3
    elif(max(r,b,y)==b):
        answer= b*3
    else:
        answer= y*3+3
    return answer

def main():
    read_input()
    # answer = solve(r, b, y)
    # print(answer)


if __name__ == '__main__':
    main()