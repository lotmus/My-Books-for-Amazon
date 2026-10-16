from editC import d
S=d.cutp
d.sub('“Can the distinction be maintained?”','“Can that line be held?”')
d.sub('The distinction irritated him. “Every copy','That irritated him. “Every copy')
S('Miss Ahmed described the arrivals’ current circumstances.')
S('The committee laughed. Miss Ahmed waited until it stopped.')
S('“They both have lives to get on with.')
S('That sentence appeared in the eventual public report.')
S('Fanshawe accepted responsibility with less elegance and more perspiration.','Fanshawe accepted both columns of his record, the approval and the resistance, with less elegance and more perspiration, and resigned before the finding was published.')
for s in ('“Were you deceived?” a member asked.','“Yes.”','“Were you negligent?”','Fanshawe swallowed.','“Also yes.”','He resigned before the disciplinary finding was published.'):
    S(s)
d.sub('had a lone','') if False else None
S('Saye’s cooperation was recorded but did not erase','Saye gave evidence against both Bells and faced his own proceedings. Cresswell had been arrested at the committee rooms on the twenty-third of June 1815; the charge sheet survived, and so did the constable’s entry for a brass curiosity taken from his pocket. The inquiry authorised contact only to establish his condition and offer lawful return, not to rescue him from accountability.')
S('Arthur found this untidy and correct.')
S('For a while Bell said nothing. Then he described a flood','For a while Bell said nothing. Then he said, “Leeds. The third floor,” and Arthur remembered the porridge of paper and the queue outside, and the people asked to produce what the office had drowned.')
for s in ('Arthur opened the notebook to the limited terms','Bell studied the page. “You signed that willingly.”','“I read it first.”','“And if they concealed something?”','“Then the concealment can be established without their permission.”','For the first time, Bell had no immediate reply.'):
    S(s)
S('The laboratory meetings were longer.') if False else None
S('There was some good news, some incomplete news and one answer nobody wanted.')
S('Two weeks later, an additional note was identified')
S('Beatrice prepared the reimbursement in appropriate coins.')
S('At the next case lay a facsimile of Hester’s invoice')
S('Arthur stood there longer than he intended.')
# Agnes snuffbox
import re
i=d.t.find('Agnes Strath’s papers received their own public catalogue entry.')
j=d.t.find('\n\n',i)
para=d.t[i:j]
d.t=d.t[:j]+' Among the estate’s effects an inventory of 1747 listed a snuffbox of unknown metal, which would not open. Eleanor asked for a photograph, studied it in a silence that Arthur chose not to interrupt, and then asked, courteously, that the museum leave it exactly as it was.'+d.t[j:]
# name clash Reed/Reeve
d.t=d.t.replace('Dr Reeve','Dr Hartigan').replace('Dr Salma Hartigan','Dr Salma Hartigan')
d.sub('Dr Salma Reeve','Dr Salma Hartigan',count=0) if 'Dr Salma Reeve' in d.t else None
d.t=d.t.replace('Reeve','Hartigan')
from editE import apply
apply(d)
# reader note
d.cutp('If you enjoyed this book, please consider leaving a short, honest review.','If this book made you laugh, or made you slightly nervous about the forms you signed last week, please consider leaving a short, honest review. A sentence is plenty. It helps other readers find the Department, and the Department would, for once, like to be found.')
# renumber chapters
n=[0]
def rn(m):
    n[0]+=1; return f'## {n[0]} {m.group(2)}'
d.t=re.sub(r'^## (\d+) (.+)$',rn,d.t,flags=re.M)
print('chapters',n[0]); print('fail',d.fail)
d.save('/workspace/histcorr/rev2/rev2.md')
w=len(re.sub(r'#','',d.t).split()); print('words',w)
