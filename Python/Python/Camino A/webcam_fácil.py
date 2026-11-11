from deepface import DeepFace

# ─── UNA SOLA LINEA: webcam + reconocimiento + emociones ───
DeepFace.stream(
    db_path="Base_datos",   # Carpeta con fotos conocidas
    source=0                 # 0 = tu webcam principal
)