
def Qval_calc(Q, reaction_channel, isomer_level=None):
	t=8.5; a=28.3; d=2.2; He3=7.7
	m_t = 2808.92113298 #MrV
	m_a = 3727.3794066 # MeV
	if reaction_channel == 't':
		ch = Q - t - m_t
	elif reaction_channel == 'alpha':
		ch = Q - a

	print(ch)



Q=-1769.3
Ir_190Ir = Qval_calc(Q, 't')

#print()

