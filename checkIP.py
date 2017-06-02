# -*- coding:utf-8 -*-
class Solution():
    def CheckIP(self, ip):
        if not ip:
            return False
        address = ip.strip().split('.')
        if len(address) != 4:
            return False
        for i in range(4):
            if address[i][0] == '0' and len(address[i]) > 1:
                return False
            if address[i][0] == ' ' and len(address[i]) >= 1:
                return False
            try:
                address[i] = int(address[i])
            except ValueError:
                return False
        for a in address:
            if a < 0 or a > 255:
                return False
        return True
