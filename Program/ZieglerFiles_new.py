import os
def ziegler_files():
    #path= '/Users/hannah/Documents/UIO/Masteroppgaven/Ziegler/'
    path = os.getcwd() + '/new_ziegler/'


    ### FILENAMES:
    ### Bn10 : Beam negative 10%
    ### Dn250 : Density negative 25% (multiplied by ten to avoid desimal points)
    ### Beam varies for each paragraph. Density remains constant for each paragraph.

    ### Density -25%
    Bn100_Dn250 = path + 'ziegler_B_-10_D_-25_fluxes.csv'
    Bn75_Dn250 = path + 'ziegler_B_-7,5_D_-25_fluxes.csv'
    Bn50_Dn250 = path + 'ziegler_B_-5_D_-25_fluxes.csv'
    Bn25_Dn250 = path + 'ziegler_B_-2,5_D_-25_fluxes.csv'
    B0_Dn250   = path + 'ziegler_B_0_D_-25_fluxes.csv'
    Bp25_Dn250 = path + 'ziegler_B_+2,5_D_-25_fluxes.csv'
    Bp50_Dn250 = path + 'ziegler_B_+5_D_-25_fluxes.csv'
    Bp75_Dn250 = path + 'ziegler_B_+7,5_D_-25_fluxes.csv'
    Bp100_Dn250 = path + 'ziegler_B_+10_D_-25_fluxes.csv'

    ### Density -22.5%
    Bn100_Dn225 = path + 'ziegler_B_-10_D_-22,5_fluxes.csv'
    Bn75_Dn225 = path + 'ziegler_B_-7,5_D_-22,5_fluxes.csv'
    Bn50_Dn225 = path + 'ziegler_B_-5_D_-22,5_fluxes.csv'
    Bn25_Dn225 = path + 'ziegler_B_-2,5_D_-22,5_fluxes.csv'
    B0_Dn225   = path + 'ziegler_B_0_D_-22,5_fluxes.csv'
    Bp25_Dn225 = path + 'ziegler_B_+2,5_D_-22,5_fluxes.csv'
    Bp50_Dn225 = path + 'ziegler_B_+5_D_-22,5_fluxes.csv'
    Bp75_Dn225 = path + 'ziegler_B_+7,5_D_-22,5_fluxes.csv'
    Bp100_Dn225 = path + 'ziegler_B_+10_D_-22,5_fluxes.csv'

    ### Density -20%
    Bn100_Dn200 = path + 'ziegler_B_-10_D_-20_fluxes.csv'
    Bn75_Dn200 = path + 'ziegler_B_-7,5_D_-20_fluxes.csv'
    Bn50_Dn200 = path + 'ziegler_B_-5_D_-20_fluxes.csv'
    Bn25_Dn200 = path + 'ziegler_B_-2,5_D_-20_fluxes.csv'
    B0_Dn200   = path + 'ziegler_B_0_D_-20_fluxes.csv'
    Bp25_Dn200 = path + 'ziegler_B_+2,5_D_-20_fluxes.csv'
    Bp50_Dn200 = path + 'ziegler_B_+5_D_-20_fluxes.csv'
    Bp75_Dn200 = path + 'ziegler_B_+7,5_D_-20_fluxes.csv'
    Bp100_Dn200 = path + 'ziegler_B_+10_D_-20_fluxes.csv'

    ### Density -17.5%
    Bn100_Dn175 = path + 'ziegler_B_-10_D_-22,5_fluxes.csv'
    Bn75_Dn175 = path + 'ziegler_B_-7,5_D_-22,5_fluxes.csv'
    Bn50_Dn175 = path + 'ziegler_B_-5_D_-22,5_fluxes.csv'
    Bn25_Dn175 = path + 'ziegler_B_-2,5_D_-22,5_fluxes.csv'
    B0_Dn175   = path + 'ziegler_B_0_D_-22,5_fluxes.csv'
    Bp25_Dn175 = path + 'ziegler_B_+2,5_D_-22,5_fluxes.csv'
    Bp50_Dn175 = path + 'ziegler_B_+5_D_-22,5_fluxes.csv'
    Bp75_Dn175 = path + 'ziegler_B_+7,5_D_-22,5_fluxes.csv'
    Bp100_Dn175 = path + 'ziegler_B_+10_D_-22,5_fluxes.csv'


    ### Density -15%
    Bn100_Dn150 = path + 'ziegler_B_-10_D_-15_fluxes.csv' ## Fixed Ni10, Ir10, Cu10. Works!
    Bn75_Dn150 = path + 'ziegler_B_-7,5_D_-15_fluxes.csv'
    Bn50_Dn150 = path + 'ziegler_B_-5_D_-15_fluxes.csv'
    Bn25_Dn150 = path + 'ziegler_B_-2,5_D_-15_fluxes.csv'
    B0_Dn150   = path + 'ziegler_B_0_D_-15_fluxes.csv'
    Bp25_Dn150 = path + 'ziegler_B_+2,5_D_-15_fluxes.csv'
    Bp50_Dn150 = path + 'ziegler_B_+5_D_-15_fluxes.csv'
    Bp75_Dn150 = path + 'ziegler_B_+7,5_D_-15_fluxes.csv'
    Bp100_Dn150 = path + 'ziegler_B_+10_D_-15_fluxes.csv'


    ### Density -12.5%
    Bn100_Dn125 = path + 'ziegler_B_-10_D_-12,5_fluxes.csv'  ### Cu10 does not intercept with wfhm
    Bn75_Dn125 = path + 'ziegler_B_-7,5_D_-12,5_fluxes.csv'
    Bn50_Dn125 = path + 'ziegler_B_-5_D_-12,5_fluxes.csv'
    Bn25_Dn125 = path + 'ziegler_B_-2,5_D_-12,5_fluxes.csv'
    B0_Dn125   = path + 'ziegler_B_0_D_-12,5_fluxes.csv'
    Bp25_Dn125 = path + 'ziegler_B_+2,5_D_-12,5_fluxes.csv'
    Bp50_Dn125 = path + 'ziegler_B_+5_D_-12,5_fluxes.csv'
    Bp75_Dn125 = path + 'ziegler_B_+7,5_D_-12,5_fluxes.csv'
    Bp100_Dn125 = path + 'ziegler_B_+10_D_-12,5_fluxes.csv'


    ### Density -10%
    Bn100_Dn100 = path + 'ziegler_B_-10_D_-10_fluxes.csv'
    Bn75_Dn100 = path + 'ziegler_B_-7,5_D_-10_fluxes.csv'
    Bn50_Dn100 = path + 'ziegler_B_-5_D_-10_fluxes.csv'
    Bn25_Dn100 = path + 'ziegler_B_-2,5_D_-10_fluxes.csv'
    B0_Dn100   = path + 'ziegler_B_0_D_-10_fluxes.csv'
    Bp25_Dn100 = path + 'ziegler_B_+2,5_D_-10_fluxes.csv'
    Bp50_Dn100 = path + 'ziegler_B_+5_D_-10_fluxes.csv'
    Bp75_Dn100 = path + 'ziegler_B_+7,5_D_-10_fluxes.csv'
    Bp100_Dn100 = path + 'ziegler_B_+10_D_-10_fluxes.csv'

    ### Density -7.5%
    Bn100_Dn75 = path + 'ziegler_B_-10_D_-7,5_fluxes.csv'
    Bn75_Dn75 = path + 'ziegler_B_-7,5_D_-7,5_fluxes.csv'
    Bn50_Dn75 = path + 'ziegler_B_-5_D_-7,5_fluxes.csv'
    Bn25_Dn75 = path + 'ziegler_B_-2,5_D_-7,5_fluxes.csv'
    B0_Dn75   = path + 'ziegler_B_0_D_-7,5_fluxes.csv'
    Bp25_Dn75 = path + 'ziegler_B_+2,5_D_-7,5_fluxes.csv'
    Bp50_Dn75 = path + 'ziegler_B_+5_D_-7,5_fluxes.csv'
    Bp75_Dn75 = path + 'ziegler_B_+7,5_D_-7,5_fluxes.csv'
    Bp100_Dn75 = path + 'ziegler_B_+10_D_-7,5_fluxes.csv'


    ### Density -5%
    Bn100_Dn50 = path + 'ziegler_B_-10_D_-5_fluxes.csv'
    Bn75_Dn50 = path + 'ziegler_B_-7,5_D_-5_fluxes.csv'
    Bn50_Dn50 = path + 'ziegler_B_-5_D_-5_fluxes.csv'
    Bn25_Dn50 = path + 'ziegler_B_-2,5_D_-5_fluxes.csv'
    B0_Dn50   = path + 'ziegler_B_0_D_-5_fluxes.csv'
    Bp25_Dn50 = path + 'ziegler_B_+2,5_D_-5_fluxes.csv'
    Bp50_Dn50 = path + 'ziegler_B_+5_D_-5_fluxes.csv'
    Bp75_Dn50 = path + 'ziegler_B_+7,5_D_-5_fluxes.csv'
    Bp100_Dn50 = path + 'ziegler_B_+10_D_-5_fluxes.csv'


    ### Density -4%
    Bn100_Dn40 = path + 'ziegler_B_-10_D_-4_fluxes.csv'
    Bn75_Dn40 = path + 'ziegler_B_-7,5_D_-4_fluxes.csv'
    Bn50_Dn40 = path + 'ziegler_B_-5_D_-4_fluxes.csv'
    Bn25_Dn40 = path + 'ziegler_B_-2,5_D_-4_fluxes.csv'
    B0_Dn40   = path + 'ziegler_B_0_D_-4_fluxes.csv'
    Bp25_Dn40 = path + 'ziegler_B_+2,5_D_-4_fluxes.csv'
    Bp50_Dn40 = path + 'ziegler_B_+5_D_-4_fluxes.csv'
    Bp75_Dn40 = path + 'ziegler_B_+7,5_D_-4_fluxes.csv'
    Bp100_Dn40 = path + 'ziegler_B_+10_D_-4_fluxes.csv'

    ### Density -3.5%
    Bn100_Dn35 = path + 'ziegler_B_-10_D_-3,5_fluxes.csv'
    Bn75_Dn35 = path + 'ziegler_B_-7,5_D_-3,5_fluxes.csv'
    Bn50_Dn35 = path + 'ziegler_B_-5_D_-3,5_fluxes.csv'
    Bn25_Dn35 = path + 'ziegler_B_-2,5_D_-3,5_fluxes.csv'
    B0_Dn35   = path + 'ziegler_B_0_D_-3,5_fluxes.csv'
    Bp25_Dn35 = path + 'ziegler_B_+2,5_D_-3,5_fluxes.csv'
    Bp50_Dn35 = path + 'ziegler_B_+5_D_-3,5_fluxes.csv'
    Bp75_Dn35 = path + 'ziegler_B_+7,5_D_-3,5_fluxes.csv'
    Bp100_Dn35 = path + 'ziegler_B_+10_D_-3,5_fluxes.csv'

    ### Density -3%
    Bn100_Dn30 = path + 'ziegler_B_-10_D_-3_fluxes.csv'
    Bn75_Dn30 = path + 'ziegler_B_-7,5_D_-3_fluxes.csv'
    Bn50_Dn30 = path + 'ziegler_B_-5_D_-3_fluxes.csv'
    Bn25_Dn30 = path + 'ziegler_B_-2,5_D_-3_fluxes.csv'
    B0_Dn30   = path + 'ziegler_B_0_D_-3_fluxes.csv'
    Bp25_Dn30 = path + 'ziegler_B_+2,5_D_-3_fluxes.csv'
    Bp50_Dn30 = path + 'ziegler_B_+5_D_-3_fluxes.csv'
    Bp75_Dn30 = path + 'ziegler_B_+7,5_D_-3_fluxes.csv'
    Bp100_Dn30 = path + 'ziegler_B_+10_D_-3_fluxes.csv'

    ### Density -2.5%
    Bn100_Dn25 = path + 'ziegler_B_-10_D_-2,5_fluxes.csv'
    Bn75_Dn25 = path + 'ziegler_B_-7,5_D_-2,5_fluxes.csv'
    Bn50_Dn25 = path + 'ziegler_B_-5_D_-2,5_fluxes.csv'
    Bn25_Dn25 = path + 'ziegler_B_-2,5_D_-2,5_fluxes.csv'
    B0_Dn25   = path + 'ziegler_B_0_D_-2,5_fluxes.csv'
    Bp25_Dn25 = path + 'ziegler_B_+2,5_D_-2,5_fluxes.csv'
    Bp50_Dn25 = path + 'ziegler_B_+5_D_-2,5_fluxes.csv'
    Bp75_Dn25 = path + 'ziegler_B_+7,5_D_-2,5_fluxes.csv'
    Bp100_Dn25 = path + 'ziegler_B_+10_D_-2,5_fluxes.csv'

    ### Density -2%
    Bn100_Dn20 = path + 'ziegler_B_-10_D_-2_fluxes.csv'
    Bn75_Dn20 = path + 'ziegler_B_-7,5_D_-2_fluxes.csv'
    Bn50_Dn20 = path + 'ziegler_B_-5_D_-2_fluxes.csv'
    Bn25_Dn20 = path + 'ziegler_B_-2,5_D_-2_fluxes.csv'
    B0_Dn20   = path + 'ziegler_B_0_D_-2_fluxes.csv'
    Bp25_Dn20 = path + 'ziegler_B_+2,5_D_-2_fluxes.csv'
    Bp50_Dn20 = path + 'ziegler_B_+5_D_-2_fluxes.csv'
    Bp75_Dn20 = path + 'ziegler_B_+7,5_D_-2_fluxes.csv'
    Bp100_Dn20 = path + 'ziegler_B_+10_D_-2_fluxes.csv'


    ### Density -1.5%
    Bn100_Dn15 = path + 'ziegler_B_-10_D_-1,5_fluxes.csv'
    Bn75_Dn15 = path + 'ziegler_B_-7,5_D_-1,5_fluxes.csv'
    Bn50_Dn15 = path + 'ziegler_B_-5_D_-1,5_fluxes.csv'
    Bn25_Dn15 = path + 'ziegler_B_-2,5_D_-1,5_fluxes.csv'
    B0_Dn15   = path + 'ziegler_B_0_D_-1,5_fluxes.csv'
    Bp25_Dn15 = path + 'ziegler_B_+2,5_D_-1,5_fluxes.csv'
    Bp50_Dn15 = path + 'ziegler_B_+5_D_-1,5_fluxes.csv'
    Bp75_Dn15 = path + 'ziegler_B_+7,5_D_-1,5_fluxes.csv'
    Bp100_Dn15 = path + 'ziegler_B_+10_D_-1,5_fluxes.csv'


    ### Density -1%
    Bn100_Dn10 = path + 'ziegler_B_-10_D_-1_fluxes.csv'
    Bn75_Dn10 = path + 'ziegler_B_-7,5_D_-1_fluxes.csv'
    Bn50_Dn10 = path + 'ziegler_B_-5_D_-1_fluxes.csv'
    Bn25_Dn10 = path + 'ziegler_B_-2,5_D_-1_fluxes.csv'
    B0_Dn10   = path + 'ziegler_B_0_D_-1_fluxes.csv'
    Bp25_Dn10 = path + 'ziegler_B_+2,5_D_-1_fluxes.csv'
    Bp50_Dn10 = path + 'ziegler_B_+5_D_-1_fluxes.csv'
    Bp75_Dn10 = path + 'ziegler_B_+7,5_D_-1_fluxes.csv'
    Bp100_Dn10 = path + 'ziegler_B_+10_D_-1_fluxes.csv'

    ### Density -0.5%
    Bn100_Dn05 = path + 'ziegler_B_-10_D_-0,5_fluxes.csv'
    Bn75_Dn05 = path + 'ziegler_B_-7,5_D_-0,5_fluxes.csv'
    Bn50_Dn05 = path + 'ziegler_B_-5_D_-0,5_fluxes.csv'
    Bn25_Dn05 = path + 'ziegler_B_-2,5_D_-0,5_fluxes.csv'
    B0_Dn05   = path + 'ziegler_B_0_D_-0,5_fluxes.csv'
    Bp25_Dn05 = path + 'ziegler_B_+2,5_D_-0,5_fluxes.csv'
    Bp50_Dn05 = path + 'ziegler_B_+5_D_-0,5_fluxes.csv'
    Bp75_Dn05 = path + 'ziegler_B_+7,5_D_-0,5_fluxes.csv'
    Bp100_Dn05 = path + 'ziegler_B_+10_D_-0,5_fluxes.csv'


    ### Density 0%
    Bn100_D0 = path + 'ziegler_B_-10_D_0_fluxes.csv'
    Bn75_D0 = path + 'ziegler_B_-7,5_D_0_fluxes.csv'
    Bn50_D0 = path + 'ziegler_B_-5_D_0_fluxes.csv'
    Bn25_D0 = path + 'ziegler_B_-2,5_D_0_fluxes.csv'
    B0_D0   = path + 'ziegler_B_0_D_0_fluxes.csv'
    Bp25_D0 = path + 'ziegler_B_+2,5_D_0_fluxes.csv'
    Bp50_D0 = path + 'ziegler_B_+5_D_0_fluxes.csv'
    Bp75_D0 = path + 'ziegler_B_+7,5_D_0_fluxes.csv'
    Bp100_D0 = path + 'ziegler_B_+10_D_0_fluxes.csv'


    ### Density +0.5%
    Bn100_Dp05 = path + 'ziegler_B_-10_D_+0,5_fluxes.csv'
    Bn75_Dp05 = path + 'ziegler_B_-7,5_D_+0,5_fluxes.csv'
    Bn50_Dp05 = path + 'ziegler_B_-5_D_+0,5_fluxes.csv'
    Bn25_Dp05 = path + 'ziegler_B_-2,5_D_+0,5_fluxes.csv'
    B0_Dp05   = path + 'ziegler_B_0_D_+0,5_fluxes.csv'
    Bp25_Dp05 = path + 'ziegler_B_+2,5_D_+0,5_fluxes.csv'
    Bp50_Dp05 = path + 'ziegler_B_+5_D_+0,5_fluxes.csv'
    Bp75_Dp05 = path + 'ziegler_B_+7,5_D_+0,5_fluxes.csv'
    Bp100_Dp05 = path + 'ziegler_B_+10_D_+0,5_fluxes.csv'
    ### Density +1%
    Bn100_Dp10 = path + 'ziegler_B_-10_D_+1_fluxes.csv'
    Bn75_Dp10 = path + 'ziegler_B_-7,5_D_+1_fluxes.csv'
    Bn50_Dp10 = path + 'ziegler_B_-5_D_+1_fluxes.csv'
    Bn25_Dp10 = path + 'ziegler_B_-2,5_D_+1_fluxes.csv'
    B0_Dp10   = path + 'ziegler_B_0_D_+1_fluxes.csv'
    Bp25_Dp10 = path + 'ziegler_B_+2,5_D_+1_fluxes.csv'
    Bp50_Dp10 = path + 'ziegler_B_+5_D_+1_fluxes.csv'
    Bp75_Dp10 = path + 'ziegler_B_+7,5_D_+1_fluxes.csv'
    Bp100_Dp10 = path + 'ziegler_B_+10_D_+1_fluxes.csv'

    ### Density +1.5%
    Bn100_Dp15 = path +  'ziegler_B_-10_D_+1,5_fluxes.csv'
    Bn75_Dp15 = path + 'ziegler_B_-7,5_D_+1,5_fluxes.csv'
    Bn50_Dp15 = path +   'ziegler_B_-5_D_+1,5_fluxes.csv'
    Bn25_Dp15 = path + 'ziegler_B_-2,5_D_+1,5_fluxes.csv'
    B0_Dp15   = path +    'ziegler_B_0_D_+1,5_fluxes.csv'
    Bp25_Dp15 = path + 'ziegler_B_+2,5_D_+1,5_fluxes.csv'
    Bp50_Dp15 = path +   'ziegler_B_+5_D_+1,5_fluxes.csv'
    Bp75_Dp15 = path + 'ziegler_B_+7,5_D_+1,5_fluxes.csv'
    Bp100_Dp15 = path +  'ziegler_B_+10_D_+1,5_fluxes.csv'

    ### Density +2%
    Bn100_Dp20 = path +  'ziegler_B_-10_D_+2_fluxes.csv'
    Bn75_Dp20 = path + 'ziegler_B_-7,5_D_+2_fluxes.csv'
    Bn50_Dp20 = path +   'ziegler_B_-5_D_+2_fluxes.csv'
    Bn25_Dp20 = path + 'ziegler_B_-2,5_D_+2_fluxes.csv'
    B0_Dp20   = path +    'ziegler_B_0_D_+2_fluxes.csv'
    Bp25_Dp20 = path + 'ziegler_B_+2,5_D_+2_fluxes.csv'
    Bp50_Dp20 = path +   'ziegler_B_+5_D_+2_fluxes.csv'
    Bp75_Dp20 = path + 'ziegler_B_+7,5_D_+2_fluxes.csv'
    Bp100_Dp20 = path +  'ziegler_B_+10_D_+2_fluxes.csv'

    ### Density +2.5%
    Bn100_Dp25 = path +  'ziegler_B_-10_D_+2,5_fluxes.csv'
    Bn75_Dp25 = path + 'ziegler_B_-7,5_D_+2,5_fluxes.csv'
    Bn50_Dp25 = path +   'ziegler_B_-5_D_+2,5_fluxes.csv'
    Bn25_Dp25 = path + 'ziegler_B_-2,5_D_+2,5_fluxes.csv'
    B0_Dp25   = path +    'ziegler_B_0_D_+2,5_fluxes.csv'
    Bp25_Dp25 = path + 'ziegler_B_+2,5_D_+2,5_fluxes.csv'
    Bp50_Dp25 = path +   'ziegler_B_+5_D_+2,5_fluxes.csv'
    Bp75_Dp25 = path + 'ziegler_B_+7,5_D_+2,5_fluxes.csv'
    Bp100_Dp25 = path +  'ziegler_B_+10_D_+2,5_fluxes.csv'


    ### Density +3%
    Bn100_Dp30 = path +  'ziegler_B_-10_D_+3_fluxes.csv'
    Bn75_Dp30 = path + 'ziegler_B_-7,5_D_+3_fluxes.csv'
    Bn50_Dp30 = path +   'ziegler_B_-5_D_+3_fluxes.csv'
    Bn25_Dp30 = path + 'ziegler_B_-2,5_D_+3_fluxes.csv'
    B0_Dp30   = path +    'ziegler_B_0_D_+3_fluxes.csv'
    Bp25_Dp30 = path + 'ziegler_B_+2,5_D_+3_fluxes.csv'
    Bp50_Dp30 = path +   'ziegler_B_+5_D_+3_fluxes.csv'
    Bp75_Dp30 = path + 'ziegler_B_+7,5_D_+3_fluxes.csv'
    Bp100_Dp30 = path +  'ziegler_B_+10_D_+3_fluxes.csv'


    ### Density +3.5%
    Bn100_Dp35 = path +  'ziegler_B_-10_D_+3,5_fluxes.csv'
    Bn75_Dp35 = path + 'ziegler_B_-7,5_D_+3,5_fluxes.csv'
    Bn50_Dp35 = path +   'ziegler_B_-5_D_+3,5_fluxes.csv'
    Bn25_Dp35 = path + 'ziegler_B_-2,5_D_+3,5_fluxes.csv'
    B0_Dp35   = path +    'ziegler_B_0_D_+3,5_fluxes.csv'
    Bp25_Dp35 = path + 'ziegler_B_+2,5_D_+3,5_fluxes.csv'
    Bp50_Dp35 = path +   'ziegler_B_+5_D_+3,5_fluxes.csv'
    Bp75_Dp35 = path + 'ziegler_B_+7,5_D_+3,5_fluxes.csv'
    Bp100_Dp35 = path +  'ziegler_B_+10_D_+3,5_fluxes.csv'

    ### Density +4%
    Bn100_Dp40 = path +  'ziegler_B_-10_D_+4_fluxes.csv'
    Bn75_Dp40 = path + 'ziegler_B_-7,5_D_+4_fluxes.csv'
    Bn50_Dp40 = path +   'ziegler_B_-5_D_+4_fluxes.csv'
    Bn25_Dp40 = path + 'ziegler_B_-2,5_D_+4_fluxes.csv'
    B0_Dp40   = path +    'ziegler_B_0_D_+4_fluxes.csv'
    Bp25_Dp40 = path + 'ziegler_B_+2,5_D_+4_fluxes.csv'
    Bp50_Dp40 = path +   'ziegler_B_+5_D_+4_fluxes.csv'
    Bp75_Dp40 = path + 'ziegler_B_+7,5_D_+4_fluxes.csv'
    Bp100_Dp40 = path +  'ziegler_B_+10_D_+4_fluxes.csv'

    ### Density +5%
    Bn100_Dp50 = path +  'ziegler_B_-10_D_+5_fluxes.csv'
    Bn75_Dp50 = path + 'ziegler_B_-7,5_D_+5_fluxes.csv'
    Bn50_Dp50 = path +   'ziegler_B_-5_D_+5_fluxes.csv'
    Bn25_Dp50 = path + 'ziegler_B_-2,5_D_+5_fluxes.csv'
    B0_Dp50   = path +    'ziegler_B_0_D_+5_fluxes.csv'
    Bp25_Dp50 = path + 'ziegler_B_+2,5_D_+5_fluxes.csv'
    Bp50_Dp50 = path +   'ziegler_B_+5_D_+5_fluxes.csv'
    Bp75_Dp50 = path + 'ziegler_B_+7,5_D_+5_fluxes.csv'
    Bp100_Dp50 = path +  'ziegler_B_+10_D_+5_fluxes.csv'

    ### Density +7.5%
    Bn100_Dp75 = path +  'ziegler_B_-10_D_+7,5_fluxes.csv'
    Bn75_Dp75 = path + 'ziegler_B_-7,5_D_+7,5_fluxes.csv'
    Bn50_Dp75 = path +   'ziegler_B_-5_D_+7,5_fluxes.csv'
    Bn25_Dp75 = path + 'ziegler_B_-2,5_D_+7,5_fluxes.csv'
    B0_Dp75   = path +    'ziegler_B_0_D_+7,5_fluxes.csv'
    Bp25_Dp75 = path + 'ziegler_B_+2,5_D_+7,5_fluxes.csv'
    Bp50_Dp75 = path +   'ziegler_B_+5_D_+7,5_fluxes.csv'
    Bp75_Dp75 = path + 'ziegler_B_+7,5_D_+7,5_fluxes.csv'
    Bp100_Dp75 = path +  'ziegler_B_+10_D_+7,5_fluxes.csv'

    ### Density +10%
    Bn100_Dp100 = path +  'ziegler_B_-10_D_+10_fluxes.csv'
    Bn75_Dp100 = path + 'ziegler_B_-7,5_D_+10_fluxes.csv'
    Bn50_Dp100 = path +   'ziegler_B_-5_D_+10_fluxes.csv'
    Bn25_Dp100 = path + 'ziegler_B_-2,5_D_+10_fluxes.csv'
    B0_Dp100   = path +    'ziegler_B_0_D_+10_fluxes.csv'
    Bp25_Dp100 = path + 'ziegler_B_+2,5_D_+10_fluxes.csv'
    Bp50_Dp100 = path +   'ziegler_B_+5_D_+10_fluxes.csv'
    Bp75_Dp100 = path + 'ziegler_B_+7,5_D_+10_fluxes.csv'
    Bp100_Dp100 = path +  'ziegler_B_+10_D_+10_fluxes.csv'

    ### Density +12.5%
    Bn100_Dp125 = path +  'ziegler_B_-10_D_+12,5_fluxes.csv'
    Bn75_Dp125 = path + 'ziegler_B_-7,5_D_+12,5_fluxes.csv'
    Bn50_Dp125 = path +   'ziegler_B_-5_D_+12,5_fluxes.csv'
    Bn25_Dp125 = path + 'ziegler_B_-2,5_D_+12,5_fluxes.csv'
    B0_Dp125   = path +    'ziegler_B_0_D_+12,5_fluxes.csv'
    Bp25_Dp125 = path + 'ziegler_B_+2,5_D_+12,5_fluxes.csv'
    Bp50_Dp125 = path +   'ziegler_B_+5_D_+12,5_fluxes.csv'
    Bp75_Dp125 = path + 'ziegler_B_+7,5_D_+12,5_fluxes.csv'
    Bp100_Dp125 = path +  'ziegler_B_+10_D_+12,5_fluxes.csv'
    ### Density +15%
    Bn100_Dp150 = path +  'ziegler_B_-10_D_+15_fluxes.csv'
    Bn75_Dp150 = path + 'ziegler_B_-7,5_D_+15_fluxes.csv'
    Bn50_Dp150 = path +   'ziegler_B_-5_D_+15_fluxes.csv'
    Bn25_Dp150 = path + 'ziegler_B_-2,5_D_+15_fluxes.csv'
    B0_Dp150   = path +    'ziegler_B_0_D_+15_fluxes.csv'
    Bp25_Dp150 = path + 'ziegler_B_+2,5_D_+15_fluxes.csv'
    Bp50_Dp150 = path +   'ziegler_B_+5_D_+15_fluxes.csv'
    Bp75_Dp150 = path + 'ziegler_B_+7,5_D_+15_fluxes.csv'
    Bp100_Dp150 = path +  'ziegler_B_+10_D_+15_fluxes.csv'

    files = [Bn100_Dn250, Bn75_Dn250, Bn50_Dn250, Bn25_Dn250, B0_Dn250, Bp25_Dn250, Bp50_Dn250, Bp75_Dn250, Bp100_Dn250,
            Bn100_Dn225, Bn75_Dn225, Bn50_Dn225, Bn25_Dn225, B0_Dn225, Bp25_Dn225, Bp50_Dn225, Bp75_Dn225, Bp100_Dn225,
            Bn100_Dn200, Bn75_Dn200, Bn50_Dn200, Bn25_Dn200, B0_Dn200, Bp25_Dn200, Bp50_Dn200, Bp75_Dn200, Bp100_Dn200,
            Bn100_Dn175, Bn75_Dn175, Bn50_Dn175, Bn25_Dn175, B0_Dn175, Bp25_Dn175, Bp50_Dn175, Bp75_Dn175, Bp100_Dn175,
            Bn100_Dn150, Bn75_Dn150, Bn50_Dn150, Bn25_Dn150, B0_Dn150, Bp25_Dn150, Bp50_Dn150, Bp75_Dn150, Bp100_Dn150,
            Bn100_Dn125, Bn75_Dn125, Bn50_Dn125, Bn25_Dn125, B0_Dn125, Bp25_Dn125, Bp50_Dn125, Bp75_Dn125, Bp100_Dn125,
            Bn100_Dn100, Bn75_Dn100, Bn50_Dn100, Bn25_Dn100, B0_Dn100, Bp25_Dn100, Bp50_Dn100, Bp75_Dn100, Bp100_Dn100,
            Bn100_Dn75, Bn75_Dn75, Bn50_Dn75, Bn25_Dn75, B0_Dn75, Bp25_Dn75, Bp50_Dn75, Bp75_Dn75, Bp100_Dn75,
            Bn100_Dn50, Bn75_Dn50, Bn50_Dn50, Bn25_Dn50, B0_Dn50, Bp25_Dn50, Bp50_Dn50, Bp75_Dn50, Bp100_Dn50,
            #Bn100_Dn45, Bn75_Dn45, Bn50_Dn45, Bn25_Dn45, B0_Dn45, Bp25_Dn45, Bp50_Dn45, Bp75_Dn45, Bp100_Dn45,
            Bn100_Dn40, Bn75_Dn40, Bn50_Dn40, Bn25_Dn40, B0_Dn40, Bp25_Dn40, Bp50_Dn40, Bp75_Dn40, Bp100_Dn40,
            Bn100_Dn35, Bn75_Dn35, Bn50_Dn35, Bn25_Dn35, B0_Dn35, Bp25_Dn35, Bp50_Dn35, Bp75_Dn35, Bp100_Dn35,
            Bn100_Dn30, Bn75_Dn30, Bn50_Dn30, Bn25_Dn30, B0_Dn30, Bp25_Dn30, Bp50_Dn30, Bp75_Dn30, Bp100_Dn30,
            Bn100_Dn25, Bn75_Dn25, Bn50_Dn25, Bn25_Dn25, B0_Dn25, Bp25_Dn25, Bp50_Dn25, Bp75_Dn25, Bp100_Dn25,
            Bn100_Dn20, Bn75_Dn20, Bn50_Dn20, Bn25_Dn20, B0_Dn20, Bp25_Dn20, Bp50_Dn20, Bp75_Dn20, Bp100_Dn20,
            Bn100_Dn15, Bn75_Dn15, Bn50_Dn15, Bn25_Dn15, B0_Dn15, Bp25_Dn15, Bp50_Dn15, Bp75_Dn15, Bp100_Dn15,
            Bn100_Dn10, Bn75_Dn10, Bn50_Dn10, Bn25_Dn10, B0_Dn10, Bp25_Dn10, Bp50_Dn10, Bp75_Dn10, Bp100_Dn10,
            Bn100_Dn05, Bn75_Dn05, Bn50_Dn05, Bn25_Dn05, B0_Dn05, Bp25_Dn05, Bp50_Dn05, Bp75_Dn05, Bp100_Dn05,
            Bn100_D0, Bn75_D0, Bn50_D0, Bn25_D0, B0_D0, Bp25_D0, Bp50_D0, Bp75_D0, Bp100_D0,
            Bn100_Dp05, Bn75_Dp05, Bn50_Dp05, Bn25_Dp05, B0_Dp05, Bp25_Dp05, Bp50_Dp05, Bp75_Dp05, Bp100_Dp05,
            Bn100_Dp10, Bn75_Dp10, Bn50_Dp10, Bn25_Dp10, B0_Dp10, Bp25_Dp10, Bp50_Dp10, Bp75_Dp10, Bp100_Dp10,
            Bn100_Dp15, Bn75_Dp15, Bn50_Dp15, Bn25_Dp15, B0_Dp15, Bp25_Dp15, Bp50_Dp15, Bp75_Dp15, Bp100_Dp15,
            Bn100_Dp20, Bn75_Dp20, Bn50_Dp20, Bn25_Dp20, B0_Dp20, Bp25_Dp20, Bp50_Dp20, Bp75_Dp20, Bp100_Dp20,
            Bn100_Dp25, Bn75_Dp25, Bn50_Dp25, Bn25_Dp25, B0_Dp25, Bp25_Dp25, Bp50_Dp25, Bp75_Dp25, Bp100_Dp25,
            Bn100_Dp30, Bn75_Dp30, Bn50_Dp30, Bn25_Dp30, B0_Dp30, Bp25_Dp30, Bp50_Dp30, Bp75_Dp30, Bp100_Dp30,
            Bn100_Dp35, Bn75_Dp35, Bn50_Dp35, Bn25_Dp35, B0_Dp35, Bp25_Dp35, Bp50_Dp35, Bp75_Dp35, Bp100_Dp35,
            Bn100_Dp40, Bn75_Dp40, Bn50_Dp40, Bn25_Dp40, B0_Dp40, Bp25_Dp40, Bp50_Dp40, Bp75_Dp40, Bp100_Dp40,
            #Bn100_Dp45, Bn75_Dp45, Bn50_Dp45, Bn25_Dp45, B0_Dp45, Bp25_Dp45, Bp50_Dp45, Bp75_Dp45, Bp100_Dp45,
            Bn100_Dp50, Bn75_Dp50, Bn50_Dp50, Bn25_Dp50, B0_Dp50, Bp25_Dp50, Bp50_Dp50, Bp75_Dp50, Bp100_Dp50,
            Bn100_Dp75, Bn75_Dp75, Bn50_Dp75, Bn25_Dp75, B0_Dp75, Bp25_Dp75, Bp50_Dp75, Bp75_Dp75, Bp100_Dp75,
            Bn100_Dp100, Bn75_Dp100, Bn50_Dp100, Bn25_Dp100, B0_Dp100, Bp25_Dp100, Bp50_Dp100, Bp75_Dp100, Bp100_Dp100,
            #Bn100_Dp125, Bn75_Dp125, Bn50_Dp125, Bn25_Dp125, B0_Dp125, Bp25_Dp125, Bp50_Dp125, Bp75_Dp125, Bp100_Dp125,
            Bn100_Dp150, Bn75_Dp150, Bn50_Dp150, Bn25_Dp150, B0_Dp150, Bp25_Dp150, Bp50_Dp150, Bp75_Dp150, Bp100_Dp150
            ]

    names = ['B-10%_D-25%', 'B-7,5%_D-25%', 'B-5%_D-25%', 'B-2,5%_D-25%', 'B0%_D-25%', 'B+2,5%_D-25%', 'B+5%_D-25%','B+7,5%_D-25%','B+10%_D-25%',
            'B-10%_D-22,5%', 'B-7,5%_D-22,5%', 'B-5%_D-22,5%', 'B-2,5%_D-22,5%', 'B0%_D-22,5%', 'B+2,5%_D-22,5%', 'B+5%_D-22,5%','B+7,5%_D-22,5%','B+10%_D-22,5%',
            'B-10%_D-20%', 'B-7,5%_D-20%', 'B-5%_D-20%', 'B-2,5%_D-20%', 'B0%_D-20%', 'B+2,5%_D-20%', 'B+5%_D-20%','B+7,5%_D-20%','B+10%_D-20%',
            'B-10%_D-17,5%', 'B-7,5%_D-17,5%', 'B-5%_D-17,5%', 'B-2,5%_D-17,5%', 'B0%_D-17,5%', 'B+2,5%_D-17,5%', 'B+5%_D-17,5%','B+7,5%_D-17,5%','B+10%_D-17,5%',
            'B-10%_D-15%', 'B-7,5%_D-15%', 'B-5%_D-15%', 'B-2,5%_D-15%', 'B0%_D-15%', 'B+2,5%_D-15%', 'B+5%_D-15%','B+7,5%_D-15%','B+10%_D-15%',
            'B-10%_D-12,5%', 'B-7,5%_D-12,5%', 'B-5%_D-12,5%', 'B-2,5%_D-12,5%', 'B0%_D-12,5%', 'B+2,5%_D-12,5%', 'B+5%_D-12,5%','B+7,5%_D-12,5%','B+10%_D-12,5%',
            'B-10%_D-10%', 'B-7,5%_D-10%', 'B-5%_D-10%', 'B-2,5%_D-10%', 'B0%_D-10%', 'B+2,5%_D-10%', 'B+5%_D-10%','B+7,5%_D-10%','B+10%_D-10%',
            'B-10%_D-7,5%', 'B-7,5%_D-7,5%', 'B-5%_D-7,5%', 'B-2,5%_D-7,5%', 'B0%_D-7,5%', 'B+2,5%_D-7,5%', 'B+5%_D-7,5%','B+7,5%_D-7,5%','B+10%_D-7,5%',
            'B-10%_D-5%', 'B-7,5%_D-5%', 'B-5%_D-5%', 'B-2,5%_D-5%', 'B0%_D-5%', 'B+2,5%_D-5%', 'B+5%_D-5%','B+7,5%_D-5%','B+10%_D-5%',
            'B-10%_D-4%', 'B-7,5%_D-4%', 'B-5%_D-4%', 'B-2,5%_D-4%', 'B0%_D-4%', 'B+2,5%_D-4%', 'B+5%_D-4%','B+7,5%_D-4%','B+10%_D-4%',
            'B-10%_D-3,5%', 'B-7,5%_D-3,5%', 'B-5%_D-3,5%', 'B-2,5%_D-3,5%', 'B0%_D-3,5%', 'B+2,5%_D-3,5%', 'B+5%_D-3,5%','B+7,5%_D-3,5%','B+10%_D-3,5%',
            'B-10%_D-3%', 'B-7,5%_D-3%', 'B-5%_D-3%', 'B-2,5%_D-3%', 'B0%_D-3%', 'B+2,5%_D-3%', 'B+5%_D-3%','B+7,5%_D-3%','B+10%_D-3%',
            'B-10%_D-2,5%', 'B-7,5%_D-2,5%', 'B-5%_D-2,5%', 'B-2,5%_D-2,5%', 'B0%_D-2,5%', 'B+2,5%_D-2,5%', 'B+5%_D-2,5%','B+7,5%_D-2,5%','B+10%_D-2,5%',
            'B-10%_D-2%', 'B-7,5%_D-2%', 'B-5%_D-2%', 'B-2,5%_D-2%', 'B0%_D-2%', 'B+2,5%_D-2%', 'B+5%_D-2%','B+7,5%_D-2%','B+10%_D-2%',
            'B-10%_D-1,5%', 'B-7,5%_D-1,5%', 'B-5%_D-1,5%', 'B-2,5%_D-1,5%', 'B0%_D-1,5%', 'B+2,5%_D-1,5%', 'B+5%_D-1,5%','B+7,5%_D-1,5%','B+10%_D-1,5%',
            'B-10%_D-1%', 'B-7,5%_D-1%', 'B-5%_D-1%', 'B-2,5%_D-1%', 'B0%_D-1%', 'B+2,5%_D-1%', 'B+5%_D-1%','B+7,5%_D-1%','B+10%_D-1%',
            'B-10%_D-0,5%', 'B-7,5%_D-0,5%', 'B-5%_D-0,5%', 'B-2,5%_D-0,5%', 'B0%_D-0,5%', 'B+2,5%_D-0,5%', 'B+5%_D-0,5%','B+7,5%_D-0,5%','B+10%_D-0,5%',
            'B-10%_D0%', 'B-7,5%_D0%', 'B-5%_D0%', 'B-2,5%_D0%', 'B0%_D0%', 'B+2,5%_D0%', 'B+5%_D0%','B+7,5%_D0%','B+10%_D0%',
            'B-10%_D+0,5%', 'B-7,5%_D+0,5%', 'B-5%_D+0,5%', 'B-2,5%_D+0,5%', 'B0%_D+0,5%', 'B+2,5%_D+0,5%', 'B+5%_D+0,5%','B+7,5%_D+0,5%','B+10%_D+0,5%',
            'B-10%_D+1%', 'B-7,5%_D+1%', 'B-5%_D+1%', 'B-2,5%_D+1%', 'B0%_D+1%', 'B+2,5%_D+1%', 'B+5%_D+1%','B+7,5%_D+1%','B+10%_D+1%',
            'B-10%_D+1,5%', 'B-7,5%_D+1,5%', 'B-5%_D+1,5%', 'B-2,5%_D+1,5%', 'B0%_D+1,5%', 'B+2,5%_D+1,5%', 'B+5%_D+1,5%','B+7,5%_D+1,5%','B+10%_D+1,5%',
            'B-10%_D+2%', 'B-7,5%_D+2%', 'B-5%_D+2%', 'B-2,5%_D+2%', 'B0%_D+2%', 'B+2,5%_D+2%', 'B+5%_D+2%','B+7,5%_D+2%','B+10%_D+2%',
            'B-10%_D+2,5%', 'B-7,5%_D+2,5%', 'B-5%_D+2,5%', 'B-2,5%_D+2,5%', 'B0%_D+2,5%', 'B+2,5%_D+2,5%', 'B+5%_D+2,5%','B+7,5%_D+2,5%','B+10%_D+2,5%',
            'B-10%_D+3%', 'B-7,5%_D+3%', 'B-5%_D+3%', 'B-2,5%_D+3%', 'B0%_D+3%', 'B+2,5%_D+3%', 'B+5%_D+3%','B+7,5%_D+3%','B+10%_D+3%',
            'B-10%_D+3,5%', 'B-7,5%_D+3,5%', 'B-5%_D+3,5%', 'B-2,5%_D+3,5%', 'B0%_D+3,5%', 'B+2,5%_D+3,5%', 'B+5%_D+3,5%','B+7,5%_D+3,5%','B+10%_D+3,5%',
            'B-10%_D+4%', 'B-7,5%_D+4%', 'B-5%_D+4%', 'B-2,5%_D+4%', 'B0%_D+4%', 'B+2,5%_D+4%', 'B+5%_D+4%','B+7,5%_D+4%','B+10%_D+4%',
            'B-10%_D+5%', 'B-7,5%_D+5%', 'B-5%_D+5%', 'B-2,5%_D+5%', 'B0%_D+5%', 'B+2,5%_D+5%', 'B+5%_D+5%','B+7,5%_D+5%','B+10%_D+5%',
            'B-10%_D+7,5%', 'B-7,5%_D+7,5%', 'B-5%_D+7,5%', 'B-2,5%_D+7,5%', 'B0%_D+7,5%', 'B+2,5%_D+7,5%', 'B+5%_D+7,5%','B+7,5%_D+7,5%','B+10%_D+7,5%',
            'B-10%_D+10%', 'B-7,5%_D+10%', 'B-5%_D+10%', 'B-2,5%_D+10%', 'B0%_D+10%', 'B+2,5%_D+10%', 'B+5%_D+10%','B+7,5%_D+10%','B+10%_D+10%',
            #'B-10%_D+12,5%', 'B-7,5%_D+12,5%', 'B-5%_D+12,5%', 'B-2,5%_D+12,5%', 'B0%_D+12,5%', 'B+2,5%_D+12,5%', 'B+5%_D+12,5%','B+7,5%_D+12,5%','B+10%_D+12,5%',
            'B-10%_D+15%', 'B-7,5%_D+15%', 'B-5%_D+15%', 'B-2,5%_D+15%', 'B0%_D+15%', 'B+2,5%_D+15%', 'B+5%_D+15%','B+7,5%_D+15%','B+10%_D+15%',
            ]
    return files, names
