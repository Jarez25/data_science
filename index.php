<?php

$meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"];
$ventas_2023 = [0, 0, 0, 395420.81, 509526.92, 353176.34, 349377.88, 478985.38, 390399.08, 433253.70, 314806.35, 337565.10];
$ventas_2024 = [415870.59, 387472.95, 309609.47, 438305.18, 316628.25, 658289.62, 228714.61, 0, 0, 0, 0, 0];

$width = 800;
$height = 600;

$image = imagecreatetruecolor($width, $height);

$white = imagecolorallocate($image, 255, 255, 255);
$black = imagecolorallocate($image, 0, 0, 0);
$red = imagecolorallocate($image, 255, 0, 0);
$blue = imagecolorallocate($image, 0, 0, 255);

imagefill($image, 0, 0, $white);

$font_size = 4;
$margins = 40;
$graph_width = $width - 2 * $margins;
$graph_height = $height - 2 * $margins;

$max_value = max(max($ventas_2023), max($ventas_2024));

for ($i = 0; $i < count($meses); $i++) {
    $x = $margins + $i * ($graph_width / (count($meses) - 1));
    
    // Línea y puntos para 2023
    if ($i > 0) {
        imageline(
            $image,
            $last_x_2023,
            $last_y_2023,
            $x,
            $margins + $graph_height - ($ventas_2023[$i] / $max_value) * $graph_height,
            $red
        );
    }
    imagefilledellipse(
        $image,
        $x,
        $margins + $graph_height - ($ventas_2023[$i] / $max_value) * $graph_height,
        8,
        8,
        $red
    );
    $last_x_2023 = $x;
    $last_y_2023 = $margins + $graph_height - ($ventas_2023[$i] / $max_value) * $graph_height;

    // Línea y puntos para 2024
    if ($i > 0) {
        imageline(
            $image,
            $last_x_2024,
            $last_y_2024,
            $x,
            $margins + $graph_height - ($ventas_2024[$i] / $max_value) * $graph_height,
            $blue
        );
    }
    imagefilledellipse(
        $image,
        $x,
        $margins + $graph_height - ($ventas_2024[$i] / $max_value) * $graph_height,
        8,
        8,
        $blue
    );
    $last_x_2024 = $x;
    $last_y_2024 = $margins + $graph_height - ($ventas_2024[$i] / $max_value) * $graph_height;
}

// Etiquetas de los ejes
for ($i = 0; $i < count($meses); $i++) {
    $x = $margins + $i * ($graph_width / (count($meses) - 1));
    imagestring($image, $font_size, $x - 10, $height - $margins + 10, $meses[$i], $black);
}

for ($i = 0; $i <= 10; $i++) {
    $y = $margins + $i * ($graph_height / 10);
    $value = round($max_value * (1 - $i / 10), 2);
    imagestring($image, $font_size, 5, $y - 7, $value, $black);
    imageline($image, $margins, $y, $width - $margins, $y, $black);
}

// Título y etiquetas
imagestring($image, 5, ($width - 7 * strlen('Crecimiento o Decrecimiento de las Ventas por Mes')) / 2, 10, 'Crecimiento o Decrecimiento de las Ventas por Mes', $black);
imagestring($image, 4, ($width - 6 * strlen('Mes')) / 2, $height - 20, 'Mes', $black);
imagestringup($image, 4, 10, ($height + 7 * strlen('Ventas')) / 2, 'Ventas', $black);

// Mostrar la imagen
header('Content-Type: image/png');
imagepng($image);
imagedestroy($image);

?>
