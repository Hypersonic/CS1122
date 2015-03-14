import datetime

entries = []

def add_entry(time, name):
    entries.append((time, name))

def entries_to_str(entries):
    return '\n'.join([str(a) + "," + str(b) for a,b in entries])

if __name__ == '__main__':
    try:
        while True:
            name = raw_input()
            time = datetime.datetime.now()
            add_entry(time, name);
    except KeyboardInterrupt:
        try:
            with open("attendance.csv"):
                had_file = True
        except IOError:
            had_file = False
        with open("attendance.csv", 'a') as f:
            if not had_file:
                f.write("time,name\n")
            else:
                f.write("\n")
            f.write(entries_to_str(entries))
