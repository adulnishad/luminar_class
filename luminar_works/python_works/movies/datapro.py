from json import load


path="C:\\Users\\VICTUS\\OneDrive\\Desktop\\adulpy\\movies\\mdb.json"

with open(path,encoding="utf-8")as f:
    filims=load(f)
# print(len(filims)) 
   
#print movies in 2015 
movie_filter=[f.get("title") for f in filims if f.get("year")=="2015"]
# print(movie_filter)



# printfunny movies
funny_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
# print(funny_movies)



# movie runtime
runtime_movies=[f.get("title") for f in filims if f.get("id") in range(20,31) and f.get("runtime")>="110"]
# print(runtime_movies)


title_filter=[f.get("title")for f in filims if len(f.get("title").split(" "))==1]
# print(title_filter)

highest_runtime=[f for f in filims if "Drama" in f.get("genres")]
lengthy_movie=max(highest_runtime,key=lambda f:int(f.get("runtime")))
# print(lengthy_movie)


# print all geners
wc={}
for m in filims:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
# out=max(wc,key=lambda k:wc.get(k)) 
# print(out)               



# print year highest no movie names


print(max((v,k) for k,v in wc.items()))

