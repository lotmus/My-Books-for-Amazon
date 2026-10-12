import sys, os, json, urllib.request
import gen
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Step_Stories_Pics_New")
STYLE="Rich, highly detailed oil-painting style classic fantasy storybook illustration, textured brushwork, moody natural light, no text, no lettering. "
P={"f09_shadow":STYLE+"Dawn, thin mist over a wide wet field and bog, a small stone mill with a water wheel far in the distance. A single impossibly long thin shadow of a tall man in a long coat carrying a bag lies stretched across the grass toward the mill, but NOBODY is standing where the shadow starts; one line of footprints in the dew simply stops. The foreground is empty grass and puddles. Eerie and still, gentle enough for children. ABSOLUTELY NO person, figure, face, ghost, child or animal anywhere in the picture."}
P["h05_hollin_brook"]=STYLE+"Afternoon at the burnt-out old mill of Hollin Brook: black charred timbers and a half-burned water wheel against a grey-gold sky, a lone chimney. A family of four, mother, father, a boy and a girl with a puppy, sit close together on a hay cart outside the ruins wrapped in blankets with a few saved belongings, looking at the ruins with sorrow but holding hands, relieved they all got out. Neighbours bring them a pot of soup. No ghost, no other children, no cartoon, gentle and truthful."
for n in sys.argv[1:]:
    body={"model":"grok-imagine-image-quality","prompt":P[n],"aspect_ratio":"3:2","resolution":"1k"}
    req=urllib.request.Request("https://api.x.ai/v1/images/generations",data=json.dumps(body).encode(),headers={"Authorization":"Bearer "+gen.key(),"Content-Type":"application/json","User-Agent":"StepStories/1.0"})
    r=json.load(urllib.request.urlopen(req,timeout=300)); it=r["data"][0]
    open(os.path.join(OUT,n+".jpg"),"wb").write(urllib.request.urlopen(urllib.request.Request(it["url"],headers={"User-Agent":"Mozilla/5.0"}),timeout=300).read()); print(n,"ok")
