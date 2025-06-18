
import numpy as np        
import matplotlib.pyplot as plt
from DBConfig import DBConnection


database = DBConnection.getConnection()
cursor = database.cursor()


# set width of bar
class bargraph:
    def view():
        plt.clf()
        algo=['LR', 'RF', 'DT', 'NN', 'SVM']
        a1=[];a2=[]
        for a in algo:
            cursor.execute("select accuracy from evaluations where algorithm='"+str(a)+"' and dataset='Testset1' ")
            row = cursor.fetchall()
       
            for r in row:
                a1.append(float(r[0]))

            cursor.execute("select accuracy from evaluations where algorithm='"+str(a)+"' and dataset='Testset2' ")
            row = cursor.fetchall()
       
            for r in row:
                a2.append(float(r[0]))

        k = []
        v = []
        barWidth = 0.25
        fig = plt.subplots(figsize=(12, 8))
        IT = [12, 30, 1, 8, 22]
        ECE = [28, 6, 16, 5, 10]
        CSE = [29, 3, 24, 25, 17]
        br1 = np.arange(len(a1))
        br2 = [x + barWidth for x in br1]
        
        print(a1,a2)
        plt.bar(br1, a1, color='b', width=barWidth,
                edgecolor='grey', label='Testset1')
        plt.bar(br2, a2, color='r', width=barWidth,
                edgecolor='grey', label='Testset2')
        plt.xlabel('Algorithms ', fontweight='bold', fontsize=15) 
        plt.ylabel('Accuracy', fontweight='bold', fontsize=15)
        plt.xticks([r + barWidth for r in range(len(a1))],algo)
        plt.legend()
        plt.savefig('D:\\MAJOR-PROJECT\\Protein Sequences - V2 (2) new\\Protein Sequences - V2 new\\static\\assets\\images\\g1.jpg', dpi = (200))
    
if __name__ == '__main__':
    bargraph.view()
