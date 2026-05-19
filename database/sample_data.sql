INSERT INTO departments VALUES
(1, 'Engineering'),
(2, 'HR'),
(3, 'Sales');

INSERT INTO employees VALUES
(101, 'Alice', 28, 70000, 1, '2021-01-15'),
(102, 'Bob', 35, 85000, 1, '2019-03-10'),
(103, 'Charlie', 30, 50000, 2, '2022-07-01'),
(104, 'David', 40, 95000, 3, '2018-09-20'),
(105, 'Eva', 25, 60000, 1, '2023-02-12');

INSERT INTO projects VALUES
(201, 'AI Platform', 1),
(202, 'Recruitment System', 2),
(203, 'CRM Upgrade', 3);

INSERT INTO employee_projects VALUES
(101, 201, 120),
(102, 201, 200),
(103, 202, 80),
(104, 203, 150),
(105, 201, 100);