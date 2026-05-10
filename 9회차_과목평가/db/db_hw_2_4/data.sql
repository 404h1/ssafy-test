-- 1. customers 테이블 생성
-- 2. customers 데이터 삽입
-- 3. orders 테이블 생성 (FK 참조 가능)
-- 4. orders 수정 (ALTER)
-- 5. orders 데이터 삽입
-- 6. JOIN 조회

-- customers 테이블 생성: 고객 정보를 저장하기 위한 테이블
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, -- 고객 ID (기본 키)
    name TEXT,                      -- 고객 이름 (텍스트 타입)
    email TEXT,                     -- 고객 이메일 (텍스트 타입)
    phone TEXT                      -- 고객 전화번호 (텍스트 타입)
);

-- customers 테이블에 데이터 삽입
INSERT INTO customers (name, email, phone) VALUES
    ('허균', 'hong.gildong@example.com', '010-1234-5678'),    -- 허균 고객 정보
    ('김영희', 'kim.younghee@example.com', '010-9876-5432'),  -- 김영희 고객 정보
    ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');    -- 이철수 고객 정보


-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    total_amount REAL               -- 총 주문 금액 (실수 타입)
);

-- orders 테이블에 데이터 삽입
INSERT INTO orders (order_id, order_date, total_amount) VALUES
    (1, '2023-07-15', 50.99),      -- 2023년 7월 15일 주문, 총 주문 금액: 50.99
    (2, '2023-07-16', 75.50),      -- 2023년 7월 16일 주문, 총 주문 금액: 75.50
    (3, '2023-07-17', 30.25);      -- 2023년 7월 17일 주문, 총 주문 금액: 30.25

-- orders 테이블을 삭제한다.
-- orders 테이블을 첨부 파일을 참고하여 다시 생성한다. customer와 관계를 형성한다.
drop table orders;
create table orders (
	order_id integer primary key,
	order_date date,
	total_amount real, 
    customer_id integer,
	foreign key (customer_id) references customers(customer_id)
);

-- 쿼리문을 사용하여 orders 테이블을 수정한다
-- orders 테이블에 Integer 타입의 price 컬럼 추가한다.
-- orders 테이블의 total_amount 컬럼을 삭제한다.
alter table orders add column price integer;
alter table orders drop column total_amount;

-- orders 테이블에 데이터를 최소 3개 이상 생성한다.
-- Date 타입은 'YYYY-MM-DD' 형식으로 삽입한다.
-- Real 타입은 10.11 형식으로 삽입한다.
-- 데이터를 생성할 때 customers_id도 함께 삽입한다.
insert into orders (order_id, order_date, customer_id, price) values (1, '2024-01-01', 1, 15000);
insert into orders (order_id, order_date, customer_id, price) values (2, '2024-01-02', 2, 23000);
insert into orders (order_id, order_date, customer_id, price) values (3, '2024-01-03', 3, 10000);

-- orders의 모든 데이터를 조회한다. 단, 관계를 맺고 있는 customers의 name도 함께 출력한다.
select orders.*, customers.name
from orders
join customers on orders.customer_id = customers.customer_id;