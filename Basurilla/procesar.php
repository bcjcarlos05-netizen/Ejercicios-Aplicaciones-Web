<?php
// 1. Recoger los datos enviados por el formulario
$nombre = trim($_POST["nombre"] ?? "");
$email = trim($_POST["email"] ?? "");
$edad = trim($_POST["edad"] ?? "");
$curso = trim($_POST["curso"] ?? "");
$comentario = trim($_POST["comentario"] ?? "");

// 2. Preparar los datos para mostrarlos de forma segura
$nombreSeguro = htmlspecialchars($nombre, ENT_QUOTES, "UTF-8");
$emailSeguro = htmlspecialchars($email, ENT_QUOTES, "UTF-8");
$edadSegura = htmlspecialchars($edad, ENT_QUOTES, "UTF-8");
$cursoSeguro = htmlspecialchars($curso, ENT_QUOTES, "UTF-8");
$comentarioSeguro = htmlspecialchars($comentario, ENT_QUOTES, "UTF-8");

// 3. Mostrar el resultado
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inscripción recibida</title>
</head>
<body>
    <h1>¡Inscripción recibida!</h1>
    <p>Estos son los datos que has enviado:</p>
    <ul>
        <li><strong>Nombre:</strong> <?= $nombreSeguro ?></li>
        <li><strong>Correo:</strong> <?= $emailSeguro ?></li>
        <li><strong>Edad:</strong> <?= $edadSegura ?></li>
        <li><strong>Curso:</strong> <?= $cursoSeguro ?></li>
        <li><strong>Comentario:</strong><br>
            <?= nl2br($comentarioSeguro) ?>
        </li>
    </ul>
    <p><a href="formulario.html">Volver al formulario</a></p>
</body>
</html>
