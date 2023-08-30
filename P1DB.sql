-- Create database
create database P1;

use P1;

-- Create tables
create table Entry (
    ID   int not null,
    Time timestamp
);

create table Users (
    ID     int not null,
    Type   varchar(255), -- Unauthorized, Admin, Staff, Student
    Status varchar(255), -- Active, Inactive, Suspend
    primary key (ID)
);

-- Create dummy users
insert into Users values (1, 'Admin', 'Active');
insert into Users values (123, 'Student', 'Suspended');
insert into Users values (999, 'Unauthorized', 'Active');
