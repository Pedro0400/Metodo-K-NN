from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Datos de entrenamiento (X: coordenadas, y: clases)
X_train = np.array([[2, 0], [4, 4], [1, 1], [2, 4], [2, 2], [2, 3], [3, 4], [3, 3]])
y_train = np.array([0, 1, 0, 1, 0, 1, 0, 1])

# Clasificador k-NN con k=1 y usando la distancia de Manhattan
knn = KNeighborsClassifier(n_neighbors=1, metric='manhattan')
knn.fit(X_train, y_train)

# Caso a clasificar
new_point = np.array([[2.5, 2.5]])
predicted_class = knn.predict(new_point)

print(f"La clase predicha para el punto {new_point[0]} es: {predicted_class[0]}")
