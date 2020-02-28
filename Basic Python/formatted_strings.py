# Formatted Strings

userName = 'shanjinur'
lastLogin = 'Yesterday'

# Method 1

print(f'Welcome back {userName}, your last Login was on {lastLogin}') # f tells python it is a formatted string

# Method 2

print('Log out, {} ?'.format(userName))

# Method 3 

print('good bye, {user}'.format(user=userName))
print('Copyright {com} @ {year}'.format(com='Facebook',year=2020))