from deepface import DeepFace

DeepFace.stream(
    db_path="base_datos",
    source=0,
    model_name="VGG-Face",          # Modelo de reconocimiento (ver seccion 12)
    detector_backend="opencv",      # Detector de caras (opencv = rapido)
    time_threshold=3,              # Segundos entre cada analisis
    frame_threshold=1,             # Frames de confirmacion antes de decidir
    anti_spoofing=False             # True = detectar si es foto o cara real
)