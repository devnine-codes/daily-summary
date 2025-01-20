# Spring 역사

오늘 인프런 김영한님 강의를 다시 복습하면서 이전에는 지나쳤던 **이야기 - 자바 진영의 추운 겨울과 스프링의 탄생** 을 들으며 Spring의 탄생에 대해 알게 되었고 그 과정은 생각보다 재미있었다. 하여 이번엔 Spring Java 기반의 애플리케이션 개발에서 거의 표준으로 자리 잡은 **Spring Framework**의 역사와 발전 과정을 정리해보려고 한다.

---

## 1. Spring의 탄생

### 1.1 배경
Spring은 2002년 **로드 존슨(Rod Johnson)** 이 자신의 저서 *Expert One-on-One J2EE Design and Development*에서 제안한 프레임워크에서 시작되었다. 당시의 Java 개발 환경은 **EJB (Enterprise JavaBeans)** 가 주도하고 있었으나, EJB는 다음과 같은 단점으로 인해 개발자들에게 큰 불편을 초래했다.

- 복잡한 설정과 코드의 비효율성
- 과도한 XML 기반 설정
- 테스트와 배포 과정에서의 어려움

로드 존슨은 이러한 문제를 해결하고자 EJB의 대안으로 **경량화된 프레임워크**를 제안했고, 이것이 **Spring Framework**의 시초가 되었다.

---

## 2. 주요 버전과 진화

### 2.1 Spring Framework 1.x (2004)
- **핵심 개념 도입**:  
  Spring 1.x는 **IoC (Inversion of Control)** 와 **AOP (Aspect-Oriented Programming)** 라는 두 가지 주요 개념을 통해 EJB의 복잡성을 대체할 경량 프레임워크를 제안했다.
  - IoC: 객체 생성과 의존성 관리를 개발자가 아닌 컨테이너가 수행
  - AOP: 비즈니스 로직과 횡단 관심사(로깅, 트랜잭션 등)의 분리
- **초기 반응**:  
  개발자들 사이에서 빠르게 확산되며 EJB 대안으로 자리 잡기 시작

### 2.2 Spring Framework 2.x (2006)
- **XML 설정 개선**:  
  XML 기반 설정이 간소화되고, 선언적 트랜잭션 관리 기능이 추가
- **JDBC 지원 강화**:  
  반복적인 JDBC 작업을 줄이기 위한 템플릿 클래스(`JdbcTemplate`) 제공
- **초기 Hibernate 통합**:  
  ORM(Object-Relational Mapping) 기술과의 통합 지원

### 2.3 Spring Framework 3.x (2009)
- **Java Config 도입**:  
  XML 설정의 복잡함을 해결하기 위해 **Java 기반 설정**이 가능해졌다.  
- **REST 지원 강화**:  
  Spring MVC에서 RESTful 웹 서비스 개발을 공식 지원
- **SpEL (Spring Expression Language)**:  
  동적 값 처리와 조건부 로직에 활용할 수 있는 강력한 표현식 언어

### 2.4 Spring Framework 4.x (2013)
- **Java 8 지원**:  
  람다 표현식과 스트림 API 등 최신 Java 기능을 활용할 수 있게 됨
- **WebSocket 지원**:  
  실시간 양방향 통신을 위한 WebSocket 지원 추가
- **스프링 부트(Spring Boot) 탄생 배경**:  
  이 시점에서 애플리케이션 설정의 복잡성을 극단적으로 줄이기 위한 Spring Boot 프로젝트가 등장

### 2.5 Spring Framework 5.x (2017)
- **Reactive Programming 지원**:  
  Spring WebFlux를 통해 비동기 논리를 처리할 수 있는 리액티브 프로그래밍 모델 제공
- **Kotlin 지원**:  
  Kotlin 언어를 공식 지원하여 개발자의 선택 폭을 넓힘
- **Java 9 이상 지원**:  
  모듈 시스템과 같은 최신 Java 기능 호환성 강화

---

## 3. Spring의 생태계 확장

Spring Framework는 기본적인 웹 애플리케이션 개발뿐 아니라, 다음과 같은 다양한 생태계로 확장되었다.

### 3.1 Spring Boot
- **설정 간소화**:  
  "Zero Configuration"을 목표로 복잡한 설정 없이 애플리케이션 개발 가능
- **내장 서버**:  
  Tomcat, Jetty 같은 내장 웹 서버를 통해 빠른 실행 환경 제공
- **자동 설정**:  
  대부분의 기본 설정이 자동으로 이루어져 빠른 개발이 가능

### 3.2 Spring Cloud
- **마이크로서비스 지원**:  
  마이크로서비스 아키텍처에서 서비스 디스커버리, 분산 설정, 로드 밸런싱 등 핵심 기능 제공
- **분산 시스템 통합**:  
  Netflix OSS를 활용한 분산 환경 지원

---

## 4. Spring의 현재와 미래

Spring은 여전히 진화하고 있다.  
Spring Native, GraalVM 지원 등 최신 기술을 통합하여 성능과 유연성을 더욱 강화하고 있으며, 클라우드 및 마이크로서비스 환경에서의 역할을 계속 확장 중이다.

---

## 마무리

김영한님의 EJB 지옥 이야기를 들으며, 현재는 유용한 툴, 프레임워크, 라이브러리, 그리고 활성화된 커뮤니티 덕분에 정보를 얻기 쉬운 환경에서 개발하고 있다는 점을 새삼 느꼈다.  
반면, 과거의 열악한 환경에서도 개발을 이어온 선배 개발자분들께 깊은 존경심이 생겼다.  
끝으로 Spring은 EJB라는 그 겨울을 넘어서 새로운 시작, Spring 말 그대로 진짜 봄이라는 뜻에 나는 좋은 환경에서 개발하고 있구나 라는 것을 다시 한번 느꼈다.