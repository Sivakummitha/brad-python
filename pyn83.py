try:
    import notmodule
    nums = [1, 2, 3]
    print(nums[5])
    data = {"name": "Siva"}
    print(data["age"])
    print("Press Ctrl+C to raise KeyboardInterrupt")
    while True:
        pass
except ImportError:
    print("ImportError occurred")
except IndexError:
    print("IndexError occurred")
except KeyError:
    print("KeyError occurred")
except KeyboardInterrupt:
    print("KeyboardInterrupt occurred")
finally:
    print("Program finished")
