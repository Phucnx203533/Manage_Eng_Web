-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2023 at 10:55 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tlc_web`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `userId` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Role` int(100) NOT NULL,
  `rememberlogin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`userId`, `Email`, `Password`, `Role`, `rememberlogin`) VALUES
('GV0000', 'GV0000@gmail.com', '123456', 2, 0),
('GV0001', 'GV0001@gmail.com', '123456', 2, 1),
('GV0002', 'GV0002@gmail.com', '123456', 2, 0),
('GV0003', 'GV0003@gmail.com', '123456', 2, 0),
('GV0004', 'GV0004@gmail.com', '123456', 2, 0),
('TLC203533', 'tlc203533@tlc.com', '123456', 1, 0),
('TLC203534', 'tlc203534@gmail.com', '123456', 1, 0),
('TLC203535', 'tlc203535@gmail.com', '123456', 1, 0),
('TLC203536', 'tlc203536@gmail.com', '123456', 1, 0),
('TLC203537', 'tlc203537@gmail.com', '123456', 1, 0),
('TLC203538', 'tlc203538@gmail.com', '123456', 1, 0),
('TLC203539', 'tlc203539@gmail.com', '123456', 1, 0),
('TLC203540', 'tlc203540@gmail.com', '123456', 1, 0),
('TLC203541', 'tlc203541@gmail.com', '123456', 1, 0),
('TLC203542', 'tlc203542@gmail.com', '123456', 1, 0),
('TLC203543', 'tlc203543@gmail.com', '123456', 1, 0),
('TLC203544', 'tlc203544@gmail.com', '123456', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `MaLop` varchar(255) NOT NULL,
  `MaGV` varchar(255) NOT NULL,
  `TenLop` varchar(255) NOT NULL,
  `tution` float NOT NULL,
  `ThoiGian` varchar(255) NOT NULL,
  `datestart` date DEFAULT NULL,
  `DiaDiem` varchar(255) NOT NULL,
  `SoLuongHV` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`MaLop`, `MaGV`, `TenLop`, `tution`, `ThoiGian`, `datestart`, `DiaDiem`, `SoLuongHV`) VALUES
('ENG0000', 'GV0001', 'TOIEC 600', 12000000, 'Thứ 2, 17h30 - 19h30', '2023-02-13', 'D3-201', 0),
('ENG0001', 'GV0002', 'TOIEC 650', 12000000, 'Thứ 2, 17h30 - 19h30', '2023-02-13', 'D3-201', 0),
('ENG0002', 'GV0002', 'TOIEC 650', 12000000, 'Thứ 2, 17h30 - 19h30', '2023-02-13', 'D3-201', 0),
('ENG0003', 'GV0003', 'TOIEC 700', 12000000, 'Thứ 2, 17h30 - 19h30', '2023-02-13', 'D3-201', 0),
('ENG0004', 'GV0004', 'TOIEC 750', 12000000, 'Thứ 2, 17h30 - 19h30', '2023-02-13', 'D3-201', 0);

-- --------------------------------------------------------

--
-- Table structure for table `grade`
--

CREATE TABLE `grade` (
  `MaHV` varchar(255) NOT NULL,
  `MaLop` varchar(255) NOT NULL,
  `DiemGK` double NOT NULL,
  `DiemCK` double NOT NULL,
  `NhanXet` text NOT NULL,
  `DiemTK` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `grade`
--

INSERT INTO `grade` (`MaHV`, `MaLop`, `DiemGK`, `DiemCK`, `NhanXet`, `DiemTK`) VALUES
('TLC203533', 'ENG0000', 10, 8, 'Học dốt', 8.6),
('TLC203533', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203533', 'ENG0002', 8.3, 8.8, '', 0),
('TLC203533', 'ENG0003', 8.3, 8.8, '', 0),
('TLC203533', 'ENG0004', 8.3, 8.8, '', 0),
('TLC203534', 'ENG0000', 10, 10, '', 10),
('TLC203534', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203535', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203535', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203536', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203536', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203537', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203537', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203538', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203538', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203539', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203539', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203540', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203540', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203541', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203541', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203542', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203542', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203543', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203543', 'ENG0001', 8.3, 8.8, '', 0),
('TLC203544', 'ENG0000', 8.3, 8.8, '', 0),
('TLC203544', 'ENG0001', 8.3, 8.8, '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE `salary` (
  `MaGV` varchar(255) NOT NULL,
  `SoBuoi` int(11) NOT NULL,
  `LuongBuoi` double NOT NULL,
  `paid` int(11) NOT NULL,
  `TGNhan` date NOT NULL,
  `Thuong` double NOT NULL,
  `MaLuong` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`MaGV`, `SoBuoi`, `LuongBuoi`, `paid`, `TGNhan`, `Thuong`, `MaLuong`) VALUES
('GV0001', 19, 200, 0, '0000-00-00', 200, 'GV0001022023'),
('GV0002', 11, 300, 0, '0000-00-00', 300, 'GV0002022023'),
('GV0003', 13, 200, 0, '0000-00-00', 400, 'GV0003022023'),
('GV0004', 10, 300, 0, '0000-00-00', 500, 'GV0004022023');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `HoTen` varchar(255) NOT NULL,
  `NTNS` date NOT NULL,
  `SDT` varchar(255) NOT NULL,
  `DiaChi` varchar(255) NOT NULL,
  `GioiTinh` varchar(255) NOT NULL,
  `fileImg` varchar(255) NOT NULL,
  `TrinhDo` varchar(10000) NOT NULL,
  `MaGV` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`HoTen`, `NTNS`, `SDT`, `DiaChi`, `GioiTinh`, `fileImg`, `TrinhDo`, `MaGV`, `Email`) VALUES
('Nguyễn Thị A', '2023-01-18', '', 'Hà Nam', 'Nữ', 'GV0001.jpg', 'ielts:9.5', 'GV0001', '1@gmail.com'),
('Nguyễn Văn B', '2022-05-23', '010212', 'Hà nội', 'Nam', 'GV0002.jpg', 'ielts:9.5', 'GV0002', '1@gmail.com'),
('Nguyễn Thị b', '2023-01-18', '01234467', 'Hà nội', 'Nữ', 'GV0003.jpg', 'ielts:9.0', 'GV0003', '1@gmail.com'),
('Nguyễn Văn R', '2022-05-23', '010212', 'Hà nội', 'Nam', 'GV0004.jpg', 'ielts:9.5', 'GV0004', '1@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tution`
--

CREATE TABLE `tution` (
  `MaHV` varchar(255) NOT NULL,
  `MaLop` varchar(255) NOT NULL,
  `HPLop` double NOT NULL,
  `paid` int(11) NOT NULL,
  `TGThu` date NOT NULL,
  `completed` int(11) NOT NULL,
  `MaHP` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tution`
--

INSERT INTO `tution` (`MaHV`, `MaLop`, `HPLop`, `paid`, `TGThu`, `completed`, `MaHP`) VALUES
('TLC203533', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203533', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203533', 'ENG0002', 12000000, 0, '2023-01-05', 0, 0),
('TLC203533', 'ENG0003', 12000000, 0, '2023-01-05', 0, 0),
('TLC203533', 'ENG0004', 12000000, 0, '2023-01-05', 0, 0),
('TLC203534', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203534', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203535', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203535', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203536', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203536', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203537', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203537', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203538', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203538', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203539', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203539', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203540', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203540', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203541', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203541', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203542', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203542', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203543', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203543', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0),
('TLC203544', 'ENG0000', 12000000, 0, '2023-01-05', 0, 0),
('TLC203544', 'ENG0001', 12000000, 0, '2023-01-05', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `MaHV` varchar(255) NOT NULL,
  `HoTen` varchar(255) NOT NULL,
  `NTNS` date NOT NULL,
  `SDT` varchar(255) NOT NULL,
  `DiaChi` varchar(255) NOT NULL,
  `GioiTinh` varchar(255) NOT NULL,
  `fileImg` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`MaHV`, `HoTen`, `NTNS`, `SDT`, `DiaChi`, `GioiTinh`, `fileImg`, `Email`) VALUES
('TLC203533', 'Nguyễn Xuân Phúc', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203533.jpg', '1@gmail.com'),
('TLC203534', 'Nguyễn Xuân Phúc 2', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203534.jpg', '1@gmail.com'),
('TLC203535', 'Nguyễn Xuân Phúc 5', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203535.jpg', '1@gmail.com'),
('TLC203536', 'Nguyễn Xuân Phúc 6', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203536.jpg', '1@gmail.com'),
('TLC203537', 'Nguyễn Xuân Phúc 7', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203537.jpg', '1@gmail.com'),
('TLC203538', 'Nguyễn Xuân Phúc 8', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203538.jpg', '1@gmail.com'),
('TLC203539', 'Nguyễn Xuân Phúc 9', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203539.jpg', '1@gmail.com'),
('TLC203540', 'Nguyễn Xuân Phúc 40', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203540.jpg', '1@gmail.com'),
('TLC203541', 'Nguyễn Xuân Phúc 41', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203541.jpg', '1@gmail.com'),
('TLC203542', 'Nguyễn Xuân Phúc 42', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203542.jpg', '1@gmail.com'),
('TLC203543', 'Nguyễn Xuân Phúc 43', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203543.jpg', '1@gmail.com'),
('TLC203544', 'Nguyễn Xuân Phúc 44', '2022-05-23', '012345678', 'Hà Nội', 'Nam', 'TLC203544.jpg', '1@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`userId`);

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`MaLop`);

--
-- Indexes for table `grade`
--
ALTER TABLE `grade`
  ADD PRIMARY KEY (`MaHV`,`MaLop`),
  ADD KEY `grade_ibfk_1` (`MaLop`);

--
-- Indexes for table `salary`
--
ALTER TABLE `salary`
  ADD UNIQUE KEY `mTeacher` (`MaGV`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`MaGV`),
  ADD UNIQUE KEY `mTeacher` (`MaGV`);

--
-- Indexes for table `tution`
--
ALTER TABLE `tution`
  ADD PRIMARY KEY (`MaHV`,`MaLop`),
  ADD KEY `mClass` (`MaLop`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD UNIQUE KEY `userId` (`MaHV`) USING BTREE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
