-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2017 at 06:16 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iot`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `idx` int(11) NOT NULL,
  `email` varchar(500) NOT NULL COMMENT '사용자아이디',
  `pwd` varchar(500) NOT NULL COMMENT '사용자패스워드'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='사용자정보';

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`idx`, `email`, `pwd`) VALUES
(4, 'a', 'a');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`idx`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `idx` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



CREATE TABLE IF NOT EXISTS `alarm` (
  `idx` int(11) NOT NULL AUTO_INCREMENT,
  `alarmid` varchar(500) NOT NULL COMMENT '알람 아이디',
  `userid` varchar(500) NOT NULL COMMENT '사용자 아이디',
  `name` varchar(500) NOT NULL COMMENT '센서명',
  `param` varchar(500) NOT NULL COMMENT '부호',
  `value` varchar(500) NULL COMMENT '값',
  `target` varchar(500) NULL COMMENT '작동할 모터',
  PRIMARY KEY (`idx`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='동작 정보' AUTO_INCREMENT=4 ;
