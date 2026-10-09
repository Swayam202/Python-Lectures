a = "abcdefabcz"

arr = [0] * 26

for i in range(len(a)):
    if a[i] != ',':
        arr[ord(a[i]) - 97] += 1

for i in range(len(arr)):
    print(chr(i + 97), " -> ", arr[i])