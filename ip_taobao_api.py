import requests
import time
import sys
globals = {
    'true': 0,
    'false': 1
}

headers = {
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate"
    }

def main(input):
    count = 0
    with open(input,'r') as f1:
        line = f1.read().splitlines()
        arry_ip = line
    for i in arry_ip:
        count+=1
        time.sleep(2)
        try:
            print(count)
            results =requests.get(url='http://ip-api.com/json/'+i,headers=headers)
            results = eval(str(results.json()),globals)
            print(results['query'],results['country'],results['regionName'],results['city'],results['isp'],results['org'])
            with open('ip_drr.txt', 'a') as f2:
                f2.write(str(results['query']) + ':' + str(results['country']) + ':' + str(results['regionName']) + ':' + str(results['city']) +':' +str(results['isp'])+ ':' +str(results['org']) + '\n')
        except:
            print(count)
            print(i+'   NO')
def run():
    print('start...............')
    if len(sys.argv)<2:
        print('Usage: python3 IP_taobao_api.py [ip.txt]')
    else:
        try:
            ip = sys.argv[1]
            main(ip)
        except:
            print('请在当前目录下创建ip.txt，并写入ip')
if __name__ == '__main__':
    run()

