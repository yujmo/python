def gen():
    yield from subgen()
    def subgen():
        while True:
            x = yield
            yield x + 1
def main():
    g = gen()
    next(g)
    retval = g.send(1)
    print(retval)
    g.throw(StopIteration)

main()
