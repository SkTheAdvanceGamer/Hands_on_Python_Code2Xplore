n=int(input("Enter no of songs:"))

s=[]
i=0

while i<n:
    d=int(input("Song "+str(i+1)+" duration:"))
    s.append(d)
    i=i+1

bad=False
i=0

while(i<n):
    if s[i]<=0:
        bad=True
    i=i+1

if bad==True:
    print("Total:N/A")
    print("Songs:",n)
    print("Category:Invalid Playlist")
    print("Recommendation:One or more durations are wrong fix them")

else:
    t=0
    for x in s:
        t=t+x

    seen=[]
    for x in s:
        if x not in seen:
            seen.append(x)

    rep=False
    if len(seen)<n:
        rep=True
    
    h=n//2
    f=0
    i=0
    while i<h:
        f=f+s[i]
        i=i+1

    sc=0
    j=h
    while j<n:
        sc=sc+s[j]
        j=j+1

    g=f-sc
    if g<0:
        g=g*-1

    gp=(g*100)//t

    cat=""
    rec=""

    if t<300:
        cat="Too short playlist"
        rec="Only "+str(t)+" seconds, add more songs to reach atleast 300"
    elif t>3600:
        cat="Too long playlist"
        rec=str(t)+" seconds is to long, maybe split the playlist"
    elif rep==True:
        cat="Repetetive playlist"
        rec="Some songs have same length, swap them with diffrent ones"
    elif gp<=20:
        cat="Balanced playlist"
        rec="Both halves match well, great listening session"
    else:
        cat="Irregular playlist"
        rec="One half is much longer than other, try reodering the songs"

    print("Total Duration:",t,"seconds")
    print("Songs:",n)
    print("Category:",cat)
    print("Recommendation:",rec)