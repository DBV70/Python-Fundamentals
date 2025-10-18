version = list(map(int, input().split('.')))
version[2] += 1
if version[2] > 9:
    version[2] = 0
    version[1] += 1
    if version[1] > 9:
        version[1] = 0
        version[0] +=1

version = map(str, version)
print('.'.join(version))

'Alternative solution'
version = input().split('.')
version_int = int(''.join(version))
version_int += 1
version_list = list(str(version_int))
print('.'.join(version_list))