import numpy as np


def compute(point,centroid,max_dist,max_point):
    point = np.asarray(point)
    centroid = np.asarray(centroid)
    dist=np.linalg.norm(point-centroid)
    if dist>max_dist:
        max_dist=dist
        max_point=point
    return max_dist,max_point

def main():

    a = np.array(
        [
        [0,0,0,0,0,0],
        [0,0,1,1,0,0],
        [0,1,1,1,1,0],
        [0,1,1,1,1,0],
        [0,0,1,1,1,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,0]]
    )
    p = np.zeros(a.shape,dtype='int')
    max_dist = 0
    centroid = [0,0]
    max_point =[0,0]
    for i in range(a.shape[0]):
        start = False
        for j in range(a.shape[1]):
            if a[i,j]==1:
                start =True
            if a[i,j]==1 and start and a[i,j-1]==0:
                p[i,j]=1
                max_dist,max_point = compute([i,j],centroid,max_dist,max_point)

            if a[i,j]==1 and start and a[i,j+1]==0:
                p[i,j]=1
                max_dist,max_point = compute([i,j],centroid,max_dist,max_point)

    for i in range(a.shape[0]):
        start = False
        for j in range(a.shape[1]):
            if a[i,j]==1:
                start =True
            if a[i,j]==1 and start and a[i-1,j]==0:
                p[i,j]=1
                max_dist,max_point = compute([i,j],centroid,max_dist,max_point)
            if a[i,j]==1 and start and a[i+1,j]==0:
                p[i,j]=1
                max_dist,max_point = compute([i,j],centroid,max_dist,max_point)
    
if __name__ == '__main__':
    main()
