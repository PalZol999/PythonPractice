import webbrowser, sys, pyperclip

sys.argv # ['maypit.py', '870', 'Valencia', 'St'] it's a list value that you enter in the Windows+R

if len(sys.argv) > 1:
    # ['maypit.py', '870', 'Valencia', 'St']
    address= ' '.join(sys.argv[1:])   #it gonna join the list with ' ' form the index num 1
else:
    address = pyperclip.paste()
    
#https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address) 