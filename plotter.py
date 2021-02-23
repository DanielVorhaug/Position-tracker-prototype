import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    
    header = []
    data = []
    
    filename = "blink.txt"
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)

        header = next(csvreader)

        for datapoint in csvreader:
            values = [float(value) for value in datapoint]
            data.append(values)

    #print(header)
    #print(data[0])
    #print(data[1])

    time = [p[0] for p in data]
    ch1 = [p[1] for p in data]
    #ch2 = [p[2] for p in data]
    
    
    
    ax1.clear()
    ax1.plot(time, ch1)#, time, ch2)
    

ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()


