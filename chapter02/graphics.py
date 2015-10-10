'''
2.3.2 Graphics 
'''
import numpy as np
import matplotlib.pyplot as plt

# R: x=rnorm(100)
x = np.random.normal(0, 1, 100)
# R: y=rnorm(100)
y = np.random.normal(0, 1, 100)
# R: plot(x,y)
# plt.scatter(x, y)
# plt.show()

# R: plot(x,y,xlab="this is the x-axis",ylab="this is the y-axis,
#         main="Plot of X vs Y")
plt.scatter(x, y,
            s=25,  # point size; default=20 
            c='red',  # color; default=blue
            marker='x'  # marker: default=o
           )
plt.xlabel("this is the x-axis")
plt.ylabel("this is the y-axis")
plt.title("Plot of X vs Y")
plt.show()

# R: pdf("Figure.pdf")
# R: plot(x,y,col="green")
# R: dev.off()
from matplotlib.backends.backend_pdf import PdfPages
with PdfPages('Figure.pdf') as pdf:
    plt.scatter(x, y, c='green')
    plt.xlabel("this is the x-axis")
    plt.ylabel("this is the y-axis")
    plt.title("Plot of X vs Y")
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()
