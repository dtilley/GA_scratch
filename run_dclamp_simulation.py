""" Program to run dynamic-clamp simulation. """
import numpy as np
import pandas as pd
from cell_models import protocols
from cell_models.kernik import KernikModel
import matplotlib.pyplot as plt


def run_individual(IK1_Ishi):
    # Create model and constrain monovalents
    kci = KernikModel(no_ion_selective_dict={'I_K1_Ishi': IK1_Ishi})
    kci.nai_millimolar = 10
    kci.ki_millimolar = 130
    # Create 10s paced protocol
    KERNIK_PROTOCOL = protocols.PacedProtocol(model_name="Kernik", stim_end=10000, stim_mag=2)
    # Run Ishihara IK1
    tr_ishi = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    y_ishi_final = kci.y_initial
    #tr_ishi.interpolate_data(time_resolution=0.1)
    tr_ishi.get_last_ap()
    
    # Run ICal -0.15
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_CaL': -0.15}
    kci.y_initial = y_ishi_final
    tr_ical_decrease = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_ical_decrease.interpolate_data(time_resolution=0.1)
    tr_ical_decrease.get_last_ap()
    
    # Run ICal 0.7
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_CaL': 0.7}
    kci.y_initial = y_ishi_final
    tr_ical_increase = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_ical_increase.interpolate_data(time_resolution=0.1)
    tr_ical_increase.get_last_ap()

    # Run IKr -0.25
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_Kr': -0.25}
    kci.y_initial = y_ishi_final
    tr_ikr_decrease = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_ikr_decrease.interpolate_data(time_resolution=0.1)
    tr_ikr_decrease.get_last_ap()

    # Run IKr 0.9
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_Kr': 0.9}
    kci.y_initial = y_ishi_final
    tr_ikr_increase = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_ikr_increase.interpolate_data(time_resolution=0.1)
    tr_ikr_increase.get_last_ap()

    # Run Ito -0.9
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_To': -0.9}
    kci.y_initial = y_ishi_final
    tr_ito_decrease = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_ito_decrease.interpolate_data(time_resolution=0.1)
    tr_ito_decrease.get_last_ap()

    # Run Ito 1.5
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_To': 1.5}
    kci.y_initial = y_ishi_final
    tr_ito_increase = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_ito_increase.interpolate_data(time_resolution=0.1)
    tr_ito_increase.get_last_ap()

    # Run IKs 10
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_Ks': 10}
    kci.y_initial = y_ishi_final
    tr_iks_10 = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_iks_10.interpolate_data(time_resolution=0.1)
    tr_iks_10.get_last_ap()

    # Run IKs 4
    kci._CellModel__no_ion_selective = {'I_K1_Ishi': 0.75, 'I_Ks': 4}
    kci.y_initial = y_ishi_final
    tr_iks_4 = kci.generate_response(KERNIK_PROTOCOL, is_no_ion_selective=True)
    #tr_iks_4.interpolate_data(time_resolution=0.1)
    tr_iks_4.get_last_ap()

    # Compare the AP traces
    plt.plot(tr_ishi.t, tr_ishi.y, label='Ishihara '+str(IK1_Ishi)) 
    plt.plot(tr_ical_decrease.t, tr_ical_decrease.y, label='Ishihara+ICaL -0.15')
    plt.plot(tr_ical_increase.t, tr_ical_increase.y, label='Ishihara+ICaL 0.7')
    plt.plot(tr_ikr_decrease.t, tr_ikr_decrease.y, label='Ishihara+IKr -0.25')
    plt.plot(tr_ikr_increase.t, tr_ikr_increase.y, label='Ishihara+IKr 0.9')
    plt.plot(tr_ito_decrease.t, tr_ito_decrease.y, label='Ishihara+Ito -0.9')
    plt.plot(tr_ito_increase.t, tr_ito_increase.y, label='Ishihara+Ito 1.5')
    plt.plot(tr_iks_10.t, tr_iks_10.y, label='Ishihara+Iks 10')
    plt.plot(tr_iks_4.t, tr_iks_4.y, label='Ishihara+Iks 4')
    plt.legend()
    plt.show()

    # Return AP set
    ap_set = {'cntrl': tr_ishi.last_ap,
              '-0.15_ical': tr_ical_decrease.last_ap,
              '0.7_ical': tr_ical_increase.last_ap,
              '-0.25_ikr': tr_ikr_decrease.last_ap,
              '0.9_ikr': tr_ikr_increase.last_ap,
              '-0.9_ito': tr_ito_decrease.last_ap,
              '1.5_ito': tr_ito_increase.last_ap,
              '10_iks': tr_iks_10.last_ap,
              '4_iks': tr_iks_4.last_ap}
    return ap_set



#def main():
#    # Run Baseline KC model w/ dclamp
#    run_individual()



    
#if __name__ == '__main__':
#    main()
