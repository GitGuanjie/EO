import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path
OUT=Path(__file__).resolve().parent/'figures'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
# Fig 1: circuit geometry + instrument equivalence
fig=plt.figure(figsize=(7.1,3.15))
ax=fig.add_axes([0.02,0.07,.96,.88]);ax.axis('off');ax.set_xlim(0,12);ax.set_ylim(0,5.4)
for start,label,tint in [(0.7,r'Data $D_L$', '#d4e8f8'),(4.7,r'Ancilla $A$', '#f7e6c8'),(8.7,r'Data $D_R$', '#d4e8f8')]:
 ax.add_patch(FancyBboxPatch((start-.15,3.35),3.0,1.47,boxstyle='round,pad=.14,rounding_size=.12',facecolor=tint,edgecolor='#627284',lw=1))
 ax.text(start+1.35,4.58,label,ha='center',va='center',fontsize=9)
 for j in range(3):
  x=start+.4+.94*j
  ax.add_patch(Circle((x,3.82),.22,facecolor='#385b70' if start==4.7 else '#527b98',edgecolor='white'))
  ax.text(x,3.82,str(int(round(start-.7))+j+1) if start==.7 else (str(j+4) if start==4.7 else str(j+7)),color='white',fontsize=8,ha='center',va='center')
for x1,x2 in [(3.15,4.95),(7.15,8.95)]:ax.plot([x1,x2],[3.82,3.82],color='#ad6548',lw=2)
ax.text(6.1,2.83,r'Physical readout: $P^{(s)}_{45}$ vs. $I-P^{(s)}_{45}$',ha='center',fontsize=9)
ax.plot([.25,11.75],[2.52,2.52],lw=.6,color='#c0c5cc')
ax.text(.35,2.05,'50 controls',fontsize=9,fontweight='bold',ha='left')
ax.text(2.1,2.05,r'$X_{45}$',color='#b33b32',ha='center')
ax.text(3.25,2.05,'prepare',ha='center')
ax.text(4.9,2.05,r'$CZ_{L,A}$',ha='center')
ax.text(6.55,2.05,r'$CZ_{A,R}$',ha='center')
ax.text(8.2,2.05,'basis',ha='center')
ax.text(9.55,2.05,r'$X_{45}$',color='#b33b32',ha='center')
ax.text(10.9,2.05,'readout',ha='center')
for x in (2.1,9.55):ax.plot([x-.39,x+.39],[2.21,1.91],color='#b33b32',lw=1.6)
ax.annotate('',xy=(10.25,1.35),xytext=(1.4,1.35),arrowprops=dict(arrowstyle='-|>',color='#5b6573',lw=1))
ax.text(.35,.87,'48 controls',fontsize=9,fontweight='bold',ha='left')
ax.text(3.05,.87,'prepare',ha='center')
ax.text(4.9,.87,r'$CZ_{L,A}$',ha='center')
ax.text(6.55,.87,r'$CZ_{A,R}$',ha='center')
ax.text(8.4,.87,'basis',ha='center')
ax.text(10.45,.87,'readout',ha='center')
ax.text(6.1,.27,'The discarded boundaries change outcome phases, not the data instrument.',ha='center',fontsize=8,color='#44515d')
fig.savefig(OUT/'fig1_instrument.svg');fig.savefig(OUT/'fig1_instrument.pdf',bbox_inches='tight');fig.savefig(OUT/'fig1_instrument.png',dpi=185,bbox_inches='tight');plt.close(fig)
# Fig 2 quadratic curvature
metrics=['Instrument loss','Wrong syndrome','Leakage']
base=np.array([90.1754,50.1050,36.3205]); opt=np.array([86.0781,46.0078,36.3204]);
fig,ax=plt.subplots(figsize=(6.7,3.15));x=np.arange(3);w=.33
ax.bar(x-w/2,base,w,label='50C reference',color='#8ea0ad',edgecolor='white')
ax.bar(x+w/2,opt,w,label='48C optimized',color='#247a77',edgecolor='white')
ax.set_xticks(x,metrics);ax.set_ylabel(r'Static curvature $H=\sum_b H_b$');ax.set_ylim(0,108);ax.legend(ncol=2,loc='upper right',frameon=False)
for i,(a,b) in enumerate(zip(base,opt)):
 ax.text(i-w/2,a+2.1,f'{a:.1f}',ha='center',fontsize=7)
 ax.text(i+w/2,b+2.1,f'{b:.1f}',ha='center',fontsize=7)
ax.text(.98,.89,r'Exact ideal instrument in both cases',transform=ax.transAxes,ha='right',fontsize=8,color='#405662')
fig.tight_layout();fig.savefig(OUT/'fig2_curvature.svg');fig.savefig(OUT/'fig2_curvature.pdf');fig.savefig(OUT/'fig2_curvature.png',dpi=185);plt.close(fig)
# Fig3 MC scatter and paired CI
fig,axs=plt.subplots(1,2,figsize=(6.85,2.8),gridspec_kw={'width_ratios':[1.3,.9]})
labels=['50C reference','48C optimized'];vals=[1.103592,1.004484];
axs[0].bar(np.arange(2),vals,color=['#8297a9','#247a77'],width=.5)
axs[0].set_xticks([0,1],labels);axs[0].set_ylim(0,1.32);axs[0].set_ylabel('Mean wrong-syndrome probability (%)')
for i,v in enumerate(vals):axs[0].text(i,v+.04,f'{v:.3f}%',ha='center')
diff=-(0.01103592-0.01004484)*100;half=.0002694*100;
axs[1].axvline(0,color='#59656d',lw=1,ls='--');axs[1].errorbar(diff,0,xerr=half,fmt='o',color='#247a77',capsize=5,lw=2,ms=7)
axs[1].set_ylim(-.55,.65);axs[1].set_yticks([]);axs[1].set_xlabel('Paired difference (percentage points)');axs[1].set_title('48C minus 50C',fontsize=9)
axs[1].text(.5,.82,f'{diff:.3f} $\pm$ {half:.3f} (95% CI)',transform=axs[1].transAxes,ha='center',fontsize=8)
fig.tight_layout();fig.savefig(OUT/'fig3_montecarlo.svg');fig.savefig(OUT/'fig3_montecarlo.pdf');fig.savefig(OUT/'fig3_montecarlo.png',dpi=185);plt.close(fig)
# Fig4 star topology controlled geometry (hypothetical)
fig,ax=plt.subplots(figsize=(6.85,2.85));ax.axis('off');ax.set_xlim(-3.3,3.3);ax.set_ylim(-1.4,1.42)
coords={r'$D_1$':(-2.45,.92),r'$D_2$':(-2.45,-.89),r'$D_3$':(2.45,.92),r'$D_4$':(2.45,-.89)}
for lab,(x,y) in coords.items():
 ax.plot([0,x],[0,y],color='#a66f48',lw=2.4)
 ax.add_patch(Circle((x,y),.42,facecolor='#e2ecf3',edgecolor='#506a7b',lw=1.3));ax.text(x,y,lab,ha='center',va='center',fontsize=11)
ax.add_patch(Circle((0,0),.59,facecolor='#ead6af',edgecolor='#9a6f3b',lw=1.6));ax.text(0,.07,r'Ancilla',ha='center',va='center');ax.text(0,-.16,r'$(1,2,3)$',ha='center',va='center',fontsize=9)
ax.text(0,1.22,'Assumed physical exchange couplers, not strict 1D',ha='center',fontsize=10)
ax.text(0,-1.31,'Each data node is a three-spin EO encoding.',ha='center',fontsize=8,color='#54636d')
fig.savefig(OUT/'fig4_star.svg');fig.savefig(OUT/'fig4_star.pdf',bbox_inches='tight');fig.savefig(OUT/'fig4_star.png',dpi=185,bbox_inches='tight');plt.close(fig)
print('created',sorted(p.name for p in OUT.iterdir()))