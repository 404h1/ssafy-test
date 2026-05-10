-- order
--	1. orders 테이블을 생성한다. 상세한 schema는 첨부 파일 참고.
--	2. orders 테이블에 서로 다른 데이터를 최소 3개 이상 삽입한다.
--		- Date 타입은 'YYYY-MM-DD' 형식으로 삽입한다.
--		- Real 타입은 10.11 형식으로 삽입 가능하다.
create table orders (
	order_id integer primery key,
	order_date date,
	total_amount real
);
insert into orders (order_id, order_date, total_amount) values (1, '2024-01-01', 15.00);
insert into orders (order_id, order_date, total_amount) values (2, '2024-01-02', 23.50);
insert into orders (order_id, order_date, total_amount) values (3, '2024-01-03', 10.99);

-- customers
--	1. customers 테이블을 생성한다. 상세한 schema는 첨부 파일 참고.
--	2. customers 테이블에 서로 다른 데이터를 최소 3개 이상 삽입한다.
create table customers(
	customer_id integer primary key,
	name text,
	email text,
	phone text
);
insert into customers (customer_id, name, email, phone) values (1, '김철수', 'kim@test.com', '010-1111-2222');
insert into customers (customer_id, name, email, phone) values (2, '이영희', 'lee@test.com', '010-3333-4444');
insert into customers (customer_id, name, email, phone) values (3, '박민수', 'park@test.com', '010-5555-6666');

-- 데이터 수정
--	1. orders의 3번째 레코드를 삭제하시오.
--	2. customers의 1번째 레코드의 name을 '홍길동'으로 수정하시오.
delete from orders where order_id = 3;
update costomers set name = '홍길동' where customer_id = 1;

-- 데이터 조회
--	1. orders와 customers의 모든 데이터를 조회하시오.
select * from orders;
select * from customers;