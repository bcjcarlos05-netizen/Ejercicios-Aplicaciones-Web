from deepface import DeepFace
import cv2

print("===========================")
print("  VERIFICACION DEL SISTEMA")
print("===========================")
print(f"Python:   OK")
print(f"DeepFace: {DeepFace.__version__}")
print(f"OpenCV:   {cv2.__version__}")
print("===========================")
print("Todo instalado correctamente!")