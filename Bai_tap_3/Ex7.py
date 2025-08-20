# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.

def not_poor_replace(s):
    not_pos = s.find("not") #tra ve vi tri cua 'not'
    poor_pos = s.find("poor") #tra ve vi tri cua 'poor'

    if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos: #neu co ca not va poor va not dung truoc poor
        s = s[:not_pos] + "good" + s[poor_pos + 4:]  #vi len(poor)=4
    return s


my_string = input("Enter your string: ")
print(not_poor_replace(my_string))
