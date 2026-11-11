from deepface import DeepFace
import cv2
import os

# ═══ CONFIGURACION ═══
CARPETA_BD = "base_datos"     # Carpeta con fotos conocidas
FRECUENCIA = 45               # Analizar cada X frames (~1.5 seg a 30fps)

# ═══ Abrir la webcam ═══
camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("Error: no se pudo abrir la camara.")
    exit()

print("Webcam abierta. Pulsa 'q' para salir.")

# ═══ Variables que guardan el ultimo resultado ═══
contador = 0
nombre_actual = "?"
emocion_actual = "?"
edad_actual = "?"
x, y, ancho, alto = 0, 0, 0, 0
hay_cara = False

# ═══ BUCLE PRINCIPAL ═══
while True:
    ret, frame = camara.read()
    if not ret:
        break

    contador += 1

    # ─── Cada X frames: identificar + analizar ───
    if contador % FRECUENCIA == 0:

        # PASO 1: Buscar quien es en la base de datos
        try:
            resultados_find = DeepFace.find(
                img_path=frame,
                db_path=CARPETA_BD,
                enforce_detection=False,
                silent=True
            )
            if len(resultados_find) > 0 and len(resultados_find[0]) > 0:
                mejor = resultados_find[0].iloc[0]
                ruta = mejor["identity"]
                nombre_actual = os.path.splitext(os.path.basename(ruta))[0]
            else:
                nombre_actual = "Desconocido"
        except Exception:
            nombre_actual = "?"

        # PASO 2: Analizar emocion y edad
        try:
            resultados_analisis = DeepFace.analyze(
                img_path=frame,
                actions=["emotion", "age"],
                enforce_detection=False,
                silent=True
            )
            if len(resultados_analisis) > 0:
                cara = resultados_analisis[0]
                emocion_actual = cara.get("dominant_emotion", "?")
                edad_actual = cara.get("age", "?")
                region = cara.get("region", {})
                x = region.get("x", 0)
                y = region.get("y", 0)
                ancho = region.get("w", 0)
                alto = region.get("h", 0)
                hay_cara = True
            else:
                hay_cara = False
        except Exception:
            hay_cara = False

    # ─── Dibujar resultados sobre el video ───
    if hay_cara:
        # Color: verde si esta identificado, rojo si es desconocido
        if nombre_actual not in ("Desconocido", "?"):
            color = (0, 200, 0)    # Verde
        else:
            color = (0, 0, 200)    # Rojo

        # Rectangulo alrededor de la cara
        cv2.rectangle(frame, (x, y), (x + ancho, y + alto), color, 2)

        # Nombre encima del rectangulo
        cv2.putText(frame, nombre_actual, (x, y - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Emocion y edad debajo del nombre
        cv2.putText(frame, f"{emocion_actual}, {edad_actual} year", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # ─── Mostrar el frame en la ventana ───
    cv2.imshow("DeepFace Webcam", frame)

    # ─── Teclas ───
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord("q"):
        break
    if tecla == ord("s"):
        cv2.imwrite(f"captura_{contador}.jpg", frame)
        print(f"Foto guardada: captura_{contador}.jpg")

# ═══ Limpieza al salir ═══
camara.release()
cv2.destroyAllWindows()
print("Webcam cerrada.")