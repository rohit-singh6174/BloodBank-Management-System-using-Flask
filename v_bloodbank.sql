-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2022 at 03:41 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `v_bloodbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `username`, `email`, `password`) VALUES
(1, 'Rohit Singh', 'rohit_6174', 'rohit224455@gmail.com', '$2b$12$92Hevn2ORuK49pBHEleuoujQySPqB8gAvs9fOPTv4ySNnYJajr1eK');

-- --------------------------------------------------------

--
-- Table structure for table `bloodbank`
--

CREATE TABLE `bloodbank` (
  `id` int(11) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `bloodquanity` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bloodbank`
--

INSERT INTO `bloodbank` (`id`, `bloodgroup`, `bloodquanity`) VALUES
(1, 'A+', '1200'),
(2, 'A-', '350'),
(3, 'B+', '350'),
(4, 'B-', '350'),
(5, 'O+', '800'),
(6, 'O-', '0'),
(7, 'AB+', '1150'),
(8, 'AB-', '0');

-- --------------------------------------------------------

--
-- Table structure for table `bloodreq`
--

CREATE TABLE `bloodreq` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `bloodunit` int(11) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bloodreqapproved`
--

CREATE TABLE `bloodreqapproved` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `bloodunit` int(11) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bloodtest__report`
--

CREATE TABLE `bloodtest__report` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `uhid` bigint(20) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bloodtest__report`
--

INSERT INTO `bloodtest__report` (`id`, `name`, `phone`, `uhid`, `bloodgroup`) VALUES
(1, 'Rohit Singh', 9876543211, 1234567891, 'A+'),
(3, 'Rohan Shahabaje', 8888888888, 7777777777, 'AB+'),
(4, 'Soham Sawant', 3333333333, 6666666666, 'O+'),
(6, 'Siddhi Dhumal', 2345678911, 4444444444, 'A-'),
(7, 'Saloni Parker', 9988776655, 5555555555, 'B-');

-- --------------------------------------------------------

--
-- Table structure for table `blood_approved`
--

CREATE TABLE `blood_approved` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `bloodunit` int(11) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blood_donate`
--

CREATE TABLE `blood_donate` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `bloodunit` int(11) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `blood_req_handover`
--

CREATE TABLE `blood_req_handover` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `bloodunit` int(11) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blood_req_handover`
--

INSERT INTO `blood_req_handover` (`id`, `name`, `phone`, `username`, `email`, `bloodgroup`, `district`, `bloodunit`, `date`) VALUES
(2, 'Rohit Singh', 9876543211, 'rohit_6174', 'rohit224455@gmail.com', 'A+', 'Akola', 350, '2022-04-10'),
(11, 'Rohan Shahabaje', 8888888888, 'rohan_007', 'rohan@gmail.com', 'AB+', 'Ahmednaga', 350, '2022-04-10'),
(17, 'sampledonor', 9820881695, 'sampledonor', 'sampledonor@gmail.com', 'B+', 'Ahmednaga', 350, '2022-04-17'),
(18, 'sampledonor', 9820881695, 'sampledonor', 'sampledonor@gmail.com', 'B+', 'Ahmednaga', 350, '2022-04-17');

-- --------------------------------------------------------

--
-- Table structure for table `donor`
--

CREATE TABLE `donor` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `uhid` bigint(20) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donor`
--

INSERT INTO `donor` (`id`, `name`, `phone`, `uhid`, `bloodgroup`, `district`, `username`, `email`, `password`) VALUES
(1, 'Rohit Singh', 9876543211, 1234567891, 'A+', 'Mumbai City', 'rohit_6174', 'rohit224455@gmail.com', '$2b$12$XYLVvj/LYD5w5uQHwrMgCOGvhKkckOMWDjkmtSubJ3aOOzPFKbF9S'),
(2, 'Rohan Shahabaje', 8888888888, 7777777777, 'AB+', 'Mumbai City', 'rohan_007', 'rohan@gmail.com', '$2b$12$e.G/ZkxrBamRIOWX6w45ke2RTuuRIJAUJqIsyY2qM2mkKGIhE7ov.'),
(3, 'Soham Sawant', 3333333333, 6666666666, 'O+', 'Mumbai City', 'soham', 'greatsoham@gmail.com', '$2b$12$ymbSAttEMcNHg8ygGsUMWe81w53poWyiie00vnjA5MoygYiA9dsge'),
(4, 'sampledonor', 9820881695, 3333333333, 'B+', 'Mumbai City', 'sampledonor', 'sampledonor@gmail.com', '$2b$12$DzbiXb57PccU2lXDSfNGRuicVsX9.HkXakiOoo/ii6QrjTCVR85wS'),
(6, 'Siddhi Dhumal', 2345678911, 4444444444, 'A-', 'Mumbai City', 'siddhi', 'siddhi@gmail.com', '$2b$12$2HY6NzYPNabVylhef7B37.5i8f1Mp9Omp6YoUIN5zmLZnockrsaX.'),
(7, 'Saloni Parkar', 9988776655, 5555555555, 'B-', 'Mumbai City', 'saloni', 'saloni@gmail.com', '$2b$12$dOXka1k.AwU81NmPf2iX2ugDMlQJ.WPTmPIrAUv9LB9E8jke00Efi');

-- --------------------------------------------------------

--
-- Table structure for table `handover`
--

CREATE TABLE `handover` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `bloodunit` int(11) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `handover`
--

INSERT INTO `handover` (`id`, `name`, `phone`, `username`, `email`, `bloodgroup`, `district`, `bloodunit`, `date`) VALUES
(3, 'Rohit Singh', 9876543211, 'rohit_6174', 'rohit224455@gmail.com', 'A+', 'Mumbai City', 450, '2022-04-10'),
(6, 'Rohan Shahabaje', 8888888888, 'rohan_007', 'rohan@gmail.com', 'AB+', 'Mumbai City', 350, '2022-04-10'),
(8, 'Rohit Singh', 9876543211, 'rohit_6174', 'rohit224455@gmail.com', 'A+', 'Mumbai City', 350, '2022-04-10'),
(10, 'Soham Sawant', 3333333333, 'soham', 'greatsoham@gmail.com', 'O+', 'Mumbai City', 450, '2022-04-11'),
(14, 'Rohit Singh', 9876543211, 'rohit_6174', 'rohit224455@gmail.com', 'A+', 'Mumbai City', 450, '2022-04-13'),
(18, 'sampledonor', 9820881695, 'sampledonor', 'sampledonor@gmail.com', 'B+', 'Ahmednaga', 350, '2022-04-17'),
(21, 'Siddhi Dhumal', 2345678911, 'siddhi', 'siddhi@gmail.com', 'A-', 'Mumbai City', 350, '2022-04-29'),
(22, 'Saloni Parkar', 9988776655, 'saloni', 'saloni@gmail.com', 'B-', 'Mumbai City', 350, '2022-04-29'),
(23, 'Rohit Singh', 9876543211, 'rohit_6174', 'rohit224455@gmail.com', 'A+', 'Mumbai City', 350, '2022-04-29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `bloodbank`
--
ALTER TABLE `bloodbank`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `bloodgroup` (`bloodgroup`);

--
-- Indexes for table `bloodreq`
--
ALTER TABLE `bloodreq`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `bloodreqapproved`
--
ALTER TABLE `bloodreqapproved`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `bloodtest__report`
--
ALTER TABLE `bloodtest__report`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `uhid` (`uhid`);

--
-- Indexes for table `blood_approved`
--
ALTER TABLE `blood_approved`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `blood_donate`
--
ALTER TABLE `blood_donate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `blood_req_handover`
--
ALTER TABLE `blood_req_handover`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `donor`
--
ALTER TABLE `donor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `uhid` (`uhid`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `handover`
--
ALTER TABLE `handover`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bloodbank`
--
ALTER TABLE `bloodbank`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `bloodreq`
--
ALTER TABLE `bloodreq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `bloodreqapproved`
--
ALTER TABLE `bloodreqapproved`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `bloodtest__report`
--
ALTER TABLE `bloodtest__report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `blood_approved`
--
ALTER TABLE `blood_approved`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `blood_donate`
--
ALTER TABLE `blood_donate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `blood_req_handover`
--
ALTER TABLE `blood_req_handover`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `donor`
--
ALTER TABLE `donor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `handover`
--
ALTER TABLE `handover`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
