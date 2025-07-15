-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.4.3 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para tourism
CREATE DATABASE IF NOT EXISTS `tourism` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tourism`;

-- Volcando estructura para tabla tourism.reservas
CREATE TABLE IF NOT EXISTS `reservas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `paquete_id` int NOT NULL,
  `nombre_destino` varchar(255) NOT NULL,
  `duracion` varchar(50) DEFAULT NULL,
  `mes` varchar(50) DEFAULT NULL,
  `incluye` text,
  `fecha_reserva` date NOT NULL,
  `numero_personas` int NOT NULL,
  `precio_total` decimal(10,2) NOT NULL,
  `imagen` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla tourism.reservas: ~2 rows (aproximadamente)
INSERT INTO `reservas` (`id`, `nombre`, `email`, `paquete_id`, `nombre_destino`, `duracion`, `mes`, `incluye`, `fecha_reserva`, `numero_personas`, `precio_total`, `imagen`) VALUES
	(7, 'Mel', 'lola@gmail.com', 8, 'Nueva York - EEUU', '7 noches', 'Junio', 'Vuelo, Traslados, Hotel', '2026-02-21', 2, 4001400.00, 'https://www.turismonuevayork.com/wp-content/uploads/2018/10/12a-760x500.jpg'),
	(8, 'diana', 'melu@gmail.com', 3, 'Bariloche - Argentina', '4 noches', 'Junio', 'Bus, Hotel, Seguro', '2025-07-31', 1, 605000.00, 'https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcR1uIUCEbbRvDd3Zq-zext69c9b2QVtlMcQwhsRB77eEXus8IQU5SZbHBT53VHVFoHPb8JOkTRFyUFhmVQUeL6ud57TH4BtNYrEhhIu7w');

-- Volcando estructura para tabla tourism.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla tourism.usuarios: ~0 rows (aproximadamente)
INSERT INTO `usuarios` (`id`, `username`, `password`) VALUES
	(1, 'usuario1', 'scrypt:32768:8:1$GZ60ZTNFyHNqUXoa$4ff4bbbfc13794e1ecb05a5e1f38c6811c8da3a26b1e9b693cf162eb45d6cf324832c2b40e3890356649681122f6bc7d86311a399534dbb03b9888370c8bc401');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
