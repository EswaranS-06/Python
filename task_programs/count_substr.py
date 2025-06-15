def count_substring(s, b):
    s = ''.join(s.lower().split())
    b = ''.join(b.lower().split())
    print(s,b)
    print(s.find(b))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)