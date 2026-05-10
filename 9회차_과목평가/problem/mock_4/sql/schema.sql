-- company.sqlite3 에 연결 후 이 파일 전체를 실행하세요.
-- (VSCode SQLite 확장: 우클릭 → Run Selected Query)

-- 테이블 초기화
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- 부서 테이블
CREATE TABLE departments (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT    NOT NULL,
    location TEXT    NOT NULL,
    budget   INTEGER NOT NULL
);

-- 직원 테이블
CREATE TABLE employees (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT    NOT NULL,
    department_id INTEGER NOT NULL,
    salary        INTEGER NOT NULL,
    hire_date     TEXT    NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- 부서 데이터
INSERT INTO departments (name, location, budget) VALUES ('개발', '서울', 500000000);
INSERT INTO departments (name, location, budget) VALUES ('마케팅', '부산', 300000000);
INSERT INTO departments (name, location, budget) VALUES ('인사', '서울', 200000000);
INSERT INTO departments (name, location, budget) VALUES ('영업', '대구', 250000000);

-- 직원 데이터
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('김민준', 1, 75000, '2020-03-02');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('이서연', 1, 82000, '2019-07-15');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('박지호', 2, 58000, '2021-01-10');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('최예진', 2, 61000, '2020-11-01');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('정우성', 3, 55000, '2022-03-01');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('한지민', 3, 52000, '2021-09-12');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('오승현', 1, 90000, '2018-05-20');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('임나은', 4, 63000, '2020-08-03');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('신동욱', 4, 59000, '2021-04-15');
INSERT INTO employees (name, department_id, salary, hire_date) VALUES ('강하늘', 2, 67000, '2019-12-01');

-- 확인
SELECT * FROM departments;
SELECT * FROM employees;
