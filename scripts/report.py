import os
'''
parse output to result and report result to server
'''
def parse():
    '''
    example:
    results = {"job_name":"test",
             "build_id":1,
            "cases":[
            {"name": "t1",
            "status": 0,
            "build_time": 158678992,
            "url": "http://127.0.0.1/static/log.html#s1-t1"}
            ]}
    :return:
    '''
    results = {}
    output = "D:/project/shaka/.edit/workspace/test/"
    output_xml = os.path.join(output, "output.xml")
    with open(output_xml, encoding='utf8') as f:
        data = f.read()
    print(data)
    return results

def report(results):
    pass

def main():
    parse()

if __name__ == '__main__':
    main()
