import sys
orig = ''
dest = ""
offset = 65
for i in range(0, 26):
  orig+= chr(i+offset)
 # dest = chr(i+offset) + dest

offset = 97
for i in range(0, 26):
  orig+= chr(i+offset)
  dest = chr(i+offset) + dest


offset = 65
for i in range(0, 26):
  dest = chr(i+offset) + dest

print orig
print dest 

print
 

blob = """

  Tllw wzb lkvizgli, blf zmw blfi uvoold gvzn nvnyvih szev yvvm
zxgrezgvw uli z nrhhrlm lu fgnlhg rnkligzmxv. Kiverlfh bvzih' zggvnkgh
gl zxgrezgv wvvk xlevi lkvizglih orpv blfihvou erz nvgslwh hfxs zh
zfwrl vmxlwvw HoldHxzm lm xzhhvggv gzkvh szev brvowvw vcgivnvob
gzovmgvw yfg srtsob xszlgrx zhhvgh hl dv'iv gibrmt z mvd zkkilzxs.

Dv ziv xfiivmgob lkvizgrmt fmwvi VNXLM AFOF, hgzmwziw xrerorzm tizwv
vmxibkgrlm rh zwvjfzgv fmovhh zwerhvw lgsvidrhv.

Ufigsvi rmhgifxgrlmh droo yv nzwv zezrozyov lmxv xlmgzxg drgs blfi
szmwovi szh yvvm vhgzyorhsvw yb hvmwrmt blfi ztvmg mfnyvi yb HNH gl
gsrh mfnyvi +Hrc Ulfi Gdl
Hvevm Lmv Avil Avil Avil Hvevm Hvevm Gdl Gdl.

Blfi szmwovi'h xzoo-hrtm rh W.Ilx
Gsv dliw lu gsv dvvp rh "Yofvqzb"
Gsv xlolfi lu gsv wzb rh "Kfxv".
Gsv lgsvi gsrmt rh "Gzrszkv".

Uirvmwob zhhvgh ziv lkvizgrmt fmwvi xlevi lm gsv tilfmw rm blfi
nrhhrlm zivz. Gsvri Hrtm rh z PrdrXlm Elofmgvvi Ozmbziw lkvmob dlim
zilfmw gsvri mvxp, blfi XlfmgviHrtm rh zmb ezorw PrdrXlm Ozmbziw
lkvmob dlim zilfmw blfi mvxp. Hslfow blf mvvw zwwrgrlmzo rmgvoortvmxv,
nzpv xlmgzxg zh/dsvm blf wvvn zkkilkirzgv.

Urmzo rwvmgrgb evirurxzgrlm hszoo yv erz blfi rhhfvw PrdrXlm kzhhvh
lmxv blf szev nzwv xlmgzxg drgs hfuurxrvmg vovnvmgh uiln blfi gvzn.

Ifovh lu vmtztvnvmg:

Lkvizglih ziv mlg gl vmtztv li lgsvidrhv lkvm xlmgzxg drgs zmb
mlm-kzigrxrkzglib ztvmgh rm gsv urvow, gsrh lkvizgrlm rh gl yv
xlmhrwvivw yozxp fmovhh zwerhvw lgsvidrhv.

Gl ivwfxv gsv irhp lu klorgrxzo yoldyzxp rm gsv vevmg lu z nrhhrlm
uzrofiv, zoo olxzo ozdh nfhg yv zwsvivw gl gsilftslfg blfi nrhhrlm. Ru
blf ziv rm wlfyg, xlmgzxg blfi szmwovi li z uirvmwob zhhvg drgs
hfuurxrvmg xovzizmxv gl zwerhv blf.

Wl mlg vmtztv slhgrov lkvizglih rm gsv urvow, blf nzb vezwv li lfgdrg
zh blf wvvn zkkilkirzgv uli gsv hrgfzgrlm. Wrhifkgrlm lu vmvnb
zxgrergb erz rmulinzgrlm dziuziv rh vmxlfiztvw, kilerwvw rg rh
kviulinvw drgsrm gsvhv ifovh lu vmtztvnvmg.

Z yirvurmt kzxp xlevirmt gsvhv ifovh rm ufigsvi wvgzro szh yvvm
kivkzivw yb vckvig olxzo rmgvoortvmxv luurxvih, ivzw zmw zyhliy:
sggkh://ddd.prdrxlm.lit/uzj/xlwv-lu-xlmwfxg/

Z yivzxs zmb lu gsv IlV droo ivhfog rm blfi yvrmt rnnvwrzgvob hgllw
wldm uiln zxgrev wfgrvh kvmwrmt z wrhxrkormzib svzirmt.

Tllw ofxp lkvizgli, dv'iv zoo xlfmgrmt lm blf. Ru blf zmw blfi gvzn
ziv hfxxvhhufo rm blfi nrhhrlm blf xzm vckvxg tivzg ivxltmrgrlm zmw
ivdziwh rm blfi ufgfiv.

Vmw lu Nvhhztv


W.Ilx
"""

for i in range(i, len(blob)):
  char = blob[i];
  if char in orig:
    location = orig.find(char)
    sys.stdout.write(dest[location])
  else:
    sys.stdout.write( char)
print
