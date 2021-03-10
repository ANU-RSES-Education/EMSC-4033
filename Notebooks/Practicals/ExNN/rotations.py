import numpy as np
def rotation_about(axis,angle):
    cth = np.cos(np.deg2rad(angle))
    sth = np.sin(np.deg2rad(angle))
    if axis=='x':
        return np.array([[1,0,0],[0,cth,-sth],[0,sth,cth]])
    elif axis=='y':
        return np.array([[cth,0,-sth],[0,1,0],[sth,0,cth]])
    elif axis=='z':
        return np.array([[cth,-sth,0],[sth,cth,0],[0,0,1]])
    else:
        raise ValueError('Unrecognised axis')
def rotation_list(rots):
    R = np.eye(3)
    for ax,ang in rots:
        R = rotation_about(ax,ang).dot(R)
    return R