*** Settings ***
Library           Selenium2Library

*** Test Cases ***
baidu_search
    Open Browser    http://www.baidu.com    chrome
    Input Text    id=kw    robotframework学习
    Press Key    id=kw    \\13
    sleep    6
    close Browser
