def change(minutes):
    hour = divmod(int(minutes), 60)
    return str(hour[0]) + 'h' +str(hour[1]) + 'min'


if __name__ == '__main__':
    while True:
        min = raw_input('>enter the minutes,enter q to quit ')
        if min == 'q':
            break
        else:
            print change(min)