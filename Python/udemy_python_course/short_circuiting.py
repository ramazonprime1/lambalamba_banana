# Short Circuiting

is_friend = True
is_user = True

if is_friend and is_user: #Short circuited when is_friend is False
   print ('bffs \n')

if is_friend or is_user: #Short circuited when is_friend is True
    print ('bffs not')