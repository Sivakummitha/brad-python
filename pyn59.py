import itertools
import operator
for i in itertools.islice(itertools.count(1,2),5):
    print(i)
for i,x in zip(range(6),itertools.cycle(['a','b','c'])):
    print(x)
for i in itertools.repeat('hi',3):
    print(i)
nums=[1,2,3,4,5]
print(list(itertools.accumulate(nums)))
print(list(itertools.accumulate(nums,operator.mul)))
print(list(itertools.chain.from_iterable([[1, 2], [3, 4]])))
print(list(itertools.compress(['a', 'b', 'c', 'd'], [1, 0, 1, 0])))
print(list(itertools.dropwhile(lambda x: x < 5, [1, 3, 6, 2, 8, 4])))
print(list(itertools.takewhile(lambda x: x < 5, [1, 3, 6, 2, 8, 4])))
print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))
print(list(itertools.islice(range(10), 2, 8, 2)))
pairs = [(2, 5), (3, 2), (10, 3)]
print(list(itertools.starmap(pow, pairs)))
a, b = itertools.tee([10, 20, 30], 2)
print(list(a))
print(list(b))
print(list(itertools.zip_longest([1, 2, 3], ['a', 'b'], fillvalue='-')))
print(list(itertools.product([1, 2], ['a', 'b'])))
print(list(itertools.permutations([1, 2, 3], 2)))
print(list(itertools.combinations([1, 2, 3, 4], 2)))

 