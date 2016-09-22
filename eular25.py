# encoding=utf-8
import eular2

if __name__ == "__main__":
    print('Eular Problem 25:')

    for i, x in enumerate(eular2.fibonacci()):
        if len(str(x)) >= 1000:
            print('Term {} has over 1000 digits!'.format(i+1))
            break
