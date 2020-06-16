

# 生产消费模式
# 生产者
# 提供数据的一方

# 消费者
# 拿到数据之后写入文件也好,写入数据库也好


def consumer():
    """消费者"""
    print("消费者需要消费(ps:写入数据了..)")
    # 消费结果
    r = ''
    while True:
        # 交出方法执行权给生产者
        # 商品n (数据)
        n = yield r
        # 如果没有商品(数据)
        if not n:
            return

        print("消费者 消费...... %s......." % n)
        r = '消费完毕 ok!'


def product(consumer):
    """生产者"""
    print("--------------生产者-------------")
    # 1. 启动生成器对象
    next(consumer)
    # 2. 商品
    n = 0
    # 3. 生产商品的流程
    while n < 5:
        n += 1
        print("生产者 生产了.......%s........" % n)
        # 此时已经生产了一件商品
        # 此时需要把方法的执行权交给 消费者
        # 表示从n开始 直接是给yield后面赋值
        # 相比于生成器函数 生成器函数是直接给定一个值，然后从这个范围里一个一个yield 但是这里yield的值是由生产者send
        r = consumer.send(n)
        print("生产者 售卖商品 得到.......%s......." % r)


# 1. 创建生成器对象
c = consumer()
# 2. 启动生成器
product(c)

# 总结:
# 1. 生产者 启动生成器对象(消费者) 通过next() 方法的执行权会交给生成器对象(消费者)
# 2. 一旦遇见yield关键字, 就会把方法执行权交给生产者(上次交还给消费者的位置) => next()返回值这里
# 3. 当生产者生产出商品后, 通过send方法将方法的执行权再次交还给消费者 => yield x
# 4. 消费者消费, 返回消费结果给生产者 (通过yield)
# 5. 方法的执行权再次交给生产者 => 即send() 这个位置
# 6. 然后反复执行,直到没有商品 整个过程中止
