b_f, rss_f, df_f = glm(X_f, Y)
b_r, rss_r, df_r = glm(X_r, Y)
f_stat = ((rss_r - rss_f) / nu_1) / (rss_f / df_f)
f_stat
# 6.15949...
