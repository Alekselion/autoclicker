def autotest(fun, inp:list, out:list, verbose=False):
    """ Arguments:
            fun: function to be tested.
            inp: input for function.
            out: expected function output.

        Return:
            True if all tests is done. 
            Otherwise False.
    """
    if verbose:
        name = str(fun).split()[1]
        print(f"\n\n{'-' * (len(name) + 7)}")
        print(f"Test {name}()\n{'-' * (len(name) + 7)}\n")
    
    assert len(inp) == len(out), "The amount of input data does not match the amount of output data."

    # ############################################################################
    # FIX: если тестируемая функция принимает более 1 аргумента, автотест ломается
    # ############################################################################

    count = 0
    verdict = True
    for case in range(len(inp)):
        i = inp[case]
        o = out[case]
        res = fun(i)
        test = "done" if res == o else "fail"
        count += 1

        if test == "fail":
            verdict = False
            print(f"Case {count}:\n\tinput: {i}\n\texpected: {o}\n\toutput: {res}\n\tverdict: {test}\t<---")
        elif verbose:
            print(f"Case {count}:\n\tinput: {i}\n\texpected: {o}\n\toutput: {res}\n\tverdict: {test}")

    return verdict


if __name__ == "__main__":
    def double(a):
        return a * 2


    testInput = [1, 2, 3, 4, 5]
    testOutput = [2, 4, 6, 8, 10]
    print(autotest(double, testInput, testOutput, False))  # тихий режим без fail
    
    testInput = [1, 2, 3, 4, 5]
    testOutput = [2, 4, 6, 8, 10]
    print(autotest(double, testInput, testOutput, True))  # вывод процесса без fail


    def triple(a):
        return a * 2 if a % 2 == 0 else a * 3


    testInput = [1, 2, 3, 4, 5]
    testOutput = [3, 6, 9, 12, 15]
    print(autotest(triple, testInput, testOutput))  # тихий режим с fail
    
    testInput = [1, 2, 3, 4, 5]
    testOutput = [3, 6, 9, 12, 15]
    print(autotest(triple, testInput, testOutput, True))  # вывод процесса c fail
    

    def diff(a, b):
        return a - b


    # testInput = [1, 2, 3, 4, 5]
    # testOutput = [0, 0]
    # print(autotest(triple, testInput, testOutput, True))  # кол-во входов != кол-ву выходов

    # testInput = [(5, 4), (3, 3), (1, 3)]
    # testOutput = [1, 0, -2]
    # print(autotest(diff, testInput, testOutput, True))  # передача в функцию более 1-го параметра
