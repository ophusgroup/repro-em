"""Patch the downloaded book-theme template: replace the dialog-based
search with a flat top-bar input, and optionally keep top-level TOC
sections expanded.

Ported from quantem-docs. The stock theme's search opens a modal dialog,
and it opens a sidebar section only while that section contains the
active page (re-collapsing it on navigation). There are no template
options for either, so we patch the compiled bundles in _build/templates.
Run after the template has been downloaded (any `myst build` or `myst
start` does that), and re-run whenever _build is cleared:

    python3 scripts/patch_theme.py

The deploy workflow runs this between a warm-up build and the real build.
"""

import hashlib
import os
import re
import sys

# With 30+ pages the fully-expanded sidebar runs several screens long, so
# we keep the stock behaviour: a section is open only while you are inside
# it. Set True to pin every top-level section open instead.
"""Sidebar sections whose URL contains one of these strings are expanded on
first paint instead of only while you are inside them. Empty list = the stock
behaviour, where every section stays collapsed until visited. The framework is
the spine of the site, so it is worth showing its steps without a click."""
EXPAND_SECTIONS_MATCHING = ["framework"]

HERE = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.normpath(
    os.path.join(HERE, "..", "_build", "templates", "site", "myst", "book-theme")
)

TARGETS = [
    os.path.join(THEME, "build", "index.js"),
    os.path.join(THEME, "public", "build", "_shared", "chunk-RUUCG5OS.js"),
]

# Flat top-bar search runtime (replaces the theme's dialog search).
# Injected into the server-rendered HTML. The search index path is
# resolved relative to the current page so it also works when the site
# is served under a path prefix (GitHub Pages project sites).
_RUNTIME = """
;(function(){
  /* ---------- flat top-bar search (replaces the theme's dialog) -------- */
  var idx=null,loading=false,waiters=[],base='';
  /* Record URLs in the index are written from the site root ('/modules/...')
     with no path prefix, so on a GitHub Pages project site they have to be
     prefixed or every hit lands on the 404 page. The prefix that serves the
     index is the prefix the pages live under, so probe for it and keep it. */
  function basePrefixes(){
    var seg=window.location.pathname.split('/').filter(Boolean);
    return seg.length?['/'+seg[0],'']:[''];
  }
  function href(u){
    return (u&&u.charAt(0)==='/')?base+u:u;
  }
  function load(cb){
    if(cb&&idx)return cb();
    if(cb)waiters.push(cb);
    if(idx||loading)return;
    loading=true;
    var pre=basePrefixes();
    function attempt(i){
      if(i>=pre.length){loading=false;waiters=[];return;}
      fetch(pre[i]+'/myst.search.json').then(function(r){
        if(!r.ok)throw new Error('http '+r.status);
        return r.json();
      }).then(function(d){
        idx=d.records||[];base=pre[i];loading=false;
        var w=waiters;waiters=[];w.forEach(function(f){f();});
      }).catch(function(){attempt(i+1);});
    }
    attempt(0);
  }
  function titleOf(h){
    return [h.lvl3,h.lvl2,h.lvl1].filter(Boolean)[0]||'';
  }
  function crumbOf(h){
    return [h.lvl1,h.lvl2,h.lvl3].filter(Boolean).join(' > ');
  }
  function search(q){
    if(!idx)return [];
    var terms=q.toLowerCase().split(/\\s+/).filter(Boolean);
    if(!terms.length)return [];
    var seen={},out=[];
    idx.forEach(function(rec){
      var h=rec.hierarchy||{};
      var title=titleOf(h),crumb=crumbOf(h);
      var hay=(crumb+' '+(rec.content||'')).toLowerCase();
      var titleHay=crumb.toLowerCase();
      var score=0;
      for(var i=0;i<terms.length;i++){
        if(hay.indexOf(terms[i])<0)return;
        if(titleHay.indexOf(terms[i])>=0)score+=3;
        score+=1;
      }
      if(rec.type!=='content')score+=2;
      var key=rec.url;
      if(seen[key]!==undefined){
        if(out[seen[key]].score>=score)return;
        out[seen[key]]={score:score,url:rec.url,title:title,crumb:crumb,
                        content:rec.content||''};
        return;
      }
      seen[key]=out.length;
      out.push({score:score,url:rec.url,title:title,crumb:crumb,
                content:rec.content||''});
    });
    out.sort(function(a,b){return b.score-a.score;});
    return out.slice(0,8);
  }
  function build(bar){
    if(!bar||bar.dataset.rpeSearch)return;
    bar.dataset.rpeSearch='1';
    var wrap=document.createElement('div');
    wrap.className='rpe-search';
    var input=document.createElement('input');
    input.type='search';
    input.placeholder='Search';
    input.setAttribute('aria-label','Search this site');
    var list=document.createElement('div');
    list.className='rpe-search-results';
    list.hidden=true;
    wrap.appendChild(input);
    wrap.appendChild(list);
    bar.style.display='none';
    bar.after(wrap);
    var active=-1,hits=[];
    function render(){
      list.innerHTML='';
      if(!hits.length){list.hidden=true;return;}
      hits.forEach(function(h,i){
        var a=document.createElement('a');
        a.href=href(h.url);
        a.className='rpe-search-hit'+(i===active?' active':'');
        var t=document.createElement('div');
        t.className='rpe-search-hit-title';
        t.textContent=h.crumb||h.title;
        a.appendChild(t);
        if(h.content){
          var c=document.createElement('div');
          c.className='rpe-search-hit-text';
          c.textContent=h.content.slice(0,110);
          a.appendChild(c);
        }
        list.appendChild(a);
      });
      list.hidden=false;
    }
    function run(){
      active=-1;
      hits=search(input.value.trim());
      render();
    }
    input.addEventListener('focus',function(){load();});
    input.addEventListener('input',function(){
      load(run);   // re-runs once the index finishes loading
      run();
    });
    input.addEventListener('keydown',function(ev){
      if(ev.key==='ArrowDown'||ev.key==='ArrowUp'){
        ev.preventDefault();
        if(!hits.length)return;
        active=(active+(ev.key==='ArrowDown'?1:-1)+hits.length)%hits.length;
        render();
      }else if(ev.key==='Enter'){
        var h=hits[active<0?0:active];
        if(h){ev.preventDefault();window.location.href=href(h.url);}
      }else if(ev.key==='Escape'){
        input.value='';hits=[];render();input.blur();
      }
    });
    document.addEventListener('click',function(ev){
      if(!wrap.contains(ev.target)){hits=[];render();}
    });
    document.addEventListener('keydown',function(ev){
      if((ev.metaKey||ev.ctrlKey)&&ev.key.toLowerCase()==='k'){
        ev.preventDefault();ev.stopPropagation();input.focus();input.select();
      }
    },true);
  }
  /* ---------- COLab logo at the bottom of the left sidebar ---------- */
  function logoTick(){
    var toc=document.querySelector('.myst-primary-sidebar-toc');
    if(!toc||!toc.parentElement)return;
    if(toc.parentElement.querySelector('.rpe-group-side'))return;
    var a=document.createElement('a');
    a.className='rpe-group-side';
    a.href='https://colab.stanford.edu/';
    a.target='_blank';
    a.rel='noopener';
    [['rpe-group-light','__LOGO_LIGHT__'],['rpe-group-dark','__LOGO_DARK__']]
      .forEach(function(v){
        var img=document.createElement('img');
        img.className=v[0];
        img.alt='COLab, Stanford University';
        img.src=v[1];
        a.appendChild(img);
      });
    toc.after(a);
  }

  function tick(){
    build(document.querySelector('button.myst-search-bar'));
    logoTick();
  }
  function start(){
    tick();
    // React hydration replaces these nodes, so keep re-checking for a while
    var n=0,iv=setInterval(function(){tick();if(++n>40)clearInterval(iv);},250);
    new MutationObserver(function(){tick();}).observe(
      document.documentElement,{subtree:true,childList:true});
  }
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',start);
  }else{start();}
})();
"""

def _data_uri(path):
    import base64
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
_RUNTIME = _RUNTIME.replace(
    "__LOGO_LIGHT__", _data_uri(os.path.join(ASSETS, "colab-logo-light.png"))
).replace(
    "__LOGO_DARK__", _data_uri(os.path.join(ASSETS, "colab-logo-dark.png"))
)

# The marker embeds a hash of the runtime, so editing the code above is
# enough to make the next patch run replace an older injected copy.
INLINER_MARK = (
    "/*rpe-runtime-" + hashlib.sha1(_RUNTIME.encode()).hexdigest()[:8] + "*/"
)
INLINER = INLINER_MARK + _RUNTIME

# Suffix for the renamed client entry + manifest. It has to change whenever
# the patched output changes: the theme serves these with a 1-year immutable
# cache header, so reusing a suffix means browsers keep replaying whatever
# they cached under that name.
CACHE_TAG = "RPE" + hashlib.sha1(
    (INLINER + repr(EXPAND_SECTIONS_MATCHING)).encode()
).hexdigest()[:6].upper()


# Matches the collapsible-section state hook in both the server and client
# bundles (minified variable names differ between them):
#   [s,o]=X.useState(r); useEffect(()=>{n.state==="idle"&&o(r)},[n.state]);
#   let a=fn(e,i,t); return !i.children ...
PATTERN = re.compile(
    r'\[(\w),(\w)\]=([\w$]+(?:\.default)?)\.useState\((\w)\);'
    r'\(0,([\w$]+)\.useEffect\)\(\(\)=>\{(\w)\.state==="idle"&&\2\(\4\)\},'
    r'\[\6\.state\]\);let (\w)=[\w$]+\(([^)]*)\);return!(\w)\.c'
)


MARKER = ".title||'')).indexOf('"


def patched(src):
    def repl(m):
        s, o, hook, active, eff, nav, let_var, fn_args, heading = m.groups()
        # The TOC item exposes different fields in the server and client
        # bundles, so match against url, id and title together.
        key = f"(({heading}.url||'')+({heading}.id||'')+({heading}.title||''))"
        tests = "||".join(
            f"{key}.indexOf('{p}')>=0" for p in EXPAND_SECTIONS_MATCHING
        )
        keep_open = f'({tests}||{active})'
        return (
            f'[{s},{o}]={hook}.useState({keep_open});'
            f'(0,{eff}.useEffect)(()=>{{{nav}.state==="idle"&&{o}({keep_open})}},'
            f'[{nav}.state]);let {let_var}='
            + m.group(0).split(f'let {let_var}=', 1)[1]
        )

    return PATTERN.subn(repl, src)


def main():
    if not os.path.isdir(THEME):
        sys.exit("book-theme template not found; run `myst build` first")
    total = 0
    # dev server: drop the 1-year immutable cache so patched bundles reload
    server_js = os.path.join(THEME, "server.js")
    if os.path.exists(server_js):
        with open(server_js) as f:
            ssrc = f.read()
        fixed = ssrc.replace(
            "{ immutable: true, maxAge: '1y' }", "{ maxAge: '5m' }"
        )
        if fixed != ssrc:
            with open(server_js, "w") as f:
                f.write(fixed)
            print("patched server.js (cache headers)")
    # inject the search runtime into the server-rendered HTML itself; the
    # document is never long-cached, unlike the fingerprinted JS bundles
    import json
    server_bundle = os.path.join(THEME, "build", "index.js")
    with open(server_bundle) as f:
        bsrc = f.read()
    tag = json.dumps("<script>" + INLINER + "</script></body>")
    if INLINER_MARK in bsrc:
        print("already patched: build/index.js (search runtime)")
    elif "rpe-runtime" in bsrc:  # older runtime: swap it out
        new_bsrc, n = re.subn(
            r'"<script>[^"]*rpe-runtime[^"]*</script></body>"',
            lambda m: tag,
            bsrc,
        )
        with open(server_bundle, "w") as f:
            f.write(new_bsrc)
        total += n
        print(f"updated build/index.js runtime ({n} site)")
    else:
        new_bsrc, n = re.subn(
            r'new Response\("<!DOCTYPE html>"\+(\w+),',
            lambda m: (
                'new Response("<!DOCTYPE html>"+'
                f'{m.group(1)}.replace("</body>",{tag}),'
            ),
            bsrc,
        )
        if n == 0:
            sys.exit("SSR injection point not found; theme version changed?")
        with open(server_bundle, "w") as f:
            f.write(new_bsrc)
        total += n
        print(f"patched build/index.js (search runtime, {n} site)")
    # rename the patched entry + manifest so browsers that cached the stock
    # bundles (1-year immutable) fetch the patched versions
    # Rename the patched entry + manifest so browsers that cached the stock
    # bundles (1-year immutable) fetch the patched versions. The stock names
    # carry the theme's own content hashes, so discover them instead of
    # hardcoding: a theme update changes the hash, and a hardcoded name then
    # fails the build.
    import glob, shutil
    pub = os.path.join(THEME, "public", "build")
    new_entry, new_manifest = f"entry.client-{CACHE_TAG}", f"manifest-{CACHE_TAG}"
    if not os.path.exists(os.path.join(pub, f"{new_entry}.js")):
        rename = []
        for stem, new in (("entry.client-", new_entry), ("manifest-", new_manifest)):
            hits = [f for f in sorted(glob.glob(os.path.join(pub, stem + "*.js")))
                    if os.path.basename(f)[:-3] != new]
            if len(hits) == 1:
                rename.append((os.path.basename(hits[0])[:-3], new))
        if len(rename) == 2:
            for old, new in rename:
                shutil.copyfile(
                    os.path.join(pub, f"{old}.js"), os.path.join(pub, f"{new}.js")
                )
            for path in [os.path.join(THEME, "build", "index.js"),
                         os.path.join(pub, f"{new_manifest}.js")]:
                with open(path) as f:
                    s = f.read()
                for old, new in rename:
                    s = s.replace(old, new)
                with open(path, "w") as f:
                    f.write(s)
            print("renamed entry.client + manifest (cache bust)")
        else:
            print("skipped cache-bust rename: stock bundle names not found")

    if EXPAND_SECTIONS_MATCHING:
        for path in TARGETS:
            with open(path) as f:
                src = f.read()
            if MARKER in src:
                print(f"already patched: {os.path.relpath(path, THEME)}")
                continue
            out, n = patched(src)
            if n == 0:
                sys.exit(f"pattern not found in {path}; theme version changed?")
            with open(path, "w") as f:
                f.write(out)
            total += n
            print(f"patched {os.path.relpath(path, THEME)} ({n} site)")
        print(f"sections expanded by default: {EXPAND_SECTIONS_MATCHING}")
    else:
        print("TOC sections left collapsible (EXPAND_SECTIONS_MATCHING is empty)")
    print(f"done ({total} replacements)")


if __name__ == "__main__":
    main()
