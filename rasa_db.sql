-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 01, 2024 at 05:19 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rasa_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`id`, `name`) VALUES
(1, 'MSI'),
(2, 'DELL'),
(3, 'ASUS'),
(4, 'ACER');

-- --------------------------------------------------------

--
-- Table structure for table `laptop`
--

CREATE TABLE `laptop` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `brand_id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `config` longtext NOT NULL,
  `weight` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laptop`
--

INSERT INTO `laptop` (`id`, `name`, `price`, `brand_id`, `description`, `config`, `weight`) VALUES
(2, 'Asus VivoBook S 14', 11490000, 3, 'Asus VivoBook S 14 là dòng laptop văn phòng xuất sắc của Asus', 'Model  Intel® Core i3-1315U Gen 13th', '1.4 kg'),
(3, 'Asus Zenbook 14 OLED', 22690000, 3, 'Asus Zenbook 14 OLED mang đến một trải nghiệm hoàn toàn mới với thiết kế vượt trội, vật liệu nhôm cao cấp và màn hình OLED QHD+ 2.8K', 'Model  Intel® Core i5-1340P Gen 13th', '1.35 kg'),
(4, 'MSI Modern 14 B5M', 9990000, 1, 'MSI Modern 14 là dòng laptop văn phòng đẳng cấp dành cho những người yêu thích sự hiện đại và sáng tạo.', 'Model  AMD Ryzen™ R5-5500U', '1.3 kg'),
(5, 'MSI Modern 14 C7M', 10490000, 1, 'MSI Modern 14 là dòng laptop văn phòng với kích thước gọn nhẹ với CPU Ryzen 7000 series và SSD M.2 PCIe Gen3', 'Model  AMD Ryzen™ R7-7730U', '1.4 kg'),
(6, 'MSI Bravo 15 B7ED', 15990000, 1, 'Mang trong mình sức mạnh từ sự kết hợp của vi xử lý CPU AMD Ryzen 7000 và card đồ họa VGA AMD Radeon™ RX, đem lại hiệu năng vượt trội cho cả công việc và giải trí.', 'Model  AMD Ryzen™ R5-7535HS', '2.35 kg'),
(7, 'MSI GS66', 17990000, 1, 'Msi gs66 stealth không chỉ chứng minh được bản thân là một chiếc laptop gaming cao cấp mà còn là một máy tính xách tay di động mạnh mẽ bằng cách trang bị trên mình bộ cấu hình khủng', 'Chip Intel Core I7', '2 kg'),
(8, 'Dell Vostro 15 V3530', 21590000, 2, 'Laptop Dell Vostro 15 3530 là sự kết hợp hoàn hảo giữa thiết kế đẹp mắt và hiệu suất mạnh mẽ', 'Model  Intel® Core i3-1355U Gen 13th', '1.6 kg'),
(9, 'Dell Inspiron 14 5430', 28990000, 2, 'Dell inspiron 14 5430 là một tác phẩm độc đáo trong thế giới laptop, kết hợp hoàn hảo giữa thiết kế tinh tế và hiệu năng mạnh mẽ.', 'Model  Intel® Core i7-1360P Gen 13th', '1.5 kg'),
(10, 'Acer Nitro 5 Tiger', 19990000, 4, 'Có thể nói Acer Nitro 5 Tiger là một viên ngọc sáng trong dòng laptop gaming ở phân khúc tầm trung', 'Model  Intel® Core i5-12500H Gen 12th', '2.5 kg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `laptop`
--
ALTER TABLE `laptop`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `laptop`
--
ALTER TABLE `laptop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
