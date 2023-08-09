from pytube import Search

'''
classes for youtube selection and data handling
'''


def search_vids(search_term,stack):
    stack_strength=len(stack)
    result=Search(search_term)
    if stack_strength==0:
        j=0
        for i in result:
            stack[j]==i[-12:-1]
            j+=1
            
    else:
        j=len(stack)
        for i in result:
            stack[j]=i[-12:-1]

    return stack


