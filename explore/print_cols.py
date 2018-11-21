from explore_death import d

for i in range(4,14):
    print("# ",d['meta']['view']['columns'][i]['name'],"(",i,")")
    print("```")
    print(">>> d['meta']['view']['columns'][%d]" % i)
    print(d['meta']['view']['columns'][i])
    print(">>> d['data'][0][%d]" % i)
    print(d['data'][0][i])
    print("```")


