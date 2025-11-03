import sys
def explore_sys_module():
    print(f"\nsys.argv: {sys.argv}")
    print(f"\nsys.path (first 5 entries): {sys.path[:5]}...")
    print(f"\nsys.version: {sys.version}")
    print(f"\nsys.platform: {sys.platform}")
    print(f"\nsys.byteorder: {sys.byteorder}")
    initial_recursion_limit = sys.getrecursionlimit()
    print(f"\nInitial recursion limit: {initial_recursion_limit}")
    my_list = [1, 2, 3, "hello"]
    print(f"\nSize of my_list: {sys.getsizeof(my_list)} bytes")
    sys.stdout.write("This is written to standard output.\n")
    sys.stderr.write("This is written to standard error.\n")
explore_sys_module()