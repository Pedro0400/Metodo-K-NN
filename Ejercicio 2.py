# Valores de la matriz de confusión
TP = 40  # Verdaderos positivos
TN = 30  # Verdaderos negativos
FP = 20  # Falsos positivos
FN = 10  # Falsos negativos

# Cálculo de las métricas
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)  # También conocida como sensibilidad
f1_measure = 2 * (precision * recall) / (precision + recall)

# Mostrar los resultados
print(f"Exactitud (Accuracy): {accuracy * 100:.2f}%")
print(f"Precisión (Precision): {precision * 100:.2f}%")
print(f"Medida F1 (F1-Measure): {f1_measure * 100:.2f}%")
