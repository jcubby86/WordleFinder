import time
import sys

def main(words, offset):
    t_seconds = int(time.time())
    t_minutes = (t_seconds // 60)
    t_hours = (t_minutes // 60) - 7 # Time Zone
    t_days = (t_hours // 24) + offset
    print(words[(t_days - 18797)])

if __name__ == '__main__':
    main([x[1:-1] for x in open('words.txt', 'r').readline().split(', ')], 0 if len(sys.argv) < 2 else int(sys.argv[1]))