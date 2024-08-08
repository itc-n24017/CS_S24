def list_average(x):
    try:
        return sum(x)/len(x)
    except:
        print('list_length:', len(x))
        return None

print(list_average([4.1, 2.5, 2,3]))
print(list_average([]))

