'''
run test source
'''
import os
import sys

def main():
    # suite_count = sys.argv[1]
    if os.system("robot --version"):
        robot_cmd = "robot"
    else:
        robot_cmd = "pybot"
    suite_filename = sys.argv[1]
    os.system("{} {}".format(robot_cmd, suite_filename))

if __name__ == '__main__':
    main()