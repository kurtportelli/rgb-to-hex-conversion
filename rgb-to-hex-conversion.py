def rgb(r, g, b):
    rounded = []
    for num in [r, g, b]:
        if num > 255: rounded.append(255)
        if num < 0: rounded.append(0)
        if 0 <= num <= 255: rounded.append(num)
    return '{0:02X}{1:02X}{2:02X}'.format(rounded[0], rounded[1], rounded[2])
