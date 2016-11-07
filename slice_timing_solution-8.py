#- Make time vector containing start times in second of each volume,
#- relative to start of first volume.
#- Call this `slice_0_times`
slice_0_times = np.arange(fixed_data.shape[-1]) * 2.5
slice_0_times
# array([   0. ,    2.5,    5. ,    7.5,   10. ,   12.5,   15. ,   17.5,
# 20. ,   22.5,   25. ,   27.5,   30. ,   32.5,   35. ,   37.5,
# 40. ,   42.5,   45. ,   47.5,   50. ,   52.5,   55. ,   57.5,
# 60. ,   62.5,   65. ,   67.5,   70. ,   72.5,   75. ,   77.5,
# 80. ,   82.5,   85. ,   87.5,   90. ,   92.5,   95. ,   97.5,
# 100. ,  102.5,  105. ,  107.5,  110. ,  112.5,  115. ,  117.5,
# 120. ,  122.5,  125. ,  127.5,  130. ,  132.5,  135. ,  137.5,
# 140. ,  142.5,  145. ,  147.5,  150. ,  152.5,  155. ,  157.5,
# 160. ,  162.5,  165. ,  167.5,  170. ,  172.5,  175. ,  177.5,
# 180. ,  182.5,  185. ,  187.5,  190. ,  192.5,  195. ,  197.5,
# 200. ,  202.5,  205. ,  207.5,  210. ,  212.5,  215. ,  217.5,
# 220. ,  222.5,  225. ,  227.5,  230. ,  232.5,  235. ,  237.5,
# 240. ,  242.5,  245. ,  247.5,  250. ,  252.5,  255. ,  257.5,
# 260. ,  262.5,  265. ,  267.5,  270. ,  272.5,  275. ,  277.5,
# 280. ,  282.5,  285. ,  287.5,  290. ,  292.5,  295. ,  297.5,
# 300. ,  302.5,  305. ,  307.5,  310. ,  312.5,  315. ,  317.5,
# 320. ,  322.5,  325. ,  327.5,  330. ,  332.5,  335. ,  337.5,
# 340. ,  342.5,  345. ,  347.5,  350. ,  352.5,  355. ,  357.5,
# 360. ,  362.5,  365. ,  367.5,  370. ,  372.5,  375. ,  377.5,
# 380. ,  382.5,  385. ,  387.5,  390. ,  392.5,  395. ,  397.5,
# 400. ,  402.5,  405. ,  407.5,  410. ,  412.5,  415. ,  417.5,
# 420. ,  422.5,  425. ,  427.5])
