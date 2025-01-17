

def calculation_span(price, s):
    n = len(price)
    
    st = []
    st.append(0)

    
    s[0] = 1

    
    for i in range(1, n):
        
        
        while len(st) > 0 and price[st[0]] <= price[i]:
            st.pop()

        
        
        
        
        s[i] = i + 1 if len(st) <= 0 else (i - st[0])

        
        st.append(i)



def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")



price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price) + 1)]


calculation_span(price, S)


print_array(S, len(price))
