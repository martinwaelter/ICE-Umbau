from pathlib import Path
import subprocess, itertools, json, math
root=Path(__file__).resolve().parent
out=root/'simulation';out.mkdir(exist_ok=True)
rows=[]
for volt, state, tol, fault in itertools.product([12,18,24],[(0,0),(1,0),(0,1),(1,1)],[-.05,0,.05],['normal','open1','open2','short12']):
    ix=len(rows); fn=out/f'case_{ix}.cir'; data=out/f'case_{ix}.dat'
    # Separate, amplified low-side AUX outputs; external pull-ups, then series resistors.
    net=f'''ICE2976 passive two-wire adapter - nominal device models, not hardware verification
VU u 0 {volt}
RP1 u x1 {4700*(1+tol)}
RP2 u x2 {4700*(1+tol)}
RSW1 x1 0 {1 if state[0] else 1e12}
RSW2 x2 0 {1 if state[1] else 1e12}
RS1 x1 k1 {1e12 if fault=='open1' else 1000*(1+tol)}
RS2 x2 k2 {1e12 if fault=='open2' else 1000*(1+tol)}
RSHORT k1 k2 {0.01 if fault=='short12' else 1e12}
D1 k1 vp DS
D2 k2 vp DS
DR vp nr RED
DW vp nw WHITE
RR nr k1 {47000*(1+tol)}
RW nw k2 {47000*(1+tol)}
D3 nr vp DS
D4 nw vp DS
.model DS D(Is=2.52n N=1.752 Rs=0.568 Cjo=4p Tt=4n BV=75)
.model RED D(Is=1e-20 N=2 Rs=10)
.model WHITE D(Is=1e-25 N=2 Rs=10)
.control
set wr_singlescale
set wr_vecnames
op
wrdata {data.name} v(x1) v(x2) v(k1) v(k2) v(vp) v(nr) v(nw) @dr[id] @dw[id]
quit
.endc
.end
'''
    fn.write_text(net)
    proc=subprocess.run(['/opt/homebrew/bin/ngspice','-b',str(fn)],capture_output=True,text=True,cwd=out)
    if proc.returncode or not data.exists(): raise RuntimeError(proc.stdout+proc.stderr)
    vals=[float(x) for x in data.read_text().splitlines()[-1].split()]
    x1,x2,k1,k2,vp,nr,nw,ir,iw=vals[1:]
    row=dict(voltage=volt,state=state,tolerance=tol,fault=fault,red_mA=ir*1000,white_mA=iw*1000,pullup1_mW=(volt-x1)**2/(4700*(1+tol))*1000,pullup2_mW=(volt-x2)**2/(4700*(1+tol))*1000,red_reverse_V=max(nr-vp,0),white_reverse_V=max(nw-vp,0))
    rows.append(row)
    if fault=='normal' and state in [(1,0),(0,1)]:
        active=ir if state==(1,0) else iw; inactive=iw if state==(1,0) else ir
        assert 0<active<.00054, row
        assert inactive<1e-6, row
    elif fault in ['normal','open1','open2','short12']:
        assert ir<1e-6 and iw<1e-6,row
    assert max(row['red_reverse_V'],row['white_reverse_V'])<1.0,row
report={'model':'Static SPICE with resistive AUX switches, representative LEDs, 1N4148 model; physical LoDi LED characteristics unknown. Tolerances varied together, not exhaustive independent corners.','cases':len(rows),'passed':True,'max_LED_mA':max(max(r['red_mA'],r['white_mA']) for r in rows),'max_pullup_mW':max(max(r['pullup1_mW'],r['pullup2_mW']) for r in rows),'max_LED_reverse_V':max(max(r['red_reverse_V'],r['white_reverse_V']) for r in rows),'hardware_test':False,'cases_data':rows}
(root/'simulation_report.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='cases_data'},indent=2))
