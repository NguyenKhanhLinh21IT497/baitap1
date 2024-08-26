-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th6 03, 2024 lúc 02:24 PM
-- Phiên bản máy phục vụ: 10.4.22-MariaDB
-- Phiên bản PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `do-an`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `student`
--

CREATE TABLE `student` (
  `Student_ID` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Department` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Cource` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Year` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Semester` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Division` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Gender` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `DOB` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Mobile_No` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Address` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Roll_No` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Teacher_Name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `PhotoSample` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `Department`, `Cource`, `Year`, `Semester`, `Division`, `Gender`, `DOB`, `Mobile_No`, `Address`, `Roll_No`, `Email`, `Teacher_Name`, `PhotoSample`) VALUES
('1', 'ergtr', 'BSCS', 'FE', '2017-21', 'Semester-3', 'Morning', 'Female', '2003', '987654321', 'gtgt', 'btrg', '4f', 'ab', 'Yes');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
