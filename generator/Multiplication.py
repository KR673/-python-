def multiplication(n):
    print('\n'.join(['\t'.join(['%dx%d=%d' % (x, y,x * y) for x in range(1, y + 1)]) for y in range(1, n)]))

if __name__ == '__main__':
    multiplication(10)