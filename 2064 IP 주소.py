# 주어진 거 and 연산으로 네트워크 주소 찾고
# 주어진 거 or 연산으로 최대 값 찾아서 네트워크 주소와 xor 연산 한 값을 255에서 빼면됨
def solution():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split('.'))))

    mask_flag = False
    network_flag = False
    networkAddress = []
    maskAddress = []
    for i in range(4):
        networkCurrent = arr[0][i]
        maskCurrent = arr[0][i]
        if mask_flag:
            networkAddress.append(0)
            maskAddress.append(0)
        else:
            for j in range(1, n):
                if networkCurrent != arr[j][i]:
                    network_flag = True
                networkCurrent = networkCurrent & arr[j][i]
                maskCurrent = maskCurrent | arr[j][i]
            maskCurrent = 255 - (maskCurrent ^ networkCurrent)
            if network_flag:
                temp = bin(networkCurrent)
                len_temp = len(temp)
                if len_temp < 10:
                    temp = '0b' + '0' * (10 - len_temp) + temp[2:]
                for i in range(2, 10):
                    if temp[i] == 0:
                        temp = temp[:i] + '0' * (10 - i)
                networkCurrent = int(temp, 2)
            if maskCurrent != 255:
                temp = bin(maskCurrent)
                len_temp = len(temp)
                if len_temp < 10:
                    temp = '0b' + '0' * (10 - len_temp) + temp[2:]
                for i in range(2, 10):
                    if temp[i] == 0:
                        temp = temp[:i] + '0' * (10 - i)
                maskCurrent = int(temp, 2)
                mask_flag = True

            networkAddress.append(networkCurrent)
            maskAddress.append(maskCurrent)
    print(".".join(map(str, networkAddress)))
    print(".".join(map(str, maskAddress)))


solution()