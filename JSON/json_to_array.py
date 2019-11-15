import json
import numpy as np

def load_json(fname):
	f = open(fname)
	data = json.loads(f.read())
	vertices = data['vertices']
	faces = data['faces']
	return vertices,faces

def json_to_array(vertices,faces):
	N = len(faces)
	
	res = []
	for face in faces:
		m = len(face)
		a = vertices[face[0]-1]
		
		for i in range(2,len(face)):
			b = vertices[face[i-1]-1]
			c = vertices[face[i]-1]
			res.append([a,b,c])
			
	return np.array(res)

if __name__ == "__main__":
	v,f = load_json("./car_models_json/baoshijie-kayan.json")
	
	print(len(v))
	print(len(f))
	
	X = json_to_array(v,f)
	print(X.shape)
	print(X)
	
