data = ['thols','kannagi', 'amma', 'thaatha']
def long_name(spoon):
    return len(spoon)>2
result = tuple(filter(long_name,data))
print(result)