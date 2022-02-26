import numpy as np

def calculate(lists):
  list = np.array(lists)
  if list.size != 9:
    raise ValueError("List must contain nine elements")
  mat = list.reshape(3,3)
  calculation = {}
  calculation["mean"] =     [np.mean(mat,axis=0),np.mean(mat,axis=1),np.mean(mat)]
  calculation["variance"] = [np.var(mat,axis=0),np.var(mat,axis=1),np.var(mat)];
  calculation["Standard deviation"] = [np.std(mat,axis=0),np.std(mat,axis=1),np.std(mat)]
  calculation["max"] = [np.max(mat,axis=0),np.max(mat,axis=1),np.max(mat)]
  calculation["min"] = [np.min(mat,axis=0),np.min(mat,axis=1),np.min(mat)]
  calculation["sum"] = [np.sum(mat,axis=0),np.sum(mat,axis=1),np.sum(mat)]
  return calculation