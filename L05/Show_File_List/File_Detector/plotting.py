import matplotlib.pyplot as plt

def PieChart(data):
    sizes={'cpp':0,'hpp':0,'c':0,'h':0,'other':0}
    totalfiles=sum(data.values())
    for x in data:
        percent=(int(data[x])/totalfiles)*100
        sizes[x]=percent
    explode=(0,0,0,0,0)
    fig,ax=plt.subplots()
    ax.pie(sizes.values(),explode,data.keys(),autopct='%1.1f%%',shadow=True,startangle=90)
    ax.axis('equal')
    plt.show()

def BarChart(data):
    plt.rcdefaults()
    fig,ax=plt.subplots()
    plt.style.use('ggplot')
    y_pos=data.values()
    ax.barh(list(data.keys()),data.values(),align='center')
    ax.set_xlabel('NUmber of files')
    ax.set_ylabel('Files')
    ax.set_title('File Recognition(h,c,hpp,cpp)')
    plt.show()