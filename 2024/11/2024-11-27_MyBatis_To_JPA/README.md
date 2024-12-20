# MyBatis To JPA

오늘은 친구가 참여한 프로젝트에서 MyBatis로 되어있는 서비스를 JPA로 새로 개발해야 한다고 하여 알아보던 김에 **MyBatis에서 JPA로 전환**하는 과정과 이에 따른 주의사항에 대해 정리해보려고 한다.  
MyBatis는 SQL 중심의 매퍼 프레임워크로 강력한 제어권을 제공하지만, 대규모 프로젝트나 유지보수 관점에서 JPA의 생산성과 유연성이 필요하다고 느껴 전환을 고려하는 경우가 많다.  

---

## MyBatis와 JPA의 차이점

### **1. SQL 제어와 자동화의 차이**
- **MyBatis**: 개발자가 직접 SQL을 작성하고 이를 코드와 매핑.  
  SQL의 유연성과 제어력을 제공하며, 복잡한 쿼리를 처리하는 데 유리하다.
- **JPA**: 엔터티와 데이터베이스 간의 매핑을 통해 SQL을 자동 생성.  
  기본적인 CRUD 작업을 간단히 처리하고 객체 지향 설계와 잘 어울린다.

---

## MyBatis에서 JPA로 전환하는 방법

### **1) 데이터 모델링 검토**
- JPA는 **객체 지향 프로그래밍**과 **엔터티 기반 설계**를 중심으로 작동하므로, 기존 데이터베이스 모델이 이를 잘 지원하는지 검토해야 한다.
- 테이블 간 관계를 **OneToOne**, **OneToMany**, **ManyToMany** 등의 엔터티 매핑으로 전환한다.
  - 예: 
    - 사용자와 역할의 관계를 `@OneToMany` 또는 `@ManyToOne`으로 설정.
    - 조인 테이블 구조는 `@JoinTable`로 매핑.

---

### **2) CRUD 작업 전환**
- MyBatis에서 작성된 기본 CRUD 쿼리를 JPA의 **Spring Data JPA 리포지토리**로 전환.
- MyBatis의 매퍼 XML에 작성된 쿼리를 분석하고, JPA 리포지토리 메서드로 변환.
  - 예: MyBatis의 `SELECT * FROM users WHERE id = #{id}` → JPA의 `findById(Long id)` 메서드.
  - JPA의 기본 메서드: `save`, `findById`, `findAll`, `delete` 등을 활용.

---

### **3) 복잡한 쿼리 처리**
- MyBatis는 복잡한 SQL 쿼리를 쉽게 작성할 수 있지만, JPA는 기본적으로 JPQL(Java Persistence Query Language)을 사용한다.
- 기존 MyBatis의 SQL 쿼리를 JPQL로 변환하거나, 변환이 어려운 경우 **네이티브 쿼리**를 사용.

---

## MyBatis와 JPA의 공존 전략

현실적으로 **MyBatis와 JPA를 혼합 사용하는 전략**이 자주 활용된다.  
- **기본적인 CRUD 작업**: JPA를 활용하여 간결한 코드 작성.
- **복잡한 쿼리 처리**: MyBatis로 SQL을 직접 작성.

이렇게 하면 JPA의 생산성과 MyBatis의 제어력을 모두 얻을 수 있다.  
특히, 기존 프로젝트에서 MyBatis를 사용 중이라면 모든 쿼리를 JPA로 전환하기보다는 일부 쿼리만 전환하여 혼합 사용을 고려할 수 있다.

---

## MyBatis를 선택해야 할 경우

다음과 같은 상황에서는 MyBatis가 더 적합할 수 있다:
1. **복잡한 SQL이 빈번히 사용되는 프로젝트**  
   다수의 조인, 서브쿼리, 집계 함수 등이 필요한 경우 MyBatis의 SQL 제어력이 유리하다.
2. **특정 DBMS 기능 활용**  
   DBMS에 특화된 기능(예: JSON 처리, 히스토리 테이블 등)을 사용할 경우.
3. **데이터베이스 중심의 레거시 시스템**  
   기존 SQL이 많거나 DB 중심 설계가 고정된 프로젝트.
4. **빠른 개발 시작이 필요한 경우**  
   MyBatis는 설정이 간단하고 빠르게 시작할 수 있다.

---

## 결론

MyBatis와 JPA는 각각의 강점이 분명하며, 프로젝트의 특성에 따라 선택이 달라질 수 있다.  
JPA는 객체 지향 설계와 잘 맞아 유지보수성과 생산성을 높이는 데 유리하지만, 복잡한 쿼리에서는 제약이 있을 수 있다.  
반면, MyBatis는 SQL 작성의 유연성과 성능 최적화에서 강점을 가지며, 데이터베이스 중심의 작업에 적합하다.

나는 개인적으로 **MyBatis가 더 친숙하고 선호**한다.  
특히 복잡한 SQL을 직접 작성하거나 데이터베이스 특화 기능을 사용할 때 MyBatis의 장점을 많이 느꼈다.  
그러나 JPA가 제공하는 높은 생산성과 유지보수성도 매력적이기 때문에, 프로젝트 요구사항에 따라 두 기술의 혼합 사용을 적극 고려하는 것이 최선이라고 생각한다.