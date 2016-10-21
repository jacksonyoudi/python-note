def psychoologist():
    print 'Please tell me your problems'
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print ("Don't ask yourself too much questions")
            elif 'good' in answer:
                print  "A that's good, go on"
            elif 'bad' in answer:
                print "Don't be so negative"

send是向yield中传递数据

send的工作机制与next一样，但是yield将变成能够返回传入的值。因而，这个函数可以更具客户端代码来修改其行为。
同事，还添加了throw和close两个函数，以完成该行为。

同时，还添加了throw和close连个函数，已完成该行为。它们会相爱相生成器抛出一个错误。
throw允许客户端代码传入要抛出的任何类型的异常
close的工作方式是相同的，打死将会抛出一个特定的异常----GeneratorExit,在这种情况下，生成器函数必须
再次抛出GeratorExit或StopIteration异常

def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print "ok let's clean"
