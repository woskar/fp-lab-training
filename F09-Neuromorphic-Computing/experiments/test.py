import matplotlib.pyplot as plt
import numpy as np
'''
m1 = [[1,2],[3,4]]
m2 = [[1e-5,2e-5], [3,4]]

plt.imshow(m1)
plt.colorbar()
plt.show()
'''


#m2 = np.loadtxt('cc_matrix.txt').reshape((192,192))


#m = [[0.0049333144022022787, 0.004677076654137623, 0.0046609739994486893, 0.0035820358136597185, 0.0046095859585675823], 
#     [0.0050705800628593235, 0.0071339563690452704, 0.0084458602869795438, 0.0089687613152875361, 0.0080704710152427559], 
#     [0.0043054013845164616, 0.0066251856699024118, 0.0064010534713552208, 0.0087528437415155484, 0.0073875294768343111], 
#     [0.0069818731631138059, 0.0054796349564773502, 0.0060892564005755852, 0.0070882972806690326, 0.0093330630324417758], 
#     [0.0039608294874569575, 0.0066632233468752978, 0.0062258194974134937, 0.0076880022800159499, 0.0073526459261012535]]

m = [[-0.0003988831767506078, -0.0014249840945106652, -0.00026084757347639558, 4.7069313706402482e-05, -0.0018233842517164907, -9.4644895867226564e-05], [0.00060245649202823176, -0.00071677159877158369, 0.00020763588735757383, 0.00097506744834363471, 0.00045980275639864911, 0.0013363378210426832], [-0.00033677862759616919, 0.00059094522328296227, 0.0002523339756323402, 0.00073487990739628866, 0.002266717818987682, 0.0018588993813916492], [0.0003231333760119673, 0.00046726479269917426, 0.00080749611633512805, -9.2780619688309052e-05, 1.2681788622339337e-05, 0.00071524127077101491], [0.0006904033735156066, 0.0010400029621285974, -0.00044427923927055563, 0.00072406352779429627, -0.00069308322145196174, 0.0015643250425268521], [-0.00042212646635137732, 0.0004114831424692561, 4.3042575649986709e-05, 0.0013704165817258114, -0.00087051493325246453, 0.00091141986325254368]]



#plt.imshow(np.log(m))
#plt.colorbar()
#plt.show()
m = np.array(m)

plt.pcolor(m, cmap=plt.cm.jet)
#np.savetxt('avg_cvs_over_w_and_K.txt', avg_cvs_over_w_and_K)
#print('shape of avg_cvs_over_w_and_K', np.shape(avg_cvs_over_w_and_K))
plt.title("Average Correlation without Diagonal over w and K")
plt.xlabel("Number of presynaptic partners K")
plt.ylabel("Inhibitory weight w")

plt.colorbar()
plt.savefig('6-3-correlation-without-diagonal-over-w-and-k.png')
#plt.show()
plt.clf()