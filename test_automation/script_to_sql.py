def script_to_sql(script):
    settings = []
    cases = {}
    case_name = ''
    set_flag = 0
    case_flag = 0
    for line in script:
        if len(line) == 0:
            continue
        elif "*** Settings ***" in line:
            set_flag = 1
            case_flag = 0
        elif "*** Test Cases ***" in line:
            set_flag = 0
            case_flag = 1
        else:
            if set_flag == 1:
                settings.append(line)
            if case_flag == 1:
                if line[0] != ' ':
                    case_name = line.strip('\n')
                    cases[case_name] = ""
                else:
                    cases[case_name] += line
    print(settings)
    print(cases)
    return settings, cases

script = '''
*** Settings ***

Library           Selenium2Library



*** Test Cases ***

baidu_search

    Open Browser    http://www.baidu.com    chrome

    Input Text    id=kw    robotframework学习

    Press Key    id=kw    \\13

    sleep    6

    close Browser
'''

if __name__ == '__main__':
    script_to_sql(script.split('\n'))