
"""
wait(Pattern("Paste.png").similar(0.91), 120) or wait("Paste-1.png", 120)
popup('PASS')"""




while not(find("Paste.png") or find("Paste-1.png")):
    sleep(1)   
popup('PASS')


"""
while not(wait("Paste-1.png",1) or wait("Paste.png",1)):
    sleep(1)    
popup('PASS')"""