cell_1 = ExperimentalAPSet(path='/home/drew/projects/iPSC-GA_Aug21/cell_1/AP_set',
                           file_prefix='cell_1_', file_suffix='_SAP.txt', cell_id=1)
bsline_cell1 = run_individual(0.75)
cell1_rmse = cell_1.score(bsline_cell1, write_data=True)

cell_2 = ExperimentalAPSet(path='/home/drew/projects/iPSC-GA_Aug21/cell_2/AP_set',
                           file_prefix='cell_2_', file_suffix='_SAP.txt', cell_id=2)
bsline_cell2 = run_individual(1.0)
cell2_rmse = cell_2.score(bsline_cell2, write_data=True)

cell_3 = ExperimentalAPSet(path='/home/drew/projects/iPSC-GA_Aug21/cell_3/AP_set',
                           file_prefix='cell_3_', file_suffix='_SAP.txt', cell_id=3)
bsline_cell3 = run_individual(1.5)
cell3_rmse = cell_3.score(bsline_cell3, write_data=True)

cell_4 = ExperimentalAPSet(path='/home/drew/projects/iPSC-GA_Aug21/cell_4/AP_set',
                           file_prefix='cell_4_', file_suffix='_SAP.txt', cell_id=4)
bsline_cell4 = run_individual(1.45)
cell4_rmse = cell_4.score(bsline_cell4, write_data=True)

cell_5 = ExperimentalAPSet(path='/home/drew/projects/iPSC-GA_Aug21/cell_5/AP_set',
                           file_prefix='cell_5_', file_suffix='_SAP.txt', cell_id=5)
bsline_cell5 = run_individual(0.5)
cell5_rmse = cell_5.score(bsline_cell5, write_data=True)

cell_6 = ExperimentalAPSet(path='/home/drew/projects/iPSC-GA_Aug21/cell_6/AP_set',
                           file_prefix='cell_6_', file_suffix='_SAP.txt', cell_id=6)
bsline_cell6 = run_individual(1.25)
cell6_rmse = cell_6.score(bsline_cell6, write_data=True)

# Plot bsline_cell1 APs
import matplotlib.pyplot as plt

plt.plot(bsline1['cntrl'].t,bsline1['cntrl'].V, label='Ishihara '+str(0.75)) 
plt.plot(bsline1['-0.15_ical'].t,bsline1['-0.15_ical'].V, label='Ishihara+ICaL -0.15')
plt.plot(bsline1['0.7_ical'].t,bsline1['0.7_ical'].V, label='Ishihara+ICaL 0.7')
plt.plot(bsline1['-0.25_ikr'].t,bsline1['-0.25_ikr'].V, label='Ishihara+IKr -0.25')
plt.plot(bsline1['0.9_ikr'].t,bsline1['0.9_ikr'].V, label='Ishihara+IKr 0.9')
plt.plot(bsline1['-0.9_ito'].t,bsline1['-0.9_ito'].V, label='Ishihara+Ito -0.9')
plt.plot(bsline1['1.5_ito'].t,bsline1['1.5_ito'].V, label='Ishihara+Ito 1.5')
plt.plot(bsline1['10_iks'].t,bsline1['10_iks'].V, label='Ishihara+Iks 10')
plt.plot(bsline1['4_iks'].t,bsline1['4_iks'].V, label='Ishihara+Iks 4')
plt.legend()
plt.show()


plt.plot(ind0_APSet['cntrl'].t,ind0_APSet['cntrl'].V, label='Ishihara '+str(0.75)) 
plt.plot(ind0_APSet['-0.15_ical'].t,ind0_APSet['-0.15_ical'].V, label='Ishihara+ICaL -0.15')
plt.plot(ind0_APSet['0.7_ical'].t,ind0_APSet['0.7_ical'].V, label='Ishihara+ICaL 0.7')
plt.plot(ind0_APSet['-0.25_ikr'].t,ind0_APSet['-0.25_ikr'].V, label='Ishihara+IKr -0.25')
plt.plot(ind0_APSet['0.9_ikr'].t,ind0_APSet['0.9_ikr'].V, label='Ishihara+IKr 0.9')
plt.plot(ind0_APSet['-0.9_ito'].t,ind0_APSet['-0.9_ito'].V, label='Ishihara+Ito -0.9')
plt.plot(ind0_APSet['1.5_ito'].t,ind0_APSet['1.5_ito'].V, label='Ishihara+Ito 1.5')
plt.plot(ind0_APSet['10_iks'].t,ind0_APSet['10_iks'].V, label='Ishihara+Iks 10')
plt.plot(ind0_APSet['4_iks'].t,ind0_APSet['4_iks'].V, label='Ishihara+Iks 4')
plt.legend()
plt.show()


plt.plot(ind1_APSet['cntrl'].t,ind1_APSet['cntrl'].V, label='Ishihara '+str(0.75)) 
plt.plot(ind1_APSet['-0.15_ical'].t,ind1_APSet['-0.15_ical'].V, label='Ishihara+ICaL -0.15')
plt.plot(ind1_APSet['0.7_ical'].t,ind1_APSet['0.7_ical'].V, label='Ishihara+ICaL 0.7')
plt.plot(ind1_APSet['-0.25_ikr'].t,ind1_APSet['-0.25_ikr'].V, label='Ishihara+IKr -0.25')
plt.plot(ind1_APSet['0.9_ikr'].t,ind1_APSet['0.9_ikr'].V, label='Ishihara+IKr 0.9')
plt.plot(ind1_APSet['-0.9_ito'].t,ind1_APSet['-0.9_ito'].V, label='Ishihara+Ito -0.9')
plt.plot(ind1_APSet['1.5_ito'].t,ind1_APSet['1.5_ito'].V, label='Ishihara+Ito 1.5')
plt.plot(ind1_APSet['10_iks'].t,ind1_APSet['10_iks'].V, label='Ishihara+Iks 10')
plt.plot(ind1_APSet['4_iks'].t,ind1_APSet['4_iks'].V, label='Ishihara+Iks 4')
plt.legend()
plt.show()


""" EA Fit 09/21/21 """
# Ind0 did not have complete AP set
ind1 = list(hof.iloc[1, :])
ind2 = list(hof.iloc[2, :])
ind3 = list(hof.iloc[3, :])
ind4 = list(hof.iloc[4, :])
ind5 = list(hof.iloc[5, :])
ind6 = list(hof.iloc[6, :])
ind7 = list(hof.iloc[7, :])
ind8 = list(hof.iloc[8, :])
ind9 = list(hof.iloc[9, :])

ind1_APSet = run_ind_dclamp(ind1, dc_ik1=0.75)
ind2_APSet = run_ind_dclamp(ind2, dc_ik1=0.75)
ind3_APSet = run_ind_dclamp(ind3, dc_ik1=0.75)
ind4_APSet = run_ind_dclamp(ind4, dc_ik1=0.75)
ind5_APSet = run_ind_dclamp(ind5, dc_ik1=0.75)
ind6_APSet = run_ind_dclamp(ind6, dc_ik1=0.75)
ind7_APSet = run_ind_dclamp(ind7, dc_ik1=0.75)
ind8_APSet = run_ind_dclamp(ind8, dc_ik1=0.75)
ind9_APSet = run_ind_dclamp(ind9, dc_ik1=0.75)


plt.plot(ind9_APSet['cntrl'].t,ind9_APSet['cntrl'].V, label='Ishihara '+str(0.75))
plt.plot(ind9_APSet['-0.15_ical'].t,ind9_APSet['-0.15_ical'].V, label='Ishihara+ICaL -0.15')
plt.plot(ind9_APSet['0.7_ical'].t,ind9_APSet['0.7_ical'].V, label='Ishihara+ICaL 0.7')
plt.plot(ind9_APSet['-0.25_ikr'].t,ind9_APSet['-0.25_ikr'].V, label='Ishihara+IKr -0.25')
plt.plot(ind9_APSet['0.9_ikr'].t,ind9_APSet['0.9_ikr'].V, label='Ishihara+IKr 0.9')
plt.plot(ind9_APSet['-0.9_ito'].t,ind9_APSet['-0.9_ito'].V, label='Ishihara+Ito -0.9')
plt.plot(ind9_APSet['1.5_ito'].t,ind9_APSet['1.5_ito'].V, label='Ishihara+Ito 1.5')
plt.plot(ind9_APSet['10_iks'].t,ind9_APSet['10_iks'].V, label='Ishihara+Iks 10')
plt.plot(ind9_APSet['4_iks'].t,ind9_APSet['4_iks'].V, label='Ishihara+Iks 4')
plt.legend()
plt.show()

scores_ind1 = cell_1.score(ind1_APSet, model_id=1, write_data=False)
scores_ind2 = cell_1.score(ind2_APSet, model_id=2, write_data=False)
scores_ind3 = cell_1.score(ind3_APSet, model_id=3, write_data=False)
scores_ind4 = cell_1.score(ind4_APSet, model_id=4, write_data=False)
scores_ind5 = cell_1.score(ind5_APSet, model_id=5, write_data=False)
scores_ind6 = cell_1.score(ind6_APSet, model_id=6, write_data=False)
scores_ind7 = cell_1.score(ind7_APSet, model_id=7, write_data=False)
scores_ind8 = cell_1.score(ind8_APSet, model_id=8, write_data=False)
scores_ind9 = cell_1.score(ind9_APSet, model_id=9, write_data=False)

hof_scores = []
hof_scores.append(scores_ind1)
hof_scores.append(scores_ind2)
hof_scores.append(scores_ind3)
hof_scores.append(scores_ind4)
hof_scores.append(scores_ind5)
hof_scores.append(scores_ind6)
hof_scores.append(scores_ind7)
hof_scores.append(scores_ind8)
hof_scores.append(scores_ind9)

plt.plot(ind1_APSet['cntrl'].t,ind1_APSet['cntrl'].V, label='ind1')
plt.plot(ind2_APSet['cntrl'].t,ind2_APSet['cntrl'].V, label='ind2')
plt.plot(ind3_APSet['cntrl'].t,ind3_APSet['cntrl'].V, label='ind3')
plt.plot(ind4_APSet['cntrl'].t,ind4_APSet['cntrl'].V, label='ind4')
plt.plot(ind5_APSet['cntrl'].t,ind5_APSet['cntrl'].V, label='ind5')
plt.plot(ind6_APSet['cntrl'].t,ind6_APSet['cntrl'].V, label='ind6')
plt.plot(ind7_APSet['cntrl'].t,ind7_APSet['cntrl'].V, label='ind6')
plt.plot(ind8_APSet['cntrl'].t,ind8_APSet['cntrl'].V, label='ind8')
plt.plot(ind9_APSet['cntrl'].t,ind9_APSet['cntrl'].V, label='ind9')
plt.legend()
plt.show()
